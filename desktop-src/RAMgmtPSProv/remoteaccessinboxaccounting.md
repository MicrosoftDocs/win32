---
title: RemoteAccessInboxAccounting class
description: Remote Access Inbox Accounting Configuration Record.
audience: developer
ms.assetid: '628baac8-28bc-4e7b-be55-494d7978f049'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessInboxAccounting class", "RemoteAccessInboxAccounting class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessInboxAccounting
- RemoteAccessInboxAccounting.InboxAccountingStatus
- RemoteAccessInboxAccounting.StoreLimit
- RemoteAccessInboxAccounting.StoreUsedBytes
- RemoteAccessInboxAccounting.StoreUsedBytesInPercentage
- RemoteAccessInboxAccounting.StoreFreeBytes
- RemoteAccessInboxAccounting.StoreFreeBytesInPercentage
- RemoteAccessInboxAccounting.StoreFirstRecordDate
- RemoteAccessInboxAccounting.StoreLastRecordDate
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessInboxAccounting class

Remote Access Inbox Accounting Configuration Record

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessInboxAccounting
{
  string   InboxAccountingStatus;
  string   StoreLimit;
  uint64   StoreUsedBytes;
  real32   StoreUsedBytesInPercentage;
  uint64   StoreFreeBytes;
  real32   StoreFreeBytesInPercentage;
  datetime StoreFirstRecordDate;
  datetime StoreLastRecordDate;
};
```

## Members

The **RemoteAccessInboxAccounting** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessInboxAccounting** class has these properties.

<dl> <dt>

**InboxAccountingStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Inbox accounting status

The possible values are.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**StoreFirstRecordDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp of first record in the store

</dd> <dt>

**StoreFreeBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free space in the store in bytes

</dd> <dt>

**StoreFreeBytesInPercentage**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free space in the store as a percentage

</dd> <dt>

**StoreLastRecordDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp of last record in the store

</dd> <dt>

**StoreLimit**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Accounting store limit

</dd> <dt>

**StoreUsedBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used space in the store in bytes

</dd> <dt>

**StoreUsedBytesInPercentage**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used space in the store as a percentage

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





