---
description: Specifies whether the complexity of the audio encoding algorithm is constrained.
ms.assetid: a50b840f-9fe8-4291-b93f-f09c241fe802
title: MFPKEY_CONSTRAINENCOMPLEXITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_CONSTRAINENCOMPLEXITY Property

Specifies whether the complexity of the audio encoding algorithm is constrained.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

If you leave this property at its default value of **VARIANT\_FALSE**, the audio encoder uses its default algorithm. The default algorithm depends on the output type and which version of Windows is running. The following table describes the default behavior for the different combinations.



| Operating system | Default behavior                                                                                                                                                                                    |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Vista    | For all output types, the audio encoder uses the most complex algorithm by default.                                                                                                                 |
| Windows 7        | For Standard and Professional output types, the audio encoder uses the most complex algorithm by default. For Lossless output types, the audio encoder uses the least complex algorithm by default. |



 

If you set this property to **VARIANT\_TRUE**, you must also specify a complexity value by setting the [**MFPKEY\_ENCCOMPLEXITY**](mfpkey-enccomplexityproperty.md) property.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
