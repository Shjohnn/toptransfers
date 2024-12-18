from django.shortcuts import render
from django.views import View
from .models import *
from collections import OrderedDict


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        context = {
            'clubs': clubs
        }
        return render(request, 'clubs.html', context)


class LatestransfersView(View):
    def get(self, request):
        latesttransfers = Transfer.objects.all()
        context = {
            'latesttransfers': latesttransfers
        }
        return render(request, 'latest-transfers.html', context)


class PlayersView(View):
    def get(self, request):
        players = Player.objects.all()
        context = {
            "players": players
        }
        return render(request, 'players.html', context)


class U20playersView(View):
    def get(self, request):
        u20players = Player.objects.filter(age__lt=20)
        context = {
            "u20players": u20players
        }
        return render(request, 'U-20 players.html', context)


class TryoutsView(View):
    def get(self, request):
        return render(request, 'tryouts.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class StatisticsView(View):
    def get(self, request):
        return render(request, 'stats.html')


class TransferRecordsView(View):
    def get(self, request):
        transfers = Transfer.objects.order_by('-price')[:50]
        context = {
            'transfers': transfers
        }
        return render(request, 'stats/transfer-records.html', context)


class Top50IncomeView(View):
    def get(self, request):
        club_transfers = {}
        for club in Club.objects.all():
            club_transfers[club] = 0
            for transfer in club.old_club.all():
                club_transfers[club] += transfer.price

        club_transfers = OrderedDict(sorted(club_transfers.items(), key=lambda item: item[1], reverse=True))
        context = {
            "club_transfers": club_transfers,
        }
        return render(request, 'stats/top-50-income-clubs.html', context)


class Top50ExpenditureView(View):
    def get(self, request):
        club_transfers = {}
        for club in Club.objects.all():
            club_transfers[club] = 0
            for transfer in club.new_club.all():
                club_transfers[club] += transfer.price

        club_transfers = OrderedDict(sorted(club_transfers.items(), key=lambda item: item[1], reverse=True))
        context = {
            "club_transfers": club_transfers,
        }
        return render(request, 'stats/top-50-expenditure.html', context)


class AccuratePredictionView(View):
    def get(self, request):
        return render(request, 'stats/accurate-prediction.html')
