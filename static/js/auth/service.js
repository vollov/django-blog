'use strict';

angular.module('user.services', [])
.factory('userService', [ '$http', 'API', function($http, API) {
	
	var service = {
			users : [], 
			groups : []
	};

	// if user was requested, return it.
	// else start a new http request.
	service.getAll = function() {

		return $http.get(API + 'users')
		.success(function(data) {
			angular.copy(data, service.users);
		});
	};
	
	service.getTags = function() {
		return $http.get(API + 'groups')
		.success(function(data) {
			angular.copy(data, service.groups);
		});
	};
	
	service.create = function(user) {
		return $http.post(API + 'users', user).success(function(data){
			service.users.push(data);
		});
	};
	
	service.update = function(user, id) {
		console.log('service put user by id = %s', id);
		return $http.put(API + 'users/' + id, user).success(function(data){
			//service.users.push(data);
			console.log('put return res=%j', data);
			return data;
		});
	};
	
	service.getByTag = function(slug) {
		console.log('service get users by group.slug = %s', slug);
		return $http.get(API + 'group/' + slug).success(function(data) {
			angular.copy(data, service.users);
		});
	};
	
	service.get = function(slug) {
		console.log('service get user by slug = %s', slug);
		return $http.get(API + 'user/' + slug).then(function(res) {
			return res.data;
		});
	};
	
	service.deleteById = function(id) {
		return $http.delete(API + 'users/' + id).then(function(res) {
			return res.data;
		});
	};
	
	return service;
}]);