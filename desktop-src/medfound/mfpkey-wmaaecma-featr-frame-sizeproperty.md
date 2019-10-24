---
Description: Specifies the audio frame size used by the Voice Capture DSP.
ms.assetid: b414ac34-c60a-4f43-924f-43431d6ba25f
title: MFPKEY_WMAAECMA_FEATR_FRAME_SIZE Property
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_FRAME\_SIZE Property

Specifies the audio frame size used by the Voice Capture DSP.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx).

## Data Type

VT\_I4

## Default Value

0

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

The acoustic echo cancellation (AEC) algorithm processes PCM audio samples one frame at a time. The value of this property is the size of the audio frame, in samples. Before setting this property, you must set the [MFPKEY\_WMAAECMA\_FEATURE\_MODE](mfpkey-wmaaecma-feature-modeproperty.md) property to VARIANT\_TRUE.

The Voice Capture DSP supports the following frame sizes:

-   80
-   128
-   160
-   240
-   256
-   320

If the value of this property is zero, the DSP selects the frame size based on the system mode and the output format.

For the best performance, however, it is recommended that applications use the default value. If the processing mode is microphone array only, the default value is 320 samples. For all other processing modes, the default value is 160 samples. For more information about the processing modes of the Voice Capture DSP, see [MFPKEY\_WMAAECMA\_SYSTEM\_MODE](mfpkey-wmaaecma-system-modeproperty.md).

After the first call to [**IMediaObject::AllocateStreamingResources**](https://msdn.microsoft.com/en-us/library/Dd406943(v=VS.85).aspx) or [**IMediaObject::ProcessOutput**](https://msdn.microsoft.com/en-us/library/Dd406960(v=VS.85).aspx), you can read this property to get the actual frame size in use, even when [**MFPKEY\_WMAAECMA\_FEATURE\_MODE**](mfpkey-wmaaecma-feature-modeproperty.md) is false.

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

 

 




