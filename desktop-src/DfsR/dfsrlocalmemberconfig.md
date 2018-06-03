---
title: DfsrLocalMemberConfig class
description: This class is for replication group membership. An instance of this class is available for each replication group hosted on this computer. This class maps to the DFSR2-Member class in the Active Directory Domain Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7af5f06b-4950-4308-aabc-7828c07a99cf
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrLocalMemberConfig class Distributed File System Replication
- DfsrLocalMemberConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrLocalMemberConfig
- DfsrLocalMemberConfig.Caption
- DfsrLocalMemberConfig.Description
- DfsrLocalMemberConfig.SettingID
- DfsrLocalMemberConfig.MemberGuid
- DfsrLocalMemberConfig.MemberName
- DfsrLocalMemberConfig.MemberDn
- DfsrLocalMemberConfig.MemberDns
- DfsrLocalMemberConfig.MemberPeerNetGroupName
- DfsrLocalMemberConfig.ReplicationGroupGuid
- DfsrLocalMemberConfig.Keywords
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DfsrLocalMemberConfig class

This class is for replication group membership. An instance of this class is available for each replication group hosted on this computer. This class maps to the DFSR2-Member class in the Active Directory Domain Services.

## Syntax

``` syntax
[Dynamic, Provider("DfsrConfigProv")]
class DfsrLocalMemberConfig : CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
  string MemberGuid;
  string MemberName;
  string MemberDn;
  string MemberDns;
  string MemberPeerNetGroupName;
  string ReplicationGroupGuid;
  string Keywords;
};
```

## Members

The **DfsrLocalMemberConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **DfsrLocalMemberConfig** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**Keywords**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Keywords")
</dt> </dl>

User-defined strings that are used by monitoring and configuration tools and for grouping or identification purposes.

</dd> <dt>

**MemberDn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member Distinguished Name")
</dt> </dl>

The distinguished name of the corresponding DFSR-Member object in the Active Directory Domain Services.

</dd> <dt>

**MemberDns**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member DNS")
</dt> </dl>

The member-qualified DNS name.

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique identifier of the local replication group member.

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

**MemberPeerNetGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member PeerNet Group Name")
</dt> </dl>

The member's PeerNet group name.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36)
</dt> </dl>

The unique replication group identifier.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                     |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





