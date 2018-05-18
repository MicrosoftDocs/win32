---
title: DhcpServerv4IPRecords class
description: Dhcp Server v4 IPRecords class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0d2b37cb-be11-4304-b6c7-13c532514d19'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4IPRecords class", "DhcpServerv4IPRecords class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4IPRecords
- DhcpServerv4IPRecords.ScopeId
- DhcpServerv4IPRecords.IPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4IPRecords class

Dhcp Server v4 IPRecords class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4IPRecords
{
  String ScopeId;
  String IPAddress[];
};
```

## Members

The **DhcpServerv4IPRecords** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4IPRecords** class has these properties.

<dl> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

IP address record which is inconsistent.

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope identifier.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





