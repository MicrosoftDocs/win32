---
description: Specifies the device conformance template that you want to use for video encoding.
ms.assetid: cd2c068a-dbbc-42c5-bc92-bbb73f0259d1
title: MFPKEY_DECODERCOMPLEXITYREQUESTED Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_DECODERCOMPLEXITYREQUESTED Property

Specifies the device conformance template that you want to use for video encoding.

## Data Type

VT\_I4

## Default Value

1

## Constant for IPropertyBag

g\_wszWMVCDecoderComplexityRequested

## Data Type for IPropertyBag

VT\_BSTR

## Default Value for IPropertyBag

"MP"

## Remarks

The codec will attempt to encode the content using the device conformance template specified by this value. The actual template to which the encoded content conforms can be retrieved from the [MFPKEY\_DECODERCOMPLEXITYPROFILE](mfpkey-decodercomplexityprofileproperty.md) property after encoding.

This property must be one of the following values.



| Value for IPropertyStore | Value for IPropertyBag | Description         |
|--------------------------|------------------------|---------------------|
| 0                        | "SP"                   | simple profile      |
| 1                        | "MP"                   | main profile        |
| 2                        | "CP"                   | no longer supported |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




