        
        const loader = document.getElementById('loader');
        const contenido = document.getElementById('contenido');
        let totalstring = document.querySelector('medium');

        let totalstring2 = totalstring.innerHTML.replace(',', '');
        let order = parseInt(totalstring2)

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');

        function sendOrderConfirmed(orderData) {
            return fetch("/confirm-order/", {
                method: "post",
                body: JSON.stringify(orderData),
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                }
            });
        }
        paypal.Buttons({
            createOrder: function(data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value: order
                        }
                    }]
                });
            },
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(orderData) {
                    sendOrderConfirmed(orderData).then(res => {
                        window.location.replace("https://exonica.com.mx/gracias-por-comprar/")
                    })
                    // Successful capture! For dev/demo purposes:
                    
                });
            },

        }).render('#paypal-button-container');
