---
Description: Specifies whether the Voice Capture DSP uses source mode or filter mode.
ms.assetid: d1d3beba-678c-48fd-ad12-45e0418e1236
title: MFPKEY\_WMAAECMA\_DMO\_SOURCE\_MODE Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_DMO\_SOURCE\_MODE Property

Specifies whether the Voice Capture DSP uses source mode or filter mode.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/windows/desktop/e995aaa1-d4c9-475f-b1fa-b9123cd5b653).

## Data Type

VT\_BOOL

## Default Value

VARIANT\_TRUE

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

In source mode, the application does not need to send input data to the DSP, because the DSP automatically pulls data from the audio devices. In filter mode, the application must send the input data to the DSP.

This property can have the following values.



| Value          | Description  |
|----------------|--------------|
| VARIANT\_FALSE | Filter mode. |
| VARIANT\_TRUE  | Source mode. |



 

> [!Note]  
> When the DMO is in source mode, you should only call [**IMediaObject::SetOutputType**](https://msdn.microsoft.com/windows/desktop/1dda3c55-d37b-4e04-9509-0e5197d6b019) to set output stream format, and do not call [**IMediaObject::SetInputType**](https://msdn.microsoft.com/windows/desktop/6b466fe4-97a0-46f9-9e4b-461ee66095f1) to set input stream formats. Otherwise DMO initialization will fail.

 

If the value of this property is VARIANT\_TRUE, the DSP has zero inputs. If the value is VARIANT\_FALSE, the DSP has one or two inputs, depending on the value of the [MFPKEY\_WMAAECMA\_SYSTEM\_MODE](mfpkey-wmaaecma-system-modeproperty.md) property, as shown in the following table.



| Value                     | Number of inputs |
|---------------------------|------------------|
| OPTIBEAM\_ARRAY\_AND\_AEC | 2                |
| OPTIBEAM\_ARRAY\_ONLY     | 1                |
| SINGLE\_CHANNEL\_AEC      | 2                |
| SINGLE\_CHANNEL\_NSAGC    | 1                |



 

> [!Note]  
> Only modes with a single input will work with the wrapper filter DMO from the DirectShow 9.0 API.

 

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

 

 




