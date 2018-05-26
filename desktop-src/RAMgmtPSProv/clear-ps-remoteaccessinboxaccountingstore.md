---
title: Clear method of the PS\_RemoteAccessInboxAccountingStore class
description: This cmdlet clears the inbox accounting store for the specified time period.
audience: developer
ms.assetid: 22652f3f-b799-4877-83bc-38884a7c422c
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Clear method
- Clear method, PS_RemoteAccessInboxAccountingStore class
- PS_RemoteAccessInboxAccountingStore class, Clear method
topic_type:
- apiref
api_name:
- PS_RemoteAccessInboxAccountingStore.Clear
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Clear method of the PS\_RemoteAccessInboxAccountingStore class

This cmdlet clears the inbox accounting store for the specified time period.

## Syntax


```mof
uint32 Clear(
  [in]  string                      ComputerName,
  [in]  datetime                    StartDateTime,
  [in]  datetime                    EndDateTime,
  [in]  boolean                     Force,
  [in]  boolean                     PassThru,
  [out] RemoteAccessInboxAccounting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. When ComputerName is specified the store residing on that Remote Access server is cleared

</dd> <dt>

*StartDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which store should be emptied and indicates the start date. If no start date is specified then the time stamp of the first record entry in the accounting store is used by default

</dd> <dt>

*EndDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which store should be emptied and indicates the end date. When not specified the time stamp of the last record entry in the accounting store is used by default

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts shown to the user before clearing the store to warn him about the loss of data/information for the specified duration. When suppressed the cmdlet assumes user confirmation for the clearing of the store

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the object that represents the inbox accounting configuration. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The entire inbox accounting configuration.

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

[**PS\_RemoteAccessInboxAccountingStore**](ps-remoteaccessinboxaccountingstore.md)
</dt> </dl>

 

 





