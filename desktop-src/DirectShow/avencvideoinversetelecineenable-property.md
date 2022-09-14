---
description: Specifies whether the encoder performs inverse telecine.
ms.assetid: 3467b0c8-c27d-448a-8cbf-971307e4c408
title: AVEncVideoInverseTelecineEnable property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoInverseTelecineEnable property

Specifies whether the encoder performs inverse telecine.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncVideoInverseTelecineEnable**

## Remarks

If the value is **VARIANT\_TRUE**, the encoder performs inverse telecine. If inverse telecine is not required, set this property to **VARIANT\_FALSE**. To perform inverse telecine outside of the encoder, set this property to **VARIANT\_FALSE** and set the [**AVEncVideoOutputScanType**](avencvideooutputscantype-property.md) property to eAVEncVideoOutputScan\_SameAsInput.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




