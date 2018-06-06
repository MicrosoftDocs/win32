---
Description: Specifies whether the core encoder uses the &\#0034;Plus&\#0034; feature.
ms.assetid: 1ace09da-7dee-469e-a533-63b40ac747ab
title: MFPKEY\_ENHANCED\_WMA Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_ENHANCED\_WMA Property

Specifies whether the core encoder uses the "Plus" feature.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/e995aaa1-d4c9-475f-b1fa-b9123cd5b653).

## Data Type

**VT\_UI4**

## Default Value

0

## Remarks

This property is available only for Windows Media Audio Lossless.

If you leave this property at its default value of 0, or if you set it to 1, the core encoder decides whether the "Plus" portion should be used. If you set this property to 2, the core encoder does not use the "Plus" feature.

This property alters the enumerated media types, so if you set it, you must do so before you set the output type.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




