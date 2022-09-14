---
description: Specifies whether the Voice Capture DSP performs noise filling.
ms.assetid: 8bb64686-8f02-4e0d-a664-aeee1744fc8e
title: MFPKEY_WMAAECMA_FEATR_NOISE_FILL Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_NOISE\_FILL Property

Specifies whether the Voice Capture DSP performs noise filling.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_TRUE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Noise filling adds a small amount of noise to portions of the signal where center clipping has removed the residual echoes. This results in a better experience for the user than leaving silent gaps in the signal.

This property can have the following values.



| Value          | Description            |
|----------------|------------------------|
| VARIANT\_TRUE  | Enable noise filling.  |
| VARIANT\_FALSE | Disable noise filling. |



 

The default value of this property is VARIANT\_TRUE (enabled). Before setting this property, you must set the [MFPKEY\_WMAAECMA\_FEATURE\_MODE](mfpkey-wmaaecma-feature-modeproperty.md) property to VARIANT\_TRUE.

The DSP uses this property only when AEC processing is enabled.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Voice Capture DSP](voicecapturedmo.md)
</dt> </dl>

 

 
