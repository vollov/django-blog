'use strict';

angular.module('blog.controllers', [ 'blog.services'])
.controller('PostCtrl', ['$scope', 'postService',
function($scope, postService) {
	$scope.blogs = postService.blogs;

	$scope.selectBlog = function(row) {
		$scope.selectedRow = row;
	};
	
	$scope.deletePost = function(blog, index) {
		//console.log('delete blog by id='+ blog._id);
		postService.deleteById(blog.id);
		$scope.blogs.splice(index, 1);
	};
}])
.controller('PostViewCtrl', ['$scope', 'blog', function($scope,blog) {
	$scope.blog = blog;
	$scope.markdown_content = blog.body;
}]);