## Условие задания:

В этом домашнем задании мы создадим заготовку сервиса на FastAPI по приёму заказов. Какие шаги для этого нужно сделать:

RUS:
1. Описать 2 сущности (Pydantic models в нашем случае):
    1. `User` с полями `id` и `name`
    2. `Order` с полями `id`, `product_name`, `product_count`, `is_cancelled` (отменен заказ или нет) и `user_id` (id
       пользователя, создавшего заказ)
2. Создать списки users и orders для хранения сущностей
3. Написать следующие http-обработчики с применением описанных Pydantic models (точный url остается на ваше усмотрение):
    1. `POST` запрос, принимающий в теле запроса (Body) поле имя пользователя. Создает пользователя в списке users.
       Возвращает id созданного пользователя
    2. `GET` запрос, принимающий в Path параметре `id` пользователя (`/{user_id}`). Возвращает id и имя
       пользователя.
       Если пользователя с таким id не существует, то вернуть HTTPException со статусом 404.
    3. `POST` запрос, принимающий в теле запроса (Body) поле `user_id`, `product_name` и `product_count` для
       заказа. Создает заказ в списке orders. Возвращает id созданного заказа.
       Если пользователя с таким id не существует, то вернуть HTTPException со статусом 404.
    4. `PATCH` запрос, принимающий в Path параметре `id` заказа (`/{order_id}`). Отменяет заказ с данным id.
       Если заказа с таким id не существует, то вернуть HTTPException со статусом 404.
    5. `DELETE` запрос, принимающий в Path параметре `id` заказа (`/{order_id}`).
       Удаляет заказ из списка orders.
       Если заказа с таким id не существует, то вернуть HTTPException со статусом 404.
    6. `GET` запрос, принимающий в Path параметре `id` заказа,
       а также в Query параметре поля `product_name` и `is_cancelled` (`/{order_id}?product_name=...&is_cancelled=...`).
       Возвращает суммарное кол-во товаров, которые упоминаются в заказах с именем `product_name` и
       статусом `is_cancelled`
4. Запустить написанный FastAPI сервер на 8080 порту. Проверить работу сервиса через Swagger

ENG:
1. Describe 2 entities (Pydantic models in our case):
    1. `User` with `id` and `name` fields
    2. `Order` with fields `id`, `product_name`, `product_count`, `is_cancelled` (whether the order was canceled or not) and `user_id` (id
       user who created the order)
2. Create lists of users and orders to store entities
3. Write the following http handlers using the described Pydantic models (the exact url remains at your discretion):
    1. A `POST` request that accepts the user name field in the request body. Creates a user in the users list.
       Returns the id of the created user
    2. A `GET` request that accepts the `id` of the user (`/{user_id}`) in the Path parameter. Returns id and name
       the user.
       If the user with this id does not exist, then return an HttpException with the status 404.
    3. A `POST` request that accepts the `user_id`, `product_name` and `product_count` fields in the request body (Body) for
       order's. Creates an order in the orders list. Returns the id of the created order.
       If the user with this id does not exist, then return an HttpException with the status 404.
    4. `PATCH' request that accepts the `id` of the order (`/{order_id}`) in the Path parameter. Cancels an order with this id.
       If an order with this id does not exist, then return an HttpException with the status 404.
    5. `DELETE' the request that accepts the `id` of the order (`/{order_id}`) in the Path parameter.
       Removes an order from the orders list.
       If an order with this id does not exist, then return an HttpException with the status 404.
    6. `GET` request that accepts the `id` of the order in the Path parameter,
       and also in the Query parameter of the `product_name` and `is_cancelled` fields (`/{order_id}?product_name=...&is_cancelled=...`).
Returns the total number of products that are mentioned in orders with the name `product_name` and
       status `is_cancelled`
4. Run the server written by Fastagi on port 8080. Check the operation of the service via Swagger


