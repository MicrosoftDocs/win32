---
description: The GetCurrentBuffer method retrieves a copy of the buffer associated with the most recent sample.
ms.assetid: 08550c82-4711-4725-9cd0-19b43cf4c92e
title: ISampleGrabber::GetCurrentBuffer method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabber.GetCurrentBuffer
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISampleGrabber::GetCurrentBuffer method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **GetCurrentBuffer** method retrieves a copy of the buffer associated with the most recent sample.

## Syntax


```C++
HRESULT GetCurrentBuffer(
  [in, out] long *pBufferSize,
  [out]     long *pBuffer
);
```



## Parameters

<dl> <dt>

*pBufferSize* \[in, out\]
</dt> <dd>

Pointer to the size of the buffer. If *pBuffer* is **NULL**, this parameter receives the required buffer size, in bytes. If *pBuffer* is not **NULL**, set this parameter equal to the size of the buffer, in bytes. On output, the parameter receives the number of bytes that were copied into the buffer. This value might be smaller than the size of the buffer.

</dd> <dt>

*pBuffer* \[out\]
</dt> <dd>

Pointer to an array of bytes of size *pBufferSize*, or **NULL**. If this parameter is not **NULL**, the current buffer is copied into the array. If this parameter is **NULL**, the *pBufferSize* parameter receives the required buffer size.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                           | Description                                                                                                                  |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>          | Samples are not being buffered. Call [**ISampleGrabber::SetBufferSamples**](isamplegrabber-setbuffersamples.md).<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>         | The specified buffer is not large enough.<br/>                                                                         |
| <dl> <dt>**E\_POINTER**</dt> </dl>             | **NULL** pointer argument.<br/>                                                                                        |
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                                                                                                          |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The filter is not connected.<br/>                                                                                      |
| <dl> <dt>**VFW\_E\_WRONG\_STATE**</dt> </dl>   | The filter has not received any samples yet. To deliver a sample, run or pause the graph.<br/>                         |



 

## Remarks

To activate buffering, call [**ISampleGrabber::SetBufferSamples**](isamplegrabber-setbuffersamples.md) with a value of **TRUE**.

Call this method twice. On the first call, set *pBuffer* to **NULL**. The size of the buffer is returned in *pBufferSize*. Then allocate an array and call the method again. On the second call, pass the size of the array in *pBufferSize*, and pass the address of the array in *pBuffer*. If the array is not large enough, the method returns E\_OUTOFMEMORY.

The *pBuffer* parameter is typed as a **long** pointer, but the contents of the buffer depend on the format of the data. Call [**ISampleGrabber::GetConnectedMediaType**](isamplegrabber-getconnectedmediatype.md) to get the media type of the format.

Do not call this method while the filter graph is running. While the filter graph is running, the Sample Grabber filter overwrites the contents of the buffer whenever it receives a new sample. The best way to use this method is to use "one-shot mode," which stops the graph after receiving the first sample. To set one-shot mode, call [**ISampleGrabber::SetOneShot**](isamplegrabber-setoneshot.md).

The filter does not buffer preroll samples, or samples in which the **dwStreamId** member of the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-am_sample2_properties) structure is anything other than AM\_STREAM\_MEDIA.

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

 

 




