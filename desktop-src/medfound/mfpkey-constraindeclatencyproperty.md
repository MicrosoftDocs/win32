---
description: Specifies whether the encoder is constrained by a maximum decoder latency requirement.
ms.assetid: 054e445e-fc71-4d4f-9e9f-f5ff71f0b4ee
title: MFPKEY_CONSTRAINDECLATENCY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_CONSTRAINDECLATENCY Property

Specifies whether the encoder is constrained by a maximum decoder latency requirement.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

If you leave this property at its default value of **VARIANT\_FALSE**, the encoder enumerates a default set of modes that have about 1500 milliseconds of decoder latency. If you set this property to **VARIANT\_TRUE**, you must also specify a maximum decoder latency by setting the [**MFPKEY\_MAXDECLATENCYMS**](mfpkey-maxdeclatencymsproperty.md) property. In that case, the encoder creates modes that satisfy the latency requirement and enumerates only those modes. The encoder ensures that the preroll requirements (decoder buffer size) are less than or equal to **MFPKEY\_MAXDECLATENCYMS**.

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

 

 
