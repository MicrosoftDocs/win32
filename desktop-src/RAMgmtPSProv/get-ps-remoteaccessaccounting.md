---
title: Get method of the PS\_RemoteAccessAccounting class
description: This cmdlet displays the accounting configuration for Remote Access, viz. the different types of accounting that are enabled and their respective configuration.
audience: developer
ms.assetid: 382be70a-6b1c-4f94-8d52-7441cbe1525f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_RemoteAccessAccounting class
- PS_RemoteAccessAccounting class, Get method
topic_type:
- apiref
api_name:
- PS_RemoteAccessAccounting.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_RemoteAccessAccounting class

This cmdlet displays the accounting configuration for Remote Access, viz. the different types of accounting that are enabled and their respective configuration.

## Syntax


```mof
uint32 Get(
  [in]  string                 ComputerName,
  [out] RemoteAccessAccounting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Status of inbox accounting (enable or disable) 2. Inbox accounting store settings - these are displayed even if inbox accounting is disabled. a. Accounting store limit (in months) b. Time stamp of the first record in the store (includes date and time). c. Time stamp of the last record in the store (includes date and time). d. Used space in the store in bytes e. Used space in the store in percentage. f. Free space in the store in bytes g. Free space in the store in percentage. 3. Status of RADIUS accounting (disable, External Radius, Windows or Local Nps) - Windows indicates Windows Accounting. 4. RADIUS server list - If external RADIUS accounting is being used then the list of accounting servers is displayed by IPv4/IPv6 address or hostname . If external RADIUS accounting is not enabled then nothing is displayed.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessAccounting**](ps-remoteaccessaccounting.md)
</dt> </dl>

 

 





