'use strict';

angular.module('markNote', ['ui.router','hc.marked', 'blog'])
.constant('API', '/api/v1.0/')
.config(['$stateProvider', '$urlRouterProvider', '$httpProvider', function($stateProvider, $urlRouterProvider, $httpProvider) {
	$stateProvider.state('blogs', {
		url : '/blogs',
		templateUrl : '/views/blog/list.html',
		controller : 'BlogCtrl',
		resolve: {
			postPromise: ['blogService', function(blogService){
				return blogService.getAll();
			}]
		}
	})
//	.state('404', {
//		url : '/404',
//		templateUrl : '/views/404.html'
//	})
	.state('blog-view', {
		url : '/blog/view/:id',
		templateUrl : '/views/blog/view.html',
		controller : 'BlogViewCtrl',
		resolve : {
			post : ['$stateParams', 'blogService',
			function($stateParams, blogService) {
				return blogService.get($stateParams.id);
			}]
		}
	});
	
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	
	$urlRouterProvider.otherwise('blogs');
}])
.config(['markedProvider', function (markedProvider) {
	markedProvider.setOptions({
		gfm: true,
		tables: true
	});
}]);