---
description: Specifies whether the Voice Capture DSP performs center clipping.
ms.assetid: 6830cadd-fa8d-41e1-ac11-a6c8f2795941
title: MFPKEY_WMAAECMA_FEATR_CENTER_CLIP Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_CENTER\_CLIP Property

Specifies whether the Voice Capture DSP performs center clipping.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_TRUE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Center clipping is a process that removes small echo residuals that remain after AEC processing, in single-talk situations (when speech occurs only on one end of the line).

This property can have the following values.



| Value          | Description              |
|----------------|--------------------------|
| VARIANT\_FALSE | Disable center clipping. |
| VARIANT\_TRUE  | Enable center clipping.  |



 

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

 

 
