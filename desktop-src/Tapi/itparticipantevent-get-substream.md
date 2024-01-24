---
description: The get\_SubStream gets a pointer to an array of ITSubStream interfaces representing the substreams involved in the event.
ms.assetid: 0af9097a-2481-4543-bb3d-35ccd352e992
title: ITParticipantEvent::get_SubStream method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantEvent::get\_SubStream method

\[**get\_SubStream** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_SubStream** gets a pointer to an array of [**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream) interfaces representing the substreams involved in the event.

## Syntax


```C++
HRESULT get_SubStream(
  [out] ITSubStream **ppSubStream
);
```



## Parameters

<dl> <dt>

*ppSubStream* \[out\]
</dt> <dd>

Pointer to array of [**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream) pointers.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                           | Meaning                                                         |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>            | Method succeeded.<br/>                                    |
| <dl> <dt>**TAPI\_E\_NOITEMS**</dt> </dl> | There are no substreams associated with the event.<br/>   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>   | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>       | The *ppSubStream* parameter is not a valid pointer.<br/>  |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITParticipantEvent**](itparticipantevent.md)
</dt> <dt>

[**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream)
</dt> </dl>

 

