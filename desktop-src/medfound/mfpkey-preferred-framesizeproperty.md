---
description: Specifies the preferred number of samples per frame.
ms.assetid: ad629dbd-49d8-43d0-95a8-03f2043e397e
title: MFPKEY_PREFERRED_FRAMESIZE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_PREFERRED\_FRAMESIZE Property

Specifies the preferred number of samples per frame.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_UI4**

## Remarks

To specifiy a preferred frame size, set the following properties.

-   Set [**MFPKEY\_REQUESTING\_A\_FRAMESIZE**](mfpkey-requesting-a-framesizeproperty.md) to **VARIANT\_TRUE**.
-   Set **MFPKEY\_PREFERRED\_FRAMESIZE** to the number of samples you want in each frame.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
