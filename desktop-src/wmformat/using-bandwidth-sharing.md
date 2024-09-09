---
title: Using Bandwidth Sharing
description: Using Bandwidth Sharing
ms.assetid: 1df61a3a-d34a-447e-a7ee-d5d409e7c4fa
keywords:
- Windows Media Format SDK,bandwidth sharing
- bandwidth sharing,about
- profiles,bandwidth sharing
- streams,bandwidth sharing
- bandwidth sharing,IWMProfile interface
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Bandwidth Sharing

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use bandwidth sharing objects to specify that certain streams, when combined, will not use more bandwidth than specified. The information in a bandwidth sharing object is not generated or verified by the writer nor used by the reader for anything.

When a file is written that has bandwidth sharing information in its profile, the data is stored in its header section. You can use the [**IWMProfile**](iwmprofile.md) interface in the reader to check for bandwidth sharing information when the file is played.

Each bandwidth sharing object is defined by two settings. First is the bandwidth, as defined by a bandwidth and a buffer window. The second setting is a bandwidth sharing type, which can be either exclusive or partial. Exclusive bandwidth sharing means that the constituent streams are played back one at a time, while partial means the streams are delivered concurrently.

## Related topics

<dl> <dt>

[**IWMProfile Interface**](iwmprofile.md)
</dt> <dt>

[**IWMProfile3::AddBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-addbandwidthsharing)
</dt> <dt>

[**IWMProfile3::CreateNewBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-createnewbandwidthsharing)
</dt> <dt>

[**IWMProfile3::GetBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-getbandwidthsharing)
</dt> <dt>

[**IWMProfile3::GetBandwidthSharingCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmprofile3-getbandwidthsharingcount)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 




