---
description: The SetBufferSamples method specifies whether to copy sample data into a buffer as it goes through the filter.
ms.assetid: 1ef4508e-441f-45e0-afb4-239dd947284b
title: ISampleGrabber::SetBufferSamples method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabber.SetBufferSamples
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISampleGrabber::SetBufferSamples method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **SetBufferSamples** method specifies whether to copy sample data into a buffer as it goes through the filter.

## Syntax


```C++
void SetBufferSamples(
   BOOL BufferThem
);
```



## Parameters

<dl> <dt>

*BufferThem* 
</dt> <dd>

Boolean value specifying whether to buffer sample data. If **TRUE**, the filter copies sample data into an internal buffer.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To get the copied buffer, call [**ISampleGrabber::GetCurrentBuffer**](isamplegrabber-getcurrentbuffer.md).

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Using the Sample Grabber](using-the-sample-grabber.md)
</dt> <dt>

[**ISampleGrabber Interface**](isamplegrabber.md)
</dt> </dl>

 

 




