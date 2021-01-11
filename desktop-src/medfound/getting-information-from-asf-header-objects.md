---
description: ASF header information is stored in the ASF Header Objects of a media file.
ms.assetid: 1654af97-f4fe-427f-b562-3b109e921719
title: Getting Information from ASF Header Objects
ms.topic: article
ms.date: 05/31/2018
---

# Getting Information from ASF Header Objects

ASF header information is stored in the ASF Header Objects of a media file. Media Foundation provides the [ASF ContentInfo Object](asf-contentinfo-object.md) to work with the Header Object. A populated ContentInfo object is required in order for the application to read header information of an existing file. This is achieved by calling [**IMFASFContentInfo::ParseHeader**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-parseheader). If parsing completes successfully, the ASF library for the file, which is maintained internally by Media Foundation, is populated with header information from various Header Objects. Some of these properties are exposed to the application, which it can retrieve through attributes on the presentation descriptor, stream descriptor, the profile, and metadata properties.

For the complete list of attributes, see [Media Foundation Attributes for ASF Header Objects](media-foundation-attributes-for-asf-header-objects.md).

## Retrieving Header Information from a Presentation Descriptor

A presentation descriptor object contains the description of a particular media source, in this case the ASF media source. If the **ParseHeader** call completes successfully, file-level information from the Header Object is stored as attributes on the presentation descriptor. To create the presentation descriptor, call [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor). This method returns a pointer to a populated presentation descriptor object that contains these attributes for the ASF file associated with the ContentInfo object. To get values for specific attributes, call **IMFAttributes::Getxxx** methods on the presentation descriptor and specify the **MF\_PD\_ASF\_xxx** attribute.

The following example code retrieves the play duration of an ASF file, specified by a ContentInfo object.


```C++
HRESULT GetPlayDuration(
    IMFASFContentInfo *pContentInfo,  // An initialized ContentInfo object. 
    UINT64 *pcbPlayDuration           // Receives the play duration.
    )
{
    IMFPresentationDescriptor* pPD = NULL;

    HRESULT hr = pContentInfo->GeneratePresentationDescriptor(&pPD);
    if (SUCCEEDED(hr))
    {
        hr = pPD->GetUINT64(MF_PD_ASF_FILEPROPERTIES_PLAY_DURATION, pcbPlayDuration);
        pPD->Release();
    }
    return hr;
}

```



For more information about presentation descriptors in general, see [Presentation Descriptors](presentation-descriptors.md).

For the complete set of presentation descriptor attributes, see [Presentation Descriptor Attributes](presentation-descriptor-attributes.md).

## Retrieving Header Information from a Stream Descriptor

A stream descriptor object exposes the [**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor) interface and describes the characteristics of the streams in the file. The presentation descriptor for the ASF content contains one or more stream descriptors that represent the streams listed in the Header Object. After the call to [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) completes successfully, the underlying stream descriptors are populated with stream-level information from the various Header Objects. To get a stream descriptor for an ASF stream, call [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorbyindex) on the presentation descriptor that is generated from the ContentInfo object.

Some of the stream properties are set as attributes on stream descriptors. Call **IMFAttributes::Getxxx** methods on a stream descriptor and specify the **MF\_SD\_ASF\_xxx** attribute.

For the complete set of stream descriptor attributes, see "ASF-Specific Stream Descriptor" attributes listed in [Stream Descriptor Attributes](stream-descriptor-attributes.md).

## Retrieving Header Information from the Profile Object

In addition to stream descriptors, the ASF profile object also describes the stream properties. To get the profile of an existing ASF file, call [**IMFASFContentInfo::GetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getprofile). The ASF profile object returned by this method does not include any of the **MF\_PD\_ASF\_xxx** attributes. These attributes are available to the application only after it calls [**MFCreateASFProfileFromPresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfprofilefrompresentationdescriptor) to generate the profile object from a presentation descriptor. You can use the profile to get pointers to the mutual exclusion and stream prioritization objects.

For information about the profile object, see [ASF Profile](asf-profile.md) .

## Retrieving Metadata from Header Objects

An ASF file can contain several metadata properties that are set during file encoding. An application can enumerate these properties with the ContentInfo object. Some of these properties, such as variable bit rate (VBR) information, are available to the application through attributes on presentation descriptor, stream descriptors, and media types for the media file. These attributes are set on the ContentInfo object during initialization through the [**ParseHeader**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-parseheader) call.

## Related topics

<dl> <dt>

[ASF ContentInfo Object](asf-contentinfo-object.md)
</dt> </dl>

 

 



