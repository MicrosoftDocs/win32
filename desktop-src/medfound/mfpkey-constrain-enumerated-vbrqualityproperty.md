---
description: Specifies whether modes enumerated by the encoder are limeted to those that meet a quality requirement given by MFPKEY\_DESIRED\_VBRQUALITY.
ms.assetid: b2f1d5c5-d2bb-4a8a-94ea-fd969e07bb0e
title: MFPKEY_CONSTRAIN_ENUMERATED_VBRQUALITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_CONSTRAIN\_ENUMERATED\_VBRQUALITY Property

Specifies whether modes enumerated by the encoder are limeted to those that meet a quality requirement given by [**MFPKEY\_DESIRED\_VBRQUALITY**](mfpkey-desired-vbrqualityproperty.md).

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

To enumerate VBR modes that meet a certain quality requirement, set the following encoder properties.

-   Set [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) to **VARIANT\_TRUE**.
-   Set **MFPKEY\_CONSTRAIN\_ENUMERATED\_VBRQUALITY** to **VARIANT\_TRUE**.
-   Set [**MFPKEY\_DESIRED\_VBRQUALITY**](mfpkey-desired-vbrqualityproperty.md) to the desired quality. For Lossless modes, set the desired quality to 100.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista or Windows 7<br/>                                                   |
| Header<br/> | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
