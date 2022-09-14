---
description: Specifies the complexity of the encoding algorithm.
ms.assetid: 5dd34818-f282-4859-b423-97e9c4944aec
title: MFPKEY_ENCCOMPLEXITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_ENCCOMPLEXITY Property

Specifies the complexity of the encoding algorithm. The value is an integer between 0 and 100, where 0 specifies the least complex algorithm, and 100 specifies the most complex algorithm.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_UI4**

## Default Value

100 for Windows Media Audio 10 and Windows Media Audio 10 Professional

100 for the Windows Vista release of Windows Media Audio 10 Lossless

0 for the Windows 7 release Windows Media Audio 10 Lossless

## Remarks

If the [**MFPKEY\_CONSTRAINECOMPLEXITY**](mfpkey-constrainenccomplexityproperty.md) property has a value of **VARIANT\_TRUE**, the encoder adjusts the complexity of its algorithm according to the value of this property.

For the Windows Media Audio 10 encoder and the Windows Media Audio 10 Professional encoder, if the value of this property is 100, the encoder places a high demand on the CPU and produces the highest quality output. As the value of this property decreases, the demand on the CPU decreases, but the quality of the output also decreases.

For the Windows Media Audio 10 Lossless encoder, if the value of this property is 0, the encoder places a low demand on the CPU. As the value of this property increases, the demand on the CPU increases, and the size of the encoder output decreases slightly. The output is lossless regardless of the value of this property.

If you leave this property at its default value of **VARIANT\_FALSE**, the encoder uses its default algorithm. The default algorithm depends on which encoder you are using and which version of Windows is running. The following table describes the default behavior for the different combinations.



| Operating system | Default behavior                                                                                                                                                                                                |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Vista    | The Windows Media Audio 10, Windows Media Audio 10 Professional, and Windows Media Audio 10 Lossless encoders all use the most complex algorithm by default.                                                    |
| Windows 7        | The Windows Media Audio 10 and Windows Media Audio 10 Professional encoders use the most complex algorithm by default. The Windows Media Audio 10 Lossless encoder uses the least complex algorithm by default. |



 

If the [**MFPKEY\_CONSTRAINECOMPLEXITY**](mfpkey-constrainenccomplexityproperty.md) property has a value of **VARIANT\_FALSE**, the encoder ignores this property.

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

 

 
