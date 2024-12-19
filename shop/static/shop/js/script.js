document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    const cartItemCount = document.querySelector('.cart-item-count');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const jewelryId = button.dataset.jewelryId;
            
            // Здесь может быть отправка AJAX запроса на сервер для добавления в корзину
            // Предположим, что товар успешно добавлен в корзину
            // Обновляем счетчик товаров в корзине на клиентской стороне

            // Увеличиваем текущее количество на 1 (предполагаем, что начальное значение 0)
            let currentCount = parseInt(cartItemCount.textContent);
            currentCount += 1;
            cartItemCount.textContent = currentCount;
        });
    });
});
