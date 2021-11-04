---
description: The BufferCB method is a callback method that receives a pointer to the sample buffer.
ms.assetid: 9ee16dd6-8d05-4a9a-84c3-1b3bb95eaa04
title: ISampleGrabberCB::BufferCB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabberCB.BufferCB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISampleGrabberCB::BufferCB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **BufferCB** method is a callback method that receives a pointer to the sample buffer.

## Syntax


```C++
HRESULT BufferCB(
   double SampleTime,
   BYTE   *pBuffer,
   long   BufferLen
);
```



## Parameters

<dl> <dt>

*SampleTime* 
</dt> <dd>

Starting time of the sample, in seconds.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer that contains the sample data. The format of the data depends on the media type of the Sample Grabber's input pin. To get the media type, call [**ISampleGrabber::GetConnectedMediaType**](isamplegrabber-getconnectedmediatype.md).

</dd> <dt>

*BufferLen* 
</dt> <dd>

Length of the buffer pointed to by *pBuffer*, in bytes.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an **HRESULT** error code otherwise.

## Remarks

This callback method receives a pointer to the data in the most recent media sample.

> [!Note]  
> This method receives a pointer to the original sample data, not a copy. The original documentation incorrectly stated that *pBuffer* contains a copy of the data.

 

To set up the callback, call [**ISampleGrabber::SetCallback**](isamplegrabber-setcallback.md).

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

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**ISampleGrabberCB Interface**](isamplegrabbercb.md)
</dt> </dl>

 

 




