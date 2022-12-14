from django.shortcuts import render

from accounts.models import OrganizationAccount
from lobbying.models import InterpersonalTie

from .models import PublicOfficial, SupportLevel


def index(request, slug):
    return render(request, 'lobbying/index.html', {})


def officials_directory(request, slug):
    org_account = OrganizationAccount.objects.get(slug=slug)
    public_officials = PublicOfficial.objects.all()
    #house_officials = PublicOfficial.objects.filter()
    context = {'public_officials': public_officials}
    return render(request, 'lobbying/public_officials.html', context=context)


def official_profile(request, official_id, slug):
    org_account = OrganizationAccount.objects.get(slug=slug)
    public_official = PublicOfficial.objects.get(id=official_id)
    support_levels = SupportLevel.objects.filter(public_official=official_id)
    interpersonal_ties = InterpersonalTie.objects.filter(public_official1=official_id)
    contacts = PublicOfficial.contacts
    context = {
        'slug': slug,
        'public_official': public_official,
        'support_levels': support_levels,
        'interpersonal_ties': interpersonal_ties,
        'contacts': contacts
    }
    return render(request, 'lobbying/public_official_profile.html', context=context)
