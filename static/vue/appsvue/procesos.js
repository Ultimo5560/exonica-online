new Vue({
    el: '#num_car',
    delimiters: ['{$', '$}'],
    data: {
        nc: '',
    },
    created() {
        var self = this;
        axios.get('/api/num-car/').then(function (response) {
            self.nc = response.data;
        })
        .catch(function (error){
            console.log(error);
        })
        
    }
}); 