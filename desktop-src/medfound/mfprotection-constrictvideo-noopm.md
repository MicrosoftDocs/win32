---
Description: 'This attribute specifies additional protection offered by a video output trust authority(OTA) when a connector does not offer output protection.'
ms.assetid: 'D3EAD386-E730-44E8-9E05-773E1E2175C5'
title: 'MFPROTECTION\_CONSTRICTVIDEO\_NOOPM attribute'
---

# MFPROTECTION\_CONSTRICTVIDEO\_NOOPM attribute

This attribute specifies additional protection offered by a video output trust authority(OTA) when a connector does not offer output protection.

## Data type

**GUID**

## Remarks

This is an additional protection offered by a video output trust authority(OTA) when a connector does not offer output protection (see[**IMFOutputTrustAuthority**](imfoutputtrustauthority.md)). In this case the OTA may offer this protection whose effect is the same as the [MFPROTECTION\_CONSTRICTVIDEO](mfprotection-constrictvideo.md) protection. This is defined to avoid confusion with previous calls to [**IMFOutputPolicy::GenerateRequiredSchemas**](imfoutputpolicy-generaterequiredschemas.md) interactions where the presence of MFPROTECTION\_CONSTRICTVIDEO protection was used to help identify the desktop window manager pseudo-connector.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




