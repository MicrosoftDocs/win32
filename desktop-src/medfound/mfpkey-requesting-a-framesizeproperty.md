---
Description: Specifies whether the encoder should use a preferred frame size given in number of samples per frame.
ms.assetid: c9baeff7-53fb-425f-b07b-4066a705ca54
title: MFPKEY\_REQUESTING\_A\_FRAMESIZE Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_REQUESTING\_A\_FRAMESIZE Property

Specifies whether the encoder should use a preferred frame size given in number of samples per frame.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx).

## Data Type

**VT\_BOOL**

## Remarks

To specifiy a preferred frame size, set the following properties.

-   Set **MFPKEY\_REQUESTING\_A\_FRAMESIZE** to VARIANT\_TRUE.
-   Set [**MFPKEY\_PREFERRED\_FRAMESIZE**](mfpkey-preferred-framesizeproperty.md) to the number of samples you want in each frame.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




