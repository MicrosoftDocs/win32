---
title: INetFwV6Connection EnumerateIgnoredGlobalPorts method
description: The EnumerateIgnoredGlobalPorts method yields the set of port and protocol pairs that ignore the global setting controlling inbound connection attempts.
ms.assetid: bb20db36-9f0b-4894-861b-7ad18fb5c0cd
keywords:
- EnumerateIgnoredGlobalPorts method ICS/ICF
- EnumerateIgnoredGlobalPorts method ICS/ICF , INetFwV6Connection interface
- INetFwV6Connection interface ICS/ICF , EnumerateIgnoredGlobalPorts method
topic_type:
- apiref
api_name:
- INetFwV6Connection.EnumerateIgnoredGlobalPorts
api_location:
- Netfwv6.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetFwV6Connection::EnumerateIgnoredGlobalPorts method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **EnumerateIgnoredGlobalPorts** method yields the set of port and protocol pairs that ignore the global setting controlling inbound connection attempts.

## Syntax


```C++
HRESULT EnumerateIgnoredGlobalPorts(
  [out] IEnumNetFwV6Ports **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* \[out\]
</dt> <dd>

Pointer to a collection of ignored global ports.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was stopped.<br/>                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The parameter is not valid.<br/>                       |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method is unable to allocate required memory.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>     |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>            |



 

## Remarks

A port that is ignored after this method call is not a member of the set. Likewise, a port that is set to observe the global setting after this method call is also not a member of the set.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[**INetFwV6Connection**](inetfwv6connection.md)
</dt> </dl>

 

 





