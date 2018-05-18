---
title: DhcpServerSetting class
description: Dhcp Server Settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f20fcc31-bd7b-4ceb-bd9c-cacc5be8f4cf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerSetting class", "DhcpServerSetting class, described"]
topic_type:
- apiref
api_name:
- DhcpServerSetting
- DhcpServerSetting.IsDomainJoined
- DhcpServerSetting.IsAuthorized
- DhcpServerSetting.DynamicBootp
- DhcpServerSetting.RestoreStatus
- DhcpServerSetting.NapEnabled
- DhcpServerSetting.ConflictDetectionAttempts
- DhcpServerSetting.NpsUnreachableAction
- DhcpServerSetting.ActivatePolicies
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerSetting class

Dhcp Server Settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerSetting
{
  boolean IsDomainJoined;
  boolean IsAuthorized;
  boolean DynamicBootp;
  boolean RestoreStatus;
  boolean NapEnabled;
  uint32  ConflictDetectionAttempts;
  string  NpsUnreachableAction;
  boolean ActivatePolicies;
};
```

## Members

The **DhcpServerSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerSetting** class has these properties.

<dl> <dt>

**ActivatePolicies**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if policy enforcement is enabled for entire server or not.

</dd> <dt>

**ConflictDetectionAttempts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of conflict detection attempts (1-5) DHCP server makes for an IP address. Conflict detection is disabled when this is set to zero. (v4 Only).

</dd> <dt>

**DynamicBootp**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if Dhcp Server support dynamic bootp clients.

</dd> <dt>

**IsAuthorized**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if Dhcp Server is authorized in Active Directory.

</dd> <dt>

**IsDomainJoined**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if Dhcp Server is part of domain.

</dd> <dt>

**NapEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if NAP is enabled on Dhcp Server (v4 only).

</dd> <dt>

**NpsUnreachableAction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

NPS Settings for Dhcp Server (v4 only).

<dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>

**Full** ("Full")


</dt> <dd></dd> <dt>

<span id="Restricted"></span><span id="restricted"></span><span id="RESTRICTED"></span>

**Restricted** ("Restricted")


</dt> <dd></dd> <dt>

<span id="NoAccess"></span><span id="noaccess"></span><span id="NOACCESS"></span>

**NoAccess** ("NoAccess")


</dt> <dd></dd> </dl>

</dd> <dt>

**RestoreStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the database was restored from backed up database at service start.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





