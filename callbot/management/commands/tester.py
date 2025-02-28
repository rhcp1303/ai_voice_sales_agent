from django.core.management.base import BaseCommand
import logging
from ...services import twilio_service as helper
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'This is a utility management command for testing purpose'

    def handle(self, *args, **options):
        service = helper.TwilioService()
        service.make_call("+919315422432")
