# scraper/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from .tasks import scrape_coin_data

class StartScrapingView(APIView):
    def post(self, request):
        coin_acronyms = request.data.get('coins', [])
        job = scrape_coin_data.apply_async(args=[coin_acronyms])
        return Response({'job_id': job.id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        job = AsyncResult(job_id)
        if job.state == 'PENDING':
            response = {
                'job_id': job_id,
                'status': job.state,
                'tasks': []
            }
        elif job.state != 'FAILURE':
            response = {
                'job_id': job_id,
                'status': job.state,
                'tasks': job.result
            }
        else:
            response = {
                'job_id': job_id,
                'status': job.state,
                'error': str(job.info)
            }
        return Response(response)
