'use strict';

angular.module('user.controllers', [ 'user.services'])
.controller('userCtrl', ['$scope', 'userService',
function($scope, userService) {
	$scope.users = userService.users;

	$scope.selectUser = function(row) {
		$scope.selectedRow = row;
	};
	
	$scope.deleteUser = function(user, index) {
		//console.log('delete user by id='+ user._id);
		userService.deleteById(user.id);
		$scope.users.splice(index, 1);
	};
}]);