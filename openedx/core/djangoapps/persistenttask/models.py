"""
Models to support persistent tasks.
"""

from django.db import models
from jsonfield import JSONField


class FailedTask(models.Model):
    """
    Representation of tasks that have failed
    """
    task_name = models.CharField(max_length=255, db_index=True)
    task_id = models.CharField(max_length=255)
    args = JSONField(blank=True)
    kwargs = JSONField(blank=True)
    exc = models.CharField(max_length=255)
    datetime_failed = models.DateTimeField()
    datetime_resolved = models.DateTimeField(blank=True, null=True, default=None, db_index=True)

    def __unicode__(self):
        return u'FailedTask: {task_name}, args={args}, kwargs={kwargs} ({resolution})'.format(
            task_name=self.task_name,
            args=self.args,
            kwargs=self.kwargs,
            resolution=u"not resolved" if self.datetime_resolved is None else "resolved"
        )
