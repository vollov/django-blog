'use strict';

angular.module('blog.services', [])
.factory('blogService', [ '$http', 'API', function($http, API) {
	
	var service = {
			blogs : [], 
			tags : []
	};
	
	service.getAll = function() {
		return $http.get(API + 'blogs')
		.success(function(data) {
			angular.copy(data, service.blogs);
		});
	};
	
	service.getTags = function() {
		return $http.get(API + 'tags')
		.success(function(data) {
			angular.copy(data, service.tags);
		});
	};
	
	service.create = function(blog) {
		return $http.post(API + 'blogs', blog).success(function(data){
			service.blogs.push(data);
		});
	};
	
	service.update = function(blog, id) {
		console.log('service put blog by id = %s', id);
		return $http.put(API + 'blogs/' + id, blog).success(function(data){
			//service.blogs.push(data);
			console.log('put return res=%j', data);
			return data;
		});
	};
	
	service.get = function(id) {
		console.log('service get blog by id = %s', id);
		return $http.get(API + 'blogs/' + id).then(function(res) {
			return res.data;
		});
	};
	
	service.deleteById = function(id) {
		return $http.delete(API + 'blogs/' + id).then(function(res) {
			return res.data;
		});
	};
	
	return service;
}]);