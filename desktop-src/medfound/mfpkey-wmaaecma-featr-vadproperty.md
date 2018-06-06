---
Description: Specifies the type of voice activity detection that the Voice Capture DSP performs.
ms.assetid: 59c8e348-8c08-4cf8-9c72-8d0f4fabc473
title: MFPKEY\_WMAAECMA\_FEATR\_VAD Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_FEATR\_VAD Property

Specifies the type of voice activity detection that the Voice Capture DSP performs.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/e995aaa1-d4c9-475f-b1fa-b9123cd5b653).

## Data Type

VT\_I4

## Default Value

0

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

The value of this property is a member of the [AEC\_VAD\_MODE](/windows/desktop/api/wmcodecdsp/ne-wmcodecdsp-aec_vad_mode) enumeration. The output from voice activity detection is a number from 0 to 3, calculated for each audio frame. The DSP encodes the result in the lowest bit of the first two audio samples in each audio frame. The meaning of the value depends on the specified mode.

The following code shows how to extract the results from the audio data. In this example, *pOutput* is a pointer to the start of an audio frame in the output data.


```
int AecDecodeVAD(short *pOutput)
{
    int iVAD = (*pOutput) & 0x01;
    pOutput++;
    iVAD |= (*pOutput << 1) & 0x02;
    return iVAD;
}
```



The default value of this property is 0 (disabled). Before setting this property, you must set the [MFPKEY\_WMAAECMA\_FEATURE\_MODE](mfpkey-wmaaecma-feature-modeproperty.md) property to VARIANT\_TRUE.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




