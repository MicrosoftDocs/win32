---
description: Specifies whether the Voice Capture DSP performs automatic gain control.
ms.assetid: 85ac8de0-ac36-4b34-a93d-0ac792a677b2
title: MFPKEY_WMAAECMA_FEATR_AGC Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_AGC Property

Specifies whether the Voice Capture DSP performs automatic gain control.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_FALSE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Automatic gain control is a digital signal processing (DSP) component that adjusts the gain so that the output level of the signal remains within the same approximate range.

This property can have the following values.



| Value          | Description                     |
|----------------|---------------------------------|
| VARIANT\_FALSE | Disable automatic gain control. |
| VARIANT\_TRUE  | Enable automatic gain control.  |



 

The default value of this property is VARIANT\_FALSE (disabled). Before setting this property, you must set the [MFPKEY\_WMAAECMA\_FEATURE\_MODE](mfpkey-wmaaecma-feature-modeproperty.md) property to VARIANT\_TRUE.

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

 

 
