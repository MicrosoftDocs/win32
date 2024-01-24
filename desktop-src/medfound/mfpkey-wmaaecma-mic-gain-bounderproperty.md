---
description: Specifies whether the Voice Capture DSP applies microphone gain bounding.
ms.assetid: b9f0bcc7-57ab-4339-bf1d-2b12c8744f01
title: MFPKEY_WMAAECMA_MIC_GAIN_BOUNDER Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_MIC\_GAIN\_BOUNDER Property

Specifies whether the Voice Capture DSP applies microphone gain bounding.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_TRUE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Microphone gain bounding ensures that the microphone has the correct level of gain. If gain is too high, the captured signal might be saturated and will be clipped. Clipping is a non-linear effect, which will cause the acoustic echo cancellation (AEC) algorithm to fail. If the gain is too low, the signal-to-noise ratio is low, which can also cause the AEC algorithm to fail or not perform well.

This property can have the following values.



| Value          | Description                       |
|----------------|-----------------------------------|
| VARIANT\_TRUE  | Enable microphone gain bounding.  |
| VARIANT\_FALSE | Disable microphone gain bounding. |



 

The default value of this property is VARIANT\_TRUE (enabled).

Microphone gain bounding is applies only when the DSP operates in source mode. In filter mode, the application must ensure that the microphone has the correct gain level.

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

 

 
