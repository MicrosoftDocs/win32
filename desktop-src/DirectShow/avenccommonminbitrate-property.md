---
description: Specifies the minimum bit rate, in bits per second. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.
ms.assetid: 57ef6c08-3bad-4d8d-8daf-61041b878802
title: AVEncCommonMinBitRate property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonMinBitRate property

Specifies the minimum bit rate, in bits per second. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonMinBitRate**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange).

## Remarks

The encoder enforces the minimum bit rate by increasing the encoding quality as necessary.

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

 

 




