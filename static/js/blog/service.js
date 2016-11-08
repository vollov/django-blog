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
	
	service.getByTag = function(slug) {
		console.log('service get blogs by tag.slug = %s', slug);
		return $http.get(API + 'tag/' + slug).success(function(data) {
			angular.copy(data, service.blogs);
		});
	};
	
	service.get = function(slug) {
		console.log('service get blog by slug = %s', slug);
		return $http.get(API + 'blog/' + slug).then(function(res) {
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