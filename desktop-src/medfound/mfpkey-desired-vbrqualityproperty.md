---
description: Specifies the desired quality level for quality based (1-pass) variable-bit-rate (VBR) encoding of audio streams.
ms.assetid: 0bbb4f51-78c3-4455-bd96-9a6d80110220
title: MFPKEY_DESIRED_VBRQUALITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_DESIRED\_VBRQUALITY Property

Specifies the desired quality level for quality based (1-pass) variable-bit-rate (VBR) encoding of audio streams.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_UI4**

## Default Value

0

## Remarks

This value can be from 0 to 100, where 100 is maximum quality. A value of 0 indicates that the quality-based VBR encoding method is not to be used.

To enumerate VBR modes that meet a certain quality requirement, set the following encoder properties.

-   Set [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) to **VARIANT\_TRUE**.
-   Set [**MFPKEY\_CONSTRAIN\_ENUMERATED\_VBRQUALITY**](mfpkey-constrain-enumerated-vbrqualityproperty.md) to **VARIANT\_TRUE**.
-   Set **MFPKEY\_DESIRED\_VBRQUALITY** to the desired quality. For Lossless modes, set the desired quality to 100.

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

 

 
