from __future__ import unicode_literals

from django.db import models

# Local Store of Corresponding Ledger. This way each vendor can sync to the portion of the ledger they want
class DonorDB(models.Model):
    name = models.CharField(max_length=600, blank=True, null=True)
    tokens = models.CharField(max_length=600, blank=True, null=True)
    email = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=600, blank=True, null=True)
    extra1 = models.CharField(max_length=600, blank=True, null=True)
    extra2 = models.CharField(max_length=600, blank=True, null=True)
    extra3 = models.CharField(max_length=600, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self):
        return self.id

class NgoDB(models.Model):
    name = models.CharField(max_length=600, blank=True, null=True)
    website = models.CharField(max_length=600, blank=True, null=True)
    email = models.CharField(max_length=600, blank=True, null=True)
    address = models.CharField(max_length=600, blank=True, null=True)
    image = models.CharField(max_length=600, blank=True, null=True)
    description1 = models.CharField(max_length=6000, blank=True, null=True)
    description2 = models.CharField(max_length=6000, blank=True, null=True)
    status = models.CharField(max_length=600, blank=True, null=True)
    extra1 = models.CharField(max_length=600, blank=True, null=True)
    extra2 = models.CharField(max_length=600, blank=True, null=True)
    extra3 = models.CharField(max_length=600, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self):
        return self.id

class ProjectDB(models.Model):
    owner = models.ForeignKey(NgoDB)
    name = models.CharField(max_length=600, blank=True, null=True)
    milestones = models.CharField(max_length=600, blank=True, null=True)
    total_raise = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=600, blank=True, null=True)
    delivery_date = models.CharField(max_length=600, blank=True, null=True)
    extra1 = models.CharField(max_length=600, blank=True, null=True)
    extra2 = models.CharField(max_length=600, blank=True, null=True)
    extra3 = models.CharField(max_length=600, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self):
        return self.id

class MilestonesDB(models.Model):
    project = models.ForeignKey(ProjectDB)
    owner = models.ForeignKey(NgoDB)
    name = models.CharField(max_length=600, blank=True, null=True)
    milestone_number = models.CharField(max_length=600, blank=True, null=True)
    total_raise = models.CharField(max_length=600, blank=True, null=True)
    current_raise = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=600, blank=True, null=True)
    delivery_date = models.CharField(max_length=600, blank=True, null=True)
    extra1 = models.CharField(max_length=600, blank=True, null=True)
    extra2 = models.CharField(max_length=600, blank=True, null=True)
    extra3 = models.CharField(max_length=600, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self):
        return self.id

class ContractDB(models.Model):
    ngo = models.ForeignKey(NgoDB)
    project = models.ForeignKey(ProjectDB)
    milestone = models.ForeignKey(MilestonesDB)
    donor = models.ForeignKey(DonorDB)
    c_type = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=600, blank=True, null=True)
    amount = models.CharField(max_length=600, blank=True, null=True)
    info = models.CharField(max_length=6000, blank=True, null=True)
    count = models.CharField(max_length=600, blank=True, null=True)
    extra1 = models.CharField(max_length=600, blank=True, null=True)
    extra2 = models.CharField(max_length=600, blank=True, null=True)
    extra3 = models.CharField(max_length=600, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self):
        return self.id

class MilestoneReview(models.Model):
    ngo = models.ForeignKey(NgoDB)
    project = models.ForeignKey(ProjectDB)
    milestone = models.ForeignKey(MilestonesDB)
    donor = models.ForeignKey(DonorDB)
    invested_amount = models.CharField(max_length=600, blank=True, null=True)
    rating_information = models.CharField(max_length=600, blank=True, null=True)
    rating_transparency = models.CharField(max_length=600, blank=True, null=True)
    rating_completion = models.CharField(max_length=600, blank=True, null=True)
    rating_accuracy = models.CharField(max_length=600, blank=True, null=True)
    rating5 = models.CharField(max_length=600, blank=True, null=True)
    rating6 = models.CharField(max_length=600, blank=True, null=True)
    rating7 = models.CharField(max_length=600, blank=True, null=True)
    status = models.CharField(max_length=600, blank=True, null=True)
    extra1 = models.CharField(max_length=600, blank=True, null=True)
    extra2 = models.CharField(max_length=600, blank=True, null=True)
    extra3 = models.CharField(max_length=600, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self):
        return self.id