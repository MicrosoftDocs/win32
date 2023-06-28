---
title: Getting Profile Information at Playback
description: Getting Profile Information at Playback
ms.assetid: 4ea6c063-fd53-4b5e-ac01-9e2790322ace
keywords:
- Windows Media Format SDK,profiles
- Advanced Systems Format (ASF),profiles
- ASF (Advanced Systems Format),profiles
- Advanced Systems Format (ASF),mutual exclusion
- ASF (Advanced Systems Format),mutual exclusion
- Advanced Systems Format (ASF),bandwidth sharing
- ASF (Advanced Systems Format),bandwidth sharing
- streams,getting profile information at playback
- profiles,getting information at playback
- mutual exclusion,getting profile information at playback
- bandwidth sharing,getting profile information at playback
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Getting Profile Information at Playback

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Information from the profile used to create a file is stored in the header section of the file. Both reader objects can access the profile information from the file header. There are several reasons why you might want to access profile data from the reader. Most commonly, you will need to retrieve information about streams, mutual exclusion objects, and bandwidth sharing objects.

Both the asynchronous reader object and the synchronous reader object can be queried for the [**IWMProfile**](iwmprofile.md) interface. No changes made to the profile information can have any affect on the file in the reader. For more information about accessing profile information, see [Working with Profiles](working-with-profiles.md).

## Stream Information

It is sometimes important to know how a stream is configured. When you retrieve media properties from the either of the reader objects, you get the properties of the outputs. Output properties describe how the uncompressed data from a stream is going to be delivered by the reader, not how the stream is configured within the ASF file.

When receiving uncompressed stream samples from either reader object, you must use the profile information to identify the format of the compressed data. This is particularly important if you are going to write the compressed stream to another ASF file.

You also need to access stream information when using smart recompression to transcode an audio stream to a lower bit rate.

You may want to determine whether a stream was written using variable bit rate (VBR) encoding. You cannot access any VBR information from the **IWMProfile** interface of either reader object. This is because the VBR information is not stored in the file after encoding. You can determine whether a stream was created using VBR encoding by obtaining a pointer to the [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) interface of the reader object and calling [**IWMHeaderInfo::GetAttributeByName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getattributebyname). You must specify the stream number and pass g\_wszIsVBR as the attribute name.

## Mutual Exclusion Information

If you want to create a reading application that uses mutual exclusion, you will want to access the information about any mutual exclusion objects included in the profile. For all mutual exclusion types except bit rate, the reading application is responsible for any stream switching that is required. To switch streams, you need to know which streams are which.

## Bandwidth Sharing Information

Bandwidth sharing objects that are included in a profile are included only for informational purposes. Neither the writer object nor either of the reader objects takes any action as a result of bandwidth sharing data. If you want to use bandwidth sharing in your reading application, you must access the bandwidth sharing information from the profile data.

> [!Note]  
> Not all of the information from the profile used to create a file is present in the file header. As a general rule, data that is used only at the time of encoding is not persisted in the file. This includes input settings that were set using the [**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting) method, as well as properties set using the [**IWMPropertyVault::SetProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmpropertyvault-setproperty) method.

 

## Related topics

<dl> <dt>

[**IWMProfile Interface**](iwmprofile.md)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> </dl>

 

 




