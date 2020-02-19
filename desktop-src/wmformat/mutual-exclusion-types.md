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
ms.date: 05/31/2018
---

# Mutual Exclusion Types

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

 

 




