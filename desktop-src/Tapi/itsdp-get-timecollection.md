---
description: The get\_TimeCollection method gets a pointer to an ITTimeCollection interface for conference.
ms.assetid: 1cfe3f5a-dcf7-480b-9b23-e17259d8ee9c
title: ITSdp::get_TimeCollection method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITSdp::get\_TimeCollection method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_TimeCollection** method gets a pointer to an [**ITTimeCollection**](ittimecollection.md) interface for conference.

## Syntax


```C++
HRESULT get_TimeCollection(
  [out] ITTimeCollection **ppTimeCollection
);
```



## Parameters

<dl> <dt>

*ppTimeCollection* \[out\]
</dt> <dd>

Pointer to [**ITTimeCollection**](ittimecollection.md).

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                                                           | Meaning                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                            | Method succeeded.<br/>                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                                    | The *ppTimeCollection* parameter is not a valid pointer.<br/>                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                                   | Insufficient memory exists to perform the operation.<br/>                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                          | Unspecified error.<br/>                                                               |
| <dl> <dt>**HRESULT\_FROM\_ERROR\_CODE(ERROR\_INVALID\_DATA)**</dt> </dl> | An internal error has occurred, usually due to the failure of a previous method.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                                       | This method is not yet implemented.<br/>                                              |



 

## Remarks

An [**ITTimeCollection**](ittimecollection.md) pointer could also be obtained using **QueryInterface**.

TAPI calls the **AddRef** method on the [**ITTimeCollection**](ittimecollection.md) interface returned by **ITSdp::get\_TimeCollection**. The application must call **Release** on the **ITTimeCollection** interface to free resources associated with it.

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

[**ITTimeCollection**](ittimecollection.md)
</dt> </dl>

 

 




