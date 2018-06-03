---
title: INetFwV6Mgr CloseGlobalPort method
description: The CloseGlobalPort method modifies the global firewall configuration to disallow inbound connection attempts for the specified port and protocol.
ms.assetid: 8b899fec-a111-4937-a7be-0f35b7d4b79c
keywords:
- CloseGlobalPort method ICS/ICF
- CloseGlobalPort method ICS/ICF , INetFwV6Mgr interface
- INetFwV6Mgr interface ICS/ICF , CloseGlobalPort method
topic_type:
- apiref
api_name:
- INetFwV6Mgr.CloseGlobalPort
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

# INetFwV6Mgr::CloseGlobalPort method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The [**CloseGlobalPort**](inetfwv6mgr-openglobalport.md) method modifies the global firewall configuration to disallow inbound connection attempts for the specified port and protocol.

## Syntax


```C++
HRESULT CloseGlobalPort(
  [in] USHORT        usPort,
  [in] PORT_PROTOCOL Protocol
);
```



## Parameters

<dl> <dt>

*usPort* \[in\]
</dt> <dd>

Defines port ID, in host byte order. Must be in the range 1   65535.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

Defines protocol type.

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

It is not an error to call [**CloseGlobalPort**](inetfwv6mgr-openglobalport.md) for a port and protocol pair that is already closed, (for example, a pair for which [**IsPortGloballyOpen**](inetfwv6mgr-isportgloballyopen.md) returns VARIANT\_FALSE), even though such a call has no actual effect on the system.

Calling [**CloseGlobalPort**](inetfwv6mgr-openglobalport.md) does not guarantee that inbound connection attempts are denied for the specified port and protocol as there can exist connections for which that port and protocol has been explicitly opened.

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

[**INetFwV6Mgr**](inetfwv6mgr.md)
</dt> </dl>

 

 





