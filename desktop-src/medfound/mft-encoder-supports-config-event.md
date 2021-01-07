---
description: Specifies that the MFT encoder supports receiving MEEncodingParameter events while streaming.
ms.assetid: 8DE04537-641C-4154-9C7F-A7D025CA4C39
title: MFT_ENCODER_SUPPORTS_CONFIG_EVENT attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_ENCODER\_SUPPORTS\_CONFIG\_EVENT attribute

Specifies that the MFT encoder supports receiving [MEEncodingParameter](meencodingparameters.md) events while streaming.

## Data type

**Bool** stored as **UINT32**

## Remarks

Sent by the MFT encoder through [**IMFTransform::ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                             |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mftransform.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFTransform::ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent)
</dt> </dl>

 

 




