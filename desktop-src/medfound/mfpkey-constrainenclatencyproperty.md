---
description: Specifies whether the encoder is constrained by a maximum latency requirement.
ms.assetid: 8148ae1e-239e-40fa-a88d-810a1d93d8e9
title: MFPKEY_CONSTRAINENCLATENCY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_CONSTRAINENCLATENCY Property

Specifies whether the encoder is constrained by a maximum latency requirement.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

If you leave this property at its default value of **VARIANT\_FALSE**, the encoder enumerates a default set of modes that have about 2000 milliseconds of encoder latency. If you set this property to **VARIANT\_TRUE**, you must also specify a maximum encoder latency by setting the [**MFPKEY\_MAXENCLATENCYMS**](mfpkey-maxenclatencymsproperty.md) property. In that case, the encoder creates modes that satisfy the latency requirement and enumerates only those modes. The encoder guarantees an output sample as soon as the encoder has received input for a time period equal to **MFPKEY\_MAXENCLATENCYMS**.

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

 

 
