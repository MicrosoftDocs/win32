---
title: INetFwV6Mgr IsPortGloballyOpen method
description: The IsPortGloballyOpen method returns VARIANT\_TRUE if inbound connection attempts are allowed for the specified port and protocol (except on those connections that ignore the specified global port and protocol).
ms.assetid: b99e1e9e-ae2f-42cd-890b-e79ddb85d666
keywords:
- IsPortGloballyOpen method ICS/ICF
- IsPortGloballyOpen method ICS/ICF , INetFwV6Mgr interface
- INetFwV6Mgr interface ICS/ICF , IsPortGloballyOpen method
topic_type:
- apiref
api_name:
- INetFwV6Mgr.IsPortGloballyOpen
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

# INetFwV6Mgr::IsPortGloballyOpen method

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The [**IsPortGloballyOpen**](inetfwv6mgr-openglobalport.md) method returns VARIANT\_TRUE if inbound connection attempts are allowed for the specified port and protocol (except on those connections that ignore the specified global port and protocol).

## Syntax


```C++
HRESULT IsPortGloballyOpen(
  [in]  USHORT        usPort,
  [in]  PORT_PROTOCOL Protocol,
  [out] VARIANT_BOOL  *pvbPortIsOpen
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

</dd> <dt>

*pvbPortIsOpen* \[out\]
</dt> <dd>

Port status.

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

 

 





