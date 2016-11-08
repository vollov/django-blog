'use strict';

angular.module('blog.controllers', [ 'blog.services'])
.controller('BlogCtrl', ['$scope', 'blogService',
function($scope, blogService) {
	$scope.blogs = blogService.blogs;

	$scope.selectBlog = function(row) {
		$scope.selectedRow = row;
	};
	
	$scope.deletePost = function(blog, index) {
		//console.log('delete blog by id='+ blog._id);
		blogService.deleteById(blog.id);
		$scope.blogs.splice(index, 1);
	};
}])
.controller('BlogViewCtrl', ['$scope', 'blog', function($scope,blog) {
	$scope.blog = blog;
	$scope.markdown_content = blog.body;
}])
.controller('AppCtrl', ['$scope', 'SITE_NAME', function($scope,SITE_NAME) {
	$scope.site_name = SITE_NAME;
}])
.controller('AboutCtrl', ['$scope', function($scope) {
	$scope.blog = blog;
	$scope.markdown_content = blog.body;
}]);