---
title: CleanInboxAccountingStore method of the PS\_RemoteAccessInboxAccountingLocal class
description: Get the status for Inbox accounting store.
audience: developer
ms.assetid: 6d576e5a-5463-40f7-abff-f2af82e9b369
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CleanInboxAccountingStore method
- CleanInboxAccountingStore method, PS_RemoteAccessInboxAccountingLocal class
- PS_RemoteAccessInboxAccountingLocal class, CleanInboxAccountingStore method
topic_type:
- apiref
api_name:
- PS_RemoteAccessInboxAccountingLocal.CleanInboxAccountingStore
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CleanInboxAccountingStore method of the PS\_RemoteAccessInboxAccountingLocal class

Get the status for Inbox accounting store.

## Syntax


```mof
uint32 CleanInboxAccountingStore(
  [in]  datetime                         StartDateTime,
  [in]  datetime                         EndDateTime,
  [out] RemoteAccessInboxAccountingLocal cmdletOutput
);
```



## Parameters

<dl> <dt>

*StartDateTime* \[in\]
</dt> <dd>

The start date from when to cleanup the inbox accounting data.

</dd> <dt>

*EndDateTime* \[in\]
</dt> <dd>

The end date till when to cleanup the inbox accounting data.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**RemoteAccessInboxAccountingLocal**](ps-remoteaccessinboxaccountinglocal.md) containing the entire Inbox Accounting Configuration.

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

 

 





