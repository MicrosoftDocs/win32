---
title: INetFwV6Mgr OpenGlobalPort method
description: The OpenGlobalPort method modifies the global firewall configuration.
ms.assetid: 'ee020fc3-9158-484f-afb3-9d247d14f4e3'
keywords: ["OpenGlobalPort method ICS/ICF", "OpenGlobalPort method ICS/ICF , INetFwV6Mgr interface", "INetFwV6Mgr interface ICS/ICF , OpenGlobalPort method"]
topic_type:
- apiref
api_name:
- INetFwV6Mgr.OpenGlobalPort
api_location:
- Netfwv6.dll
api_type:
- COM
---

# INetFwV6Mgr::OpenGlobalPort method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **OpenGlobalPort** method modifies the global firewall configuration. This allows inbound connection attempts for the specified port and protocol on all connections, with the exception of those connections that have been configured to ignore the port and protocol.

## Syntax


```C++
HRESULT OpenGlobalPort(
  [in] USHORT        usPort,
  [in] PORT_PROTOCOL Protocol,
  [in] BSTR          bstrName
);
```



## Parameters

<dl> <dt>

*usPort* \[in\]
</dt> <dd>

Defines port ID, in host byte order. Must be in the range 1 – 65535.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

Defines protocol type.

</dd> <dt>

*bstrName* \[in\]
</dt> <dd>

Display name for the port. For information purposes only.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The parameter is invalid.<br/>                         |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method is unable to allocate required memory.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>            |



 

## Remarks

It is not an error to call **OpenGlobalPort** for a port and protocol pair that is already open, (for example, a pair for which [**IsPortGloballyOpen**](inetfwv6mgr-isportgloballyopen.md) returns VARIANT\_TRUE), even though such a call has no actual effect on the system.

The *bstrName* parameter is for information purposes only, and has no bearing on the operation of the system. Different connections are not required to have the same name for identical port and protocol pairs. Calling **OpenGlobalPort** for a port and protocol pair that is already open using a different name does not alter the persisted name.

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

[**INetFwV6Mgr**](inetfwv6mgr.md)
</dt> </dl>

 

 





