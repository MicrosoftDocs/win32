---
description: Specifies the number of encoding passes that the encoder supports.
ms.assetid: 8b476164-fd44-4277-89bd-ba9929bf93a2
title: AVEncCommonMultipassMode property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonMultipassMode property

Specifies the number of encoding passes that the encoder supports.

This property is read-only.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonMultipassMode**

## Property value

This property is returned as a range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange).

## Remarks

Decoding latency is defined as the amount of data the decoder must buffer. For example, setting this property to **VARIANT\_TRUE** on an MPEG video encoder limits the types of GOP structures the encoder can use.

To set the current encoding pass, set the [**AVEncCommonPassStart**](avenccommonpassstart-property.md) property.

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

 

 




