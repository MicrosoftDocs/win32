---
title: INetFwV6Connection OpenPort method
description: The OpenPort method modifies the firewall configuration for a given connection to allow inbound connection attempts for the specified port and protocol pair.
ms.assetid: 725ef9a6-8c2e-47bb-a784-6a51915771c0
keywords:
- OpenPort method ICS/ICF
- OpenPort method ICS/ICF , INetFwV6Connection interface
- INetFwV6Connection interface ICS/ICF , OpenPort method
topic_type:
- apiref
api_name:
- INetFwV6Connection.OpenPort
api_location:
- Netfwv6.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetFwV6Connection::OpenPort method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **OpenPort** method modifies the firewall configuration for a given connection to allow inbound connection attempts for the specified port and protocol pair. It is not an error to call **OpenPort** for a port and protocol pair that is already open, even though such a call has no actual effect on the system.

This is a state-changing method, and is subject to the access control and confirmation UI mechanisms.

## Syntax


```C++
HRESULT OpenPort(
  [in] USHORT        usPort,
  [in] PORT_PROTOCOL Protocol,
  [in] BSTR          bstrName
);
```



## Parameters

<dl> <dt>

*usPort* \[in\]
</dt> <dd>

Specified in host byte order, and must be in the range 1   65535.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

Specifies a value defined in the [**PORT\_PROTOCOL**](port-protocol.md) enumeration.

</dd> <dt>

*bstrName* \[in\]
</dt> <dd>

Specifies the port name for information only. See Remarks section for further explanation.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One of the parameters is invalid.<br/>                  |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>      |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>             |



 

## Remarks

The *bstrName* parameter is for information purposes only, and has no bearing on the operation of the system. Different connections are not required to have the same name for identical port and protocol pairs. Calling **OpenPort** for a port and protocol pair that is already open using a different name does not alter the persisted name.

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

 

 





