---
title: INetFwV6Connection IgnoreGlobalPort method
description: The IgnoreGlobalPort method modifies the firewall configuration for a connection to ignore the global setting that permit connection attempts for the specified port and protocol.
ms.assetid: 1633d919-fc0a-40fc-b48a-9ab3e87a6bbb
keywords:
- IgnoreGlobalPort method ICS/ICF
- IgnoreGlobalPort method ICS/ICF , INetFwV6Connection interface
- INetFwV6Connection interface ICS/ICF , IgnoreGlobalPort method
topic_type:
- apiref
api_name:
- INetFwV6Connection.IgnoreGlobalPort
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

# INetFwV6Connection::IgnoreGlobalPort method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The [**IgnoreGlobalPort**](inetfwv6connection-closeport.md) method modifies the firewall configuration for a connection to ignore the global setting that permit connection attempts for the specified port and protocol.

## Syntax


```C++
HRESULT IgnoreGlobalPort(
  [in] USHORT        usPort,
  [in] PORT_PROTOCOL Protocol,
  [in] BSTR          bstrName
);
```



## Parameters

<dl> <dt>

*usPort* \[in\]
</dt> <dd>

Specifies the port ID in host byte order. Must be in the range 1   65535.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

Specifies the port protocol type as defined in the [**PORT\_PROTOCOL**](port-protocol.md) enumeration.

</dd> <dt>

*bstrName* \[in\]
</dt> <dd>

Specifies the port name for information only. See the Remarks section for further explanation.

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Return code                                                                                   | Description                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>       | The operation was aborted.<br/>                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | An unspecified error occurred.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One of the parameters is invalid.<br/>                 |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | A specified interface is not supported.<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | A specified method is not implemented.<br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The method is unable to allocate required memory.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | The method failed for unknown reasons.<br/>            |



 

## Remarks

It is not an error to call **IgnoreGlobalPort** for a port and protocol pair that is not ignored, (for example, a pair for which [**IsGlobalPortIgnored**](inetfwv6connection-isglobalportignored.md) returns VARIANT\_FALSE), even though such a call has no actual effect on the system.

The *bstrName* parameter is for information purposes only, and has no bearing on the operation of the system. Different connections are not required to have the same name for identical port and protocol pairs. Calling **IgnoreGlobalPort** for a port and protocol pair that is already open using a different name does not alter the persisted name.

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

 

 





