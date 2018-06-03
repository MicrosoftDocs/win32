---
title: Set method of the PS\_RemoteAccessInboxAccountingLocal class
description: Set the status for Inbox accounting.
audience: developer
ms.assetid: 6ed496ce-c8bb-4c59-b881-5b9586b73abc
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_RemoteAccessInboxAccountingLocal class
- PS_RemoteAccessInboxAccountingLocal class, Set method
topic_type:
- apiref
api_name:
- PS_RemoteAccessInboxAccountingLocal.Set
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_RemoteAccessInboxAccountingLocal class

Set the status for Inbox accounting.

## Syntax


```mof
uint32 Set(
  [in]  uint8                            AccountingStatus,
  [in]  string                           StoreLimit,
  [out] RemoteAccessInboxAccountingLocal cmdletOutput
);
```



## Parameters

<dl> <dt>

*AccountingStatus* \[in\]
</dt> <dd>

The status of the Inbox accounting.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (0)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (1)


</dt> <dd></dd> </dl> </dd> <dt>

*StoreLimit* \[in\]
</dt> <dd>

The Inbox Accounting Store Limit

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains a [**RemoteAccessInboxAccountingLocal**](ps-remoteaccessinboxaccountinglocal.md) describing the entire Inbox Accounting Configuration.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessInboxAccountingLocal**](ps-remoteaccessinboxaccountinglocal.md)
</dt> </dl>

 

 





