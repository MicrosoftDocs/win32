---
title: Bandwidth Sharing
description: Bandwidth Sharing
ms.assetid: d33f3454-d20a-4b4d-9902-dabc5b806ad6
keywords:
- Windows Media Format SDK,bandwidth sharing
- Advanced Systems Format (ASF),bandwidth sharing
- ASF (Advanced Systems Format),bandwidth sharing
- Windows Media Format SDK,streams
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- bandwidth sharing,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Bandwidth Sharing

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can specify streams in a file that, when taken together, use less bandwidth than the sum of their stated bit rates combined. By specifying bandwidth sharing in the profile, you clarify to reading applications that the available bandwidth needed to stream the file is not what it might otherwise seem.

None of the objects of the Windows Media Format SDK change their behavior in response to bandwidth sharing information, which is provided solely so that reading applications can take it into account when determining whether a file can be played with restricted bandwidth delivery.

Bandwidth sharing is configured with a bandwidth sharing object and is added to a profile before beginning to write a file.

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Bandwidth Sharing Object**](bandwidth-sharing-object.md)
</dt> <dt>

[**IWMBandwidthSharing Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmbandwidthsharing)
</dt> <dt>

[**IWMProfile3 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofile3)
</dt> <dt>

[**Using Bandwidth Sharing**](using-bandwidth-sharing.md)
</dt> </dl>

 

 




