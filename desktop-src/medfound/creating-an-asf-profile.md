---
description: This topic describes how to create as ASF profile in Microsoft Media Foundation.
ms.assetid: 9633bc88-12bd-404a-b779-878eb1ee5699
title: Creating an ASF Profile
ms.topic: article
ms.date: 05/31/2018
---

# Creating an ASF Profile

This topic describes how to create as ASF profile in Microsoft Media Foundation.

-   [Create a New Profile](#create-a-new-profile)
-   [Get the Profile from the ASF ContentInfo Object](#get-the-profile-from-the-asf-contentinfo-object)
-   [Get the Profile from a Presentation Descriptor](#get-the-profile-from-a-presentation-descriptor)
-   [Related topics](#related-topics)

## Create a New Profile

To create an empty ASF profile, call the [**MFCreateASFProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfprofile) function. This function returns a pointer to the [**IMFASFProfile**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfprofile) interface. The application can use this interface to add streams to the profile, and to configure each of the streams. For more information, see [Creating and Configuring ASF Streams](creating-and-configuring-asf-streams.md).

Optionally, the application can add mutual-exclusion objects to two or more streams. See [Using Mutual Exclusion for ASF Streams](using-mutual-exclusion-for-asf-streams.md).

## Get the Profile from the ASF ContentInfo Object

An application can get the ASF profile of an existing ASF file from the [ASF ContentInfo Object](asf-contentinfo-object.md). The profile is already configured and contains settings for the all of the streams in the file.

Initialize the ContentInfo object by parsing the ASF Header Object of the file. This is done through the [**IMFASFContentInfo::ParseHeader**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-parseheader) method. After all the Header Objects are read and the ASF library is populated, the profile for this file is generated. The application can get a pointer to this initialized profile by calling [**IMFASFContentInfo::GetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getprofile).

## Get the Profile from a Presentation Descriptor

You can get the profile object of an existing ASF file from the [presentation descriptor](presentation-descriptors.md) for the file, or from the [ASF ContentInfo](asf-contentinfo-object.md) object. In this case, the profile is already configured and contains settings for all of the streams in the file. This can be useful if you want to modify an existing ASF profile. For example, you might wish to re-encode a Windows Media Video file at a lower bit rate.

To get the profile from the presentation descriptor, call [**MFCreateASFProfileFromPresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfprofilefrompresentationdescriptor). This function parses the presentation descriptor, and populates an ASF profile with information about the media file. The function returns a pointer to the IMFASFProfile interface. You can then use this interface to modify the profile.

To get the presentation descriptor, call one of the following methods:

-   From the ASF media source, call [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor).
-   From the [ASF ContentInfo](asf-contentinfo-object.md) object, call [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor). Prior to calling this method, make sure that the ContentInfo object is initialized for reading. For more information, see "Initializing the ContentInfo Object from an Existing ASF File" in [Reading the ASF Header Object of an Existing File](reading-the-asf-header-object-of-an-existing-file.md). However, if you already have an initialized ContentInfo object, you can get the profile directly from it. This is described in "Getting the Profile from the ContentInfo Object " later in this topic.

The following example shows how to create a profile from a presentation descriptor. The function creates a media source for the file, gets the presentation descriptor from the media source, and creates a profile. This example assumes that *pszFileName* specifies the URL of an ASF file.


```C++
HRESULT GetASFProfile(PCWSTR pszFileName, IMFASFProfile** ppProfile)
{
    *ppProfile = NULL;

    IMFSourceResolver* pResolver = NULL;
    IUnknown* pSourceUnk = NULL;
    IMFMediaSource* pSource = NULL;
    IMFPresentationDescriptor* pPD = NULL;

    // Create the source resolver.
    HRESULT hr = MFCreateSourceResolver(&pResolver);

    // Use the source resolver to create the media source.
    if (SUCCEEDED(hr))
    {
        MF_OBJECT_TYPE ObjectType;

        hr = pResolver->CreateObjectFromURL(
                pszFileName,
                MF_RESOLUTION_MEDIASOURCE, 
                NULL,                      
                &ObjectType,               
                &pSourceUnk   
            );
    }

    // Get the IMFMediaSource interface from the media source.
    if (SUCCEEDED(hr))
    {
        hr = pSourceUnk->QueryInterface(IID_PPV_ARGS(&pSource));
    }

    // Get the presentation desccriptor.
    if (SUCCEEDED(hr))
    {
        hr = pSource->CreatePresentationDescriptor(&pPD);
    }

    // Get the profile from the presentation descriptor.
    if (SUCCEEDED(hr))
    {
        hr = MFCreateASFProfileFromPresentationDescriptor(pPD, ppProfile);
    }

    SafeRelease(&pResolver);
    SafeRelease(&pSourceUnk);
    SafeRelease(&pSource);
    SafeRelease(&pPD);
    return hr;
}
```



This example uses [SafeRelease](saferelease.md) to release interface pointers.

## Related topics

<dl> <dt>

[ASF Profile](asf-profile.md)
</dt> </dl>

 

 



