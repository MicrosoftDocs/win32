---
description: The get\_ParticipantFromSubStream method allows an application to discover which participants are associated with a given substream.
ms.assetid: 0e42b4f0-d5b6-4b33-b7e5-dc525524ece7
title: ITParticipantSubStreamControl::get_ParticipantFromSubStream method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantSubStreamControl::get\_ParticipantFromSubStream method

\[**get\_ParticipantFromSubStream** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_ParticipantFromSubStream** method allows an application to discover which participants are associated with a given substream.

## Syntax


```C++
HRESULT get_ParticipantFromSubStream(
  [in]  ITSubStream   *pITSubStream,
  [out] ITParticipant **ppParticipant
);
```



## Parameters

<dl> <dt>

*pITSubStream* \[in\]
</dt> <dd>

Pointer to [**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream) interface.

</dd> <dt>

*ppParticipant* \[out\]
</dt> <dd>

Pointer to array of [**ITParticipant**](itparticipant.md) interface pointers.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                     | Description                                                                        |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>            | Method succeeded.<br/>                                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>       | The *pITSubStream* or *ppParticipant* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>    | The *pITSubStream* parameter does not point to valid interface.<br/>         |
| <dl> <dt>**TAPI\_E\_NOITEMS**</dt> </dl> | There are no participants associated with the substream.<br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>   | Insufficient memory exists to perform the operation.<br/>                    |



 

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

 

