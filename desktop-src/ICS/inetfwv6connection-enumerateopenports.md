---
title: INetFwV6Connection EnumerateOpenPorts method
description: The EnumerateOpenPorts method returns an enumerator that yields the set of port and protocol pairs for which inbound connection attempts are currently allowed at the time of the method call.
ms.assetid: '7cc78098-5070-4138-80c9-e4ff72e3bf49'
keywords: ["EnumerateOpenPorts method ICS/ICF", "EnumerateOpenPorts method ICS/ICF , INetFwV6Connection interface", "INetFwV6Connection interface ICS/ICF , EnumerateOpenPorts method"]
topic_type:
- apiref
api_name:
- INetFwV6Connection.EnumerateOpenPorts
api_location:
- Netfwv6.dll
api_type:
- COM
---

# INetFwV6Connection::EnumerateOpenPorts method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **EnumerateOpenPorts** method returns an enumerator that yields the set of port and protocol pairs for which inbound connection attempts are currently allowed at the time of the method call.

## Syntax


```C++
HRESULT EnumerateOpenPorts(
  [out] IEnumNetFwV6OpenPorts **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* \[out\]
</dt> <dd>

Pointer to a collection of open ports.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The parameter is invalid.<br/>                          |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>      |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>             |



 

## Remarks

A port that is opened after this method call is made is not a member of the set. Likewise, a port that is closed after this method call is made is a member of the set.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumNetFwV6OpenPorts**](ienumnetfwv6openports.md)
</dt> <dt>

[**INetFwV6Connection**](inetfwv6connection.md)
</dt> </dl>

 

 





