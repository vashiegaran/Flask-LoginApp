

(function(){

	angular.module('flask', []).controller('controller', function($scope, $http){


		$scope.logIn = function(){
			
				if($scope.login.email && $scope.login.password){
					console.log($scope.login);

					$http.post('/login', $scope.login).success(function(response){
						console.log(response)
				})
				
			};//end of logIn function

		}


	})

})();