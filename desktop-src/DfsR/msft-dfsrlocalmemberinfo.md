---
title: MSFT\_DfsrLocalMemberInfo class
description: This class provides statistical and operational information for each replication group member hosted on the local computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0e675fb7-d6c9-435a-8f77-a7b9cc108c98'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DfsrLocalMemberInfo class Distributed File System Replication", "MSFT_DfsrLocalMemberInfo class Distributed File System Replication , described"]
---

# MSFT\_DfsrLocalMemberInfo class

This class provides statistical and operational information for each replication group member hosted on the local computer.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrLocalMemberInfo
{
  string   MemberGuid;
  string   MemberName;
  string   ReplicationGroupGuid;
  string   ReplicationGroupName;
  uint8    State;
  datetime LastConfigChangeTime;
  uint32   LastErrorCode;
  uint32   LastErrorMessageId;
};
```

## Members

The **MSFT\_DfsrLocalMemberInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrLocalMemberInfo** class has these properties.

<dl> <dt>

**LastConfigChangeTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Configuration Change Time")
</dt> </dl>

The last time the configuration was changed.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Code")
</dt> </dl>

The last error code.

<dt>

<span id="DFSR_E_INVALID_CONFIG"></span><span id="dfsr_e_invalid_config"></span>

<span id="DFSR_E_INVALID_CONFIG"></span><span id="dfsr_e_invalid_config"></span>**DFSR\_E\_INVALID\_CONFIG**


</dt> <dd>

The replication group member configuration was inconsistent.

</dd> <dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>**Success** (0)


</dt> <dd>

TBD

</dd> </dl>

</dd> <dt>

**LastErrorMessageId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Message ID")
</dt> </dl>

The event log message identifier that corresponds to the last error code.

<dt>



 (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID")
</dt> </dl>

The local replication group member identifier.

</dd> <dt>

**MemberName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member Name")
</dt> </dl>

The member name. This is typically the unqualified DNS name of the local computer.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The unique replication group identifier.

</dd> <dt>

**ReplicationGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group Name")
</dt> </dl>

The friendly name of the replication group. This name is not required to be unique.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group State")
</dt> </dl>

The current replication group state of this member.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (0)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (1)


</dt> <dd></dd> <dt>

<span id="In_Error"></span><span id="in_error"></span><span id="IN_ERROR"></span>

**In Error** (2)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





