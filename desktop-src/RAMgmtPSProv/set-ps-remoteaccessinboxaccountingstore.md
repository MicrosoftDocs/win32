---
title: Set method of the PS\_RemoteAccessInboxAccountingStore class
description: This cmdlet modifies the size of the inbox accounting store.
audience: developer
ms.assetid: '1a97e804-8798-4f78-896e-446b60277f39'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_RemoteAccessInboxAccountingStore class", "PS_RemoteAccessInboxAccountingStore class, Set method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessInboxAccountingStore.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_RemoteAccessInboxAccountingStore class

This cmdlet modifies the size of the inbox accounting store.

## Syntax


```mof
uint32 Set(
  [in]  string                      StoreLimit,
  [in]  string                      ComputerName,
  [in]  boolean                     PassThru,
  [out] RemoteAccessInboxAccounting cmdletOutput
);
```



## Parameters

<dl> <dt>

*StoreLimit* \[in\]
</dt> <dd>

Indicates the limit on the amount of accounting data that can be stored, essentially the size of the store, in terms of time. Following is the format used: \[duration\]\[time unit\]. Time unit can be day, week, month or year specified using the characters 'd', 'w', 'm', 'y'. For e,g, 100d means 100 days, 3m means 3 months, 2y means 2 years.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. When ComputerName is specified the size limit of the store residing on that Remote Access server is modified

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the inbox accounting store object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

New value of store limit

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessInboxAccountingStore**](ps-remoteaccessinboxaccountingstore.md)
</dt> </dl>

 

 





