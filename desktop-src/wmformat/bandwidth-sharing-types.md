---
title: Bandwidth Sharing Types
description: Bandwidth Sharing Types
ms.assetid: 2da15981-65d4-4d77-a68c-810ded18670c
keywords:
- Windows Media Format SDK,bandwidth sharing
- Advanced Systems Format (ASF),bandwidth sharing
- ASF (Advanced Systems Format),bandwidth sharing
- bandwidth sharing,types
ms.topic: article
ms.date: 05/31/2018
---

# Bandwidth Sharing Types

You can use bandwidth sharing types to identify the nature of a bandwidth sharing object in a profile. Bandwidth sharing types are used as parameters for [**IWMBandwidthSharing::GetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmbandwidthsharing-gettype) and [**IWMBandwidthSharing::SetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmbandwidthsharing-settype).

The following table lists the identifiers for bandwidth sharing types.



| Bandwidth sharing type constant      | GUID                                 |
|--------------------------------------|--------------------------------------|
| CLSID\_WMBandwidthSharing\_Exclusive | af6060aa-5197-11d2-b6af-00c04fd908e9 |
| CLSID\_WMBandwidthSharing\_Partial   | af6060ab-5197-11d2-b6af-00c04fd908e9 |



 

## Related topics

<dl> <dt>

[**GUID Values**](guid-values.md)
</dt> </dl>

 

 




