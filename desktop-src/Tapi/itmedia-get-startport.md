---
description: The get\_StartPort method gets the 16-bit port value for the first port.
ms.assetid: 203b51ea-8e0c-47d2-b267-36a0bf3bff72
title: ITMedia::get_StartPort method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMedia::get\_StartPort method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_StartPort** method gets the 16-bit port value for the first port.

## Syntax


```C++
HRESULT get_StartPort(
  [out] LONG *pStartPort
);
```



## Parameters

<dl> <dt>

*pStartPort* \[out\]
</dt> <dd>

Value of the first port.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pStartPort* parameter is not a valid pointer.<br/>   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITMedia**](itmedia.md)
</dt> </dl>

 

 




