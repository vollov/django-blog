'use strict';

angular.module('markNote', ['ui.router','hc.marked', 'blog'])
.constant('API', '/api/v1.0/')
.constant('STATIC_ROOT','/static')
.constant('SITE_NAME','vollov.ca')
.config(['$stateProvider', '$urlRouterProvider', '$httpProvider', 'STATIC_ROOT',function($stateProvider, $urlRouterProvider, $httpProvider, STATIC_ROOT) {
	$stateProvider.state('blogs', {
		url : '/home',
		templateUrl : STATIC_ROOT + '/views/blog/list.html',
		controller : 'BlogCtrl',
		resolve: {
			postPromise: ['blogService', function(blogService){
				return blogService.getAll();
			}]
		}
	})
	.state('about', {
		url : '/about',
		controller : 'AboutCtrl',
		templateUrl : STATIC_ROOT + '/views/about.html',
		resolve : {
			blog : ['blogService',
			function(blogService) {
				return blogService.get('about');
			}]
		}
	})
	.state('privacy', {
		url : '/privacy',
		controller : 'AppCtrl',
		templateUrl : STATIC_ROOT + '/views/privacy.html'
	})
	.state('terms', {
		url : '/terms',
		controller : 'AppCtrl',
		templateUrl : STATIC_ROOT + '/views/terms.html'
	})
	.state('404', {
		url : '/404',
		templateUrl : STATIC_ROOT + '/views/404.html'
	})
	.state('blog-view', {
		url : '/blog/:slug',
		templateUrl : STATIC_ROOT + '/views/blog/view.html',
		controller : 'BlogViewCtrl',
		resolve : {
			blog : ['$stateParams', 'blogService',
			function($stateParams, blogService) {
				return blogService.get($stateParams.slug);
			}]
		}
	})
	.state('tag-view', {
		url : '/tag/:slug',
		templateUrl : STATIC_ROOT + '/views/blog/list.html',
		controller : 'BlogCtrl',
		resolve : {
			blogs : ['$stateParams', 'blogService',
			function($stateParams, blogService) {
				return blogService.getByTag($stateParams.slug);
			}]
		}
	});
	
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	
	$urlRouterProvider.otherwise('home');
}])
.config(['markedProvider', function (markedProvider) {
	markedProvider.setOptions({
		gfm: true,
		tables: true
	});
}]);