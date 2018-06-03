---
Description: Specifies whether the Voice Capture DSP performs noise suppression.
ms.assetid: d63e9ac1-9584-4f74-8404-c95d17eb8c2d
title: MFPKEY\_WMAAECMA\_FEATR\_NS Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_NS Property

Specifies whether the Voice Capture DSP performs noise suppression.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/windows/desktop/e995aaa1-d4c9-475f-b1fa-b9123cd5b653).

## Data Type

VT\_I4

## Default Value

1

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

Noise suppression is a digital signal processing (DSP) component that suppresses or reduces stationary background noise in the audio signal. Noise suppression is applied after the acoustic echo cancellation (AEC) and microphone array processing.

This property can have the following values.



| Value | Description                |
|-------|----------------------------|
| 0     | Disable noise suppression. |
| 1     | Enable noise suppression.  |



 

The default value of this property is 1 (enabled). Before setting this property, you must set the [MFPKEY\_WMAAECMA\_FEATURE\_MODE](mfpkey-wmaaecma-feature-modeproperty.md) property to VARIANT\_TRUE.

## Requirements



|                                     |                                                                                         |
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

 

 




