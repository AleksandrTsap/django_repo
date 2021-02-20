"use strict";

window.onload = function () {
    console.log('DOM READY');
    $('.basket_record').on('click', "input[type='number']", function (event) {
        let qty = event.target.value;
        let basketItemPk = event.target.name;
        console.log(basketItemPk, qty);
        $.ajax({
            url: "/basket/update/" + basketItemPk + "/" + qty + "/",
            success: function (data) {
                if (data.status) {
                    $('.basket_summary').html(data.basket_summary);
                    $('.product_cost').html(data.product_cost);
                }
            },
        });
    });
}
