---
description: The get\_SubStreamFromParticipant method allows an application to discover which substreams are associated with a given participant.
ms.assetid: d45cdd1d-13cf-433a-9b19-193d5c0cba11
title: ITParticipantSubStreamControl::get_SubStreamFromParticipant method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantSubStreamControl::get\_SubStreamFromParticipant method

\[**get\_SubStreamFromParticipant** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_SubStreamFromParticipant** method allows an application to discover which substreams are associated with a given participant.

## Syntax


```C++
HRESULT get_SubStreamFromParticipant(
  [in]  ITParticipant *pParticipant,
  [out] ITSubStream   **ppITSubStream
);
```



## Parameters

<dl> <dt>

*pParticipant* \[in\]
</dt> <dd>

Pointer to [**ITParticipant**](itparticipant.md) interface.

</dd> <dt>

*ppITSubStream* \[out\]
</dt> <dd>

Pointer to array of [**ITParticipant**](itparticipant.md) interface pointers.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                                 |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppITSubStream* parameter is not a valid pointer.<br/>             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pParticipant* parameter does not point to a valid interface.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The stream's participant information could not be accessed.<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>              |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITParticipantSubStreamControl**](itparticipantsubstreamcontrol.md)
</dt> <dt>

[**ITParticipant**](itparticipant.md)
</dt> <dt>

[**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream)
</dt> </dl>

 

