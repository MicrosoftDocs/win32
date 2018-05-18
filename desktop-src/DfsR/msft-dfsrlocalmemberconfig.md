---
title: MSFT\_DfsrLocalMemberConfig class
description: This class is for replication group membership. An instance of this class is available for each replication group hosted on this computer. This class maps to the DFSR2-Member class in the Active Directory Domain Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd3b2f994-74fe-4550-b5ee-fbb5534a71e9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DfsrLocalMemberConfig class Distributed File System Replication", "MSFT_DfsrLocalMemberConfig class Distributed File System Replication , described"]
topic_type:
- apiref
api_name:
- MSFT_DfsrLocalMemberConfig
- MSFT_DfsrLocalMemberConfig.MemberGuid
- MSFT_DfsrLocalMemberConfig.MemberName
- MSFT_DfsrLocalMemberConfig.MemberDn
- MSFT_DfsrLocalMemberConfig.MemberDns
- MSFT_DfsrLocalMemberConfig.MemberPeerNetGroupName
- MSFT_DfsrLocalMemberConfig.ReplicationGroupGuid
- MSFT_DfsrLocalMemberConfig.Keywords
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
---

# MSFT\_DfsrLocalMemberConfig class

This class is for replication group membership. An instance of this class is available for each replication group hosted on this computer. This class maps to the DFSR2-Member class in the Active Directory Domain Services.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrLocalMemberConfig
{
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

The **MSFT\_DfsrLocalMemberConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrLocalMemberConfig** class has these properties.

<dl> <dt>

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

The distinguished name of the corresponding [**ms-DFSR-Member**](https://msdn.microsoft.com/library/ms682403) object in the Active Directory Domain Services.

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

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID")
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

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The unique replication group identifier.

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

 

 





