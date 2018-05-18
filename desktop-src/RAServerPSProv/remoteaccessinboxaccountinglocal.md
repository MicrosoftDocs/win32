---
title: RemoteAccessInboxAccountingLocal class
description: Remote Access Inbox Accounting Configuration Record.
audience: developer
ms.assetid: '6d576e5a-5463-40f7-abff-f2af82e9b369'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessInboxAccountingLocal class", "RemoteAccessInboxAccountingLocal class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessInboxAccountingLocal
- RemoteAccessInboxAccountingLocal.AccountingStatus
- RemoteAccessInboxAccountingLocal.StoreLimit
- RemoteAccessInboxAccountingLocal.StoreLimitUnits
- RemoteAccessInboxAccountingLocal.StoreUsedBytes
- RemoteAccessInboxAccountingLocal.StoreFreeBytes
- RemoteAccessInboxAccountingLocal.StoreFirstRecordDate
- RemoteAccessInboxAccountingLocal.StoreLastRecordDate
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessInboxAccountingLocal class

Remote Access Inbox Accounting Configuration Record.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class RemoteAccessInboxAccountingLocal
{
  boolean  AccountingStatus;
  uint32   StoreLimit;
  uint32   StoreLimitUnits;
  uint64   StoreUsedBytes;
  uint64   StoreFreeBytes;
  datetime StoreFirstRecordDate;
  datetime StoreLastRecordDate;
};
```

## Members

The **RemoteAccessInboxAccountingLocal** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessInboxAccountingLocal** class has these properties.

<dl> <dt>

**AccountingStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Inbox Accounting Status. True/False indicates Enabled/Disabled

</dd> <dt>

**StoreFirstRecordDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp of first record in Store

</dd> <dt>

**StoreFreeBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free Space in the store in bytes

</dd> <dt>

**StoreLastRecordDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp of last record in Store

</dd> <dt>

**StoreLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Accounting Store Limit

</dd> <dt>

**StoreLimitUnits**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Accounting Store Limit Units

</dd> <dt>

**StoreUsedBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used Space in the store in bytes

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





