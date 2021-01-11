---
description: Specifies whether the Voice Capture DSP performs microphone array preprocessing.
ms.assetid: 0f197165-e6e5-456b-9615-1edc8ada7bb5
title: MFPKEY_WMAAECMA_FEATR_MICARR_PREPROC Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_MICARR\_PREPROC Property

Specifies whether the Voice Capture DSP performs microphone array preprocessing.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_TRUE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Preprocessing can remove stationary tones that interfere with processing, such as a tone with a fixed pitch.

This property can have the following values.



| Value          | Description            |
|----------------|------------------------|
| VARIANT\_FALSE | Disable preprocessing. |
| VARIANT\_TRUE  | Enable preprocessing.  |



 

The default value of this property is VARIANT\_TRUE (enabled). Before setting this property, you must set the [MFPKEY\_WMAAECMA\_FEATURE\_MODE](mfpkey-wmaaecma-feature-modeproperty.md) property to VARIANT\_TRUE.

The DSP uses this property only when microphone array processing is enabled.

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

 

 
