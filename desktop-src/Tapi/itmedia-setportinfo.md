---
description: The SetPortInfo method sets the 16-bit port value for the first port and the number of ports needed for a session.
ms.assetid: 4726b39b-cd10-4630-8f38-8671db4f432b
title: ITMedia::SetPortInfo method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMedia::SetPortInfo method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SetPortInfo** method sets the 16-bit port value for the first port and the number of ports needed for a session.

## Syntax


```C++
HRESULT SetPortInfo(
  [in] LONG StartPort,
  [in] LONG NumPorts
);
```



## Parameters

<dl> <dt>

*StartPort* \[in\]
</dt> <dd>

Starting port. This can be a value in the range 0-65535.

</dd> <dt>

*NumPorts* \[in\]
</dt> <dd>

Number of ports. This can be a value in the range 0-65535.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *StartPort or NumPorts* parameter is not valid.<br/>  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

This function may send data over the wire in unencrypted form; therefore, someone eavesdropping on the network may be able to read the data. The security risk of sending the data in clear text should be considered before using this method.

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

 

 




