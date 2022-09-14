---
description: Specifies the precision of the DC coefficients, in bits. This property applies to MPEG video encoders.
ms.assetid: 2b4d11c1-767c-4466-8291-7959d841ae65
title: AVEncMPVIntraDCPrecision property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPVIntraDCPrecision property

Specifies the precision of the DC coefficients, in bits. This property applies to MPEG video encoders.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncMPVIntraDCPrecision**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange).

## Remarks

The usual range for this property is 8 to 11 bits. If the value is zero, the encoder selects the precision.

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

 

 




