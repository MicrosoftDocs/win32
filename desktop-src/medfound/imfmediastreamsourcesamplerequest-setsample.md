---
description: Sets the sample for the media stream source.
ms.assetid: a35c5e18-f307-4e40-bc92-f91aa9eb80ba
title: IMFMediaStreamSourceSampleRequest::SetSample method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFMediaStreamSourceSampleRequest.SetSample
api_type: 
- COM
api_location: 
- mfidl.h
---

# IMFMediaStreamSourceSampleRequest::SetSample method

Sets the sample for the media stream source.

## Syntax


```C++
HRESULT SetSample(
  [in] IMFSample *value
);
```



## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

The sample for the media stream source.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                       |
| IDL<br/>                      | <dl> <dt>Mfidl.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaStreamSourceSampleRequest**](imfmediastreamsourcesamplerequest.md)
</dt> </dl>

 

 




