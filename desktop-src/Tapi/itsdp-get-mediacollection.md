---
description: The get\_MediaCollection method gets a pointer to the ITMediaCollection interface for the conference.
ms.assetid: 8109582a-74f0-47e8-91d1-0d89c3d3c331
title: ITSdp::get_MediaCollection method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::get\_MediaCollection method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_MediaCollection** method gets a pointer to the [**ITMediaCollection**](itmediacollection.md) interface for the conference.

## Syntax


```C++
HRESULT get_MediaCollection(
  [out] ITMediaCollection **ppMediaCollection
);
```



## Parameters

<dl> <dt>

*ppMediaCollection* \[out\]
</dt> <dd>

Pointer to [**ITMediaCollection**](itmediacollection.md).

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                                                           | Meaning                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                            | Method succeeded.<br/>                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                                    | The *ppMediaCollection* parameter is not a valid pointer.<br/>                        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                                   | Insufficient memory exists to perform the operation.<br/>                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                          | Unspecified error.<br/>                                                               |
| <dl> <dt>**HRESULT\_FROM\_ERROR\_CODE(ERROR\_INVALID\_DATA)**</dt> </dl> | An internal error has occurred, usually due to the failure of a previous method.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                                       | This method is not yet implemented.<br/>                                              |



 

## Remarks

An [**ITMediaCollection**](itmediacollection.md) pointer could also be obtained using **QueryInterface**.

TAPI calls the **AddRef** method on the [**ITMediaCollection**](itmediacollection.md) interface returned by **ITSdp::get\_MediaCollection**. The application must call **Release** on the **ITMediaCollection** interface to free resources associated with it.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITSdp**](itsdp.md)
</dt> <dt>

[**ITMediaCollection**](itmediacollection.md)
</dt> </dl>

 

 




