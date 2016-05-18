from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

urlpatterns = [
	url(r'^(?i)ConnectFour/$', RedirectView.as_view(url='/games/ConnectFour/', permanent=False)),
	url(r'^(?i)OnlineGo/$', RedirectView.as_view(url='/games/OnlineGo/', permanent=False)),
	url(r'^(?i)Mancala/$', RedirectView.as_view(url='/games/Mancala/', permanent=False)),
	url(r'^(?i)UltimateTicTacToe/$', RedirectView.as_view(url='/games/UltimateTicTacToe/', permanent=False)),
	url(r'^(?i)LameDuck/$', RedirectView.as_view(url='/games/LameDuck/', permanent=False)),
	url(r'^(?i)Maze/$', RedirectView.as_view(url='/tools/Maze/', permanent=False)),
	url(r'^(?i)PrimeFactorizer/$', RedirectView.as_view(url='/tools/PrimeFactorizer/', permanent=False)),
	url(r'^(?i)Grapher/$', RedirectView.as_view(url='/tools/Grapher/', permanent=False)),
	url(r'^(?i)HappyNumbers/$', RedirectView.as_view(url='/tools/HappyNumbers/', permanent=False)),
	url(r'^(?i)ReveresLatsLettesr/$', RedirectView.as_view(url='/tools/ReveresLatsLettesr/', permanent=False)),
	url(r'^(?i)ReveresLatsLettre/$', RedirectView.as_view(url='/tools/ReveresLatsLettesr/', permanent=False)),
	url(r'^(?i)ReverseLastLetter/$', RedirectView.as_view(url='/tools/ReveresLatsLettesr/', permanent=False)),
	url(r'^(?i)ReverseLastLetters/$', RedirectView.as_view(url='/tools/ReveresLatsLettesr/', permanent=False)),
	url(r'^(?i)ImageEditor/$', RedirectView.as_view(url='/tools/ImageEditor/', permanent=False)),
	url(r'^(?i)login/$', RedirectView.as_view(url='/account/login/', permanent=False)),
	url(r'^(?i)logout/$', RedirectView.as_view(url='/account/logout/', permanent=False)),
	url(r'^(?i)register/$', RedirectView.as_view(url='/account/register/', permanent=False)),
	url(r'^(?i)reset_password/$', RedirectView.as_view(url='/account/reset_password/', permanent=False)),
	url(r'^(?i)blog/$', RedirectView.as_view(url='/blog/', permanent=False)),
	url(r'^(?i)games/$', RedirectView.as_view(url='/games/', permanent=False)),
	url(r'^(?i)tools/$', RedirectView.as_view(url='/tools/', permanent=False)),
]