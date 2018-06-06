---
Description: Specifies the preferred number of samples per frame.
ms.assetid: ad629dbd-49d8-43d0-95a8-03f2043e397e
title: MFPKEY\_PREFERRED\_FRAMESIZE Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_PREFERRED\_FRAMESIZE Property

Specifies the preferred number of samples per frame.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/e995aaa1-d4c9-475f-b1fa-b9123cd5b653).

## Data Type

**VT\_UI4**

## Remarks

To specifiy a preferred frame size, set the following properties.

-   Set [**MFPKEY\_REQUESTING\_A\_FRAMESIZE**](mfpkey-requesting-a-framesizeproperty.md) to **VARIANT\_TRUE**.
-   Set **MFPKEY\_PREFERRED\_FRAMESIZE** to the number of samples you want in each frame.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




