---
Description: Specifies the encoding pattern for the encoder to use at the beginning of a group of pictures.
ms.assetid: 0744fdd5-8bff-47a9-ae97-90637d91ff37
title: MFPKEY\_CLOSEDENTRYPOINT Property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFPKEY\_CLOSEDENTRYPOINT Property

Specifies the encoding pattern for the encoder to use at the beginning of a group of pictures.

## Constant for IPropertyBag

**g\_wszWMVCClosedEntryPoint**

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

If you set this property to **VARIANT\_TRUE**, the encoding pattern is BBIBBP. If you set this property to **VARIANT\_FALSE**, the encoding pattern is IBBPBBP.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows XP, Windows Vista or Windows 7<br/>                                       |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




