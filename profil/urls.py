from django.conf.urls import url
from . import views, main_profile, group_view
#
urlpatterns = [
#	url(r'^/signup/$', main_profile.signup, name='signup'),
#	url(r'^/update/(?P<pk>[\-\w]+)/$', main_profile.edit_profile, name='profile_update')

#Add User
	url(r'^/add/(?P<pk>[0-9]+)$', views.TambahUSer, name='useradd'),
#Add Group
	url(r'^/add-group$', group_view.AddGruop, name='groupadd'),
#Add Profile
	url(r'^$', views.ProfileView, name='profiles'),
	url(r'^/detail/(?P<pk>[0-9]+)$', views.ProfileDetail, name='profile-detail'),
	url(r'^/tambah$', views.ProfileCreate, name='profile-tambah'),
	url(r'^/edit/(?P<pk>[0-9]+)$', views.ProfileEdit, name='profile-edit'),
	url(r'^/delete/(?P<pk>[0-9]+)$', views.ProfileDelete, name='profile-delete')
]