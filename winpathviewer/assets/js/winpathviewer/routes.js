var app = angular.module('opal');
app.controller('WelcomeCtrl', function(){});

app.config(
    ['$routeProvider',
     function($routeProvider){
//	     $routeProvider.when('/',  {redirectTo: '/list'})

         $routeProvider.when('/',  {
             controller: 'WelcomeCtrl',
             templateUrl: '/templates/welcome.html'}
                            )

     }]);


String.prototype.cultureText = function() {
    var target = this;
    return target.replace(/\\.br\\/g, "\n")

    // return target.replace(new RegExp(search, 'g'), replacement);
};
