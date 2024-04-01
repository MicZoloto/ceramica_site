function loadProducts(subcatSlug, page) {
    $.ajax({
        url: '{% url "your_view_name" category.slug %}',
        data: {
            'subcat_slug': subcatSlug,
            'page': page
        },
        success: function (data) {
            // Тут ви додаєте товари до DOM
            if(data.products.length > 0) {
                data.products.forEach(function(product) {
                    $('#subcategory-' + subcatSlug).append('<div>' + product.name + '</div>'); // Доповніть елементами сторінки
                });
            }
        }
    });
}

$(".load-more").click(function() {
    var subcatSlug = $(this).data("subcategory");
    var nextPage = parseInt($(this).data("next-page"));
    loadProducts(subcatSlug, nextPage);
    $(this).data("next-page", nextPage + 1);
});