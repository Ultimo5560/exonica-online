new Vue({
    el: '#num_car',
    delimiters: ['{$', '$}'],
    data: {
        lista_prod: '',
    },
    created() {
        var self = this;
        axios.get('/api/num-car/').then(function (response) {
            self.lista_prod = response.data;
            console.log(response.data)
        })
        .catch(function (error){
            console.log(error);
        })
        
    }
}); 