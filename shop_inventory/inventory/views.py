from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q

from .models import Item
from .forms import ItemForm


class HomeView(TemplateView):
    """Landing page with welcome board and quick actions."""
    template_name = "inventory/home.html"


class ItemCreateView(CreateView):
    """Add a new inventory item."""
    model = Item
    form_class = ItemForm
    template_name = "inventory/item_form.html"
    success_url = reverse_lazy("inventory:item-list")


class ItemUpdateView(UpdateView):
    """Edit an existing inventory item."""
    model = Item
    form_class = ItemForm
    template_name = "inventory/item_form.html"
    success_url = reverse_lazy("inventory:item-list")


class ItemDeleteView(DeleteView):
    """Delete an item (confirmation page)."""
    model = Item
    template_name = "inventory/item_confirm_delete.html"
    success_url = reverse_lazy("inventory:item-list")


class ItemListView(ListView):
    """
    List items with optional search/filter:

    * `q` – free‑text search in name or category
    * `in_stock` = '1' – restrict to items where quantity > 0
    """
    model = Item
    template_name = "inventory/item_list.html"
    context_object_name = "items"
    paginate_by = 10  # remove or tweak as you like

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        in_stock = self.request.GET.get("in_stock")

        if query:
            qs = qs.filter(
                Q(name__icontains=query) | Q(category__icontains=query)
            )
        if in_stock == "1":
            qs = qs.filter(quantity__gt=0)

        return qs.order_by("-updated_at")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Preserve search state in the template
        ctx["q"] = self.request.GET.get("q", "")
        ctx["in_stock"] = self.request.GET.get("in_stock", "")
        return ctx
