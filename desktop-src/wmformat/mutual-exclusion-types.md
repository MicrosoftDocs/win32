---
title: Mutual Exclusion Types
description: Mutual Exclusion Types
ms.assetid: bfe6cfe6-3df4-49c4-8015-fe4479b693c1
keywords:
- Windows Media Format SDK,mutual exclusion
- Advanced Systems Format (ASF),mutual exclusion
- ASF (Advanced Systems Format),mutual exclusion
- mutual exclusion,types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mutual Exclusion Types

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use mutual exclusion types to identify the nature of a mutual exclusion object in a profile. Mutual exclusion types are used as parameters for [**IWMMutualExclusion::GetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-gettype) and [**IWMMutualExclusion::SetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-settype).

The following table lists the identifiers for mutual exclusion types.



| Mutual exclusion type constant | GUID                                 |
|--------------------------------|--------------------------------------|
| CLSID\_WMMUTEX\_Language       | D6E22A00-35DA-11D1-9034-00A0C90349BE |
| CLSID\_WMMUTEX\_Bitrate        | D6E22A01-35DA-11D1-9034-00A0C90349BE |
| CLSID\_WMMUTEX\_Presentation   | D6E22A02-35DA-11D1-9034-00A0C90349BE |
| CLSID\_WMMUTEX\_Unknown        | D6E22A03-35DA-11D1-9034-00A0C90349BE |



 

## Related topics

<dl> <dt>

[**GUID Values**](guid-values.md)
</dt> </dl>

 

 




