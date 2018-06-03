---
title: DhcpServerv4PolicyIPRange class
description: Dhcp Server v4Policy IPRange.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dabd1545-2442-49e1-8f8e-47b93f839928
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4PolicyIPRange class
- DhcpServerv4PolicyIPRange class, described
topic_type:
- apiref
api_name:
- DhcpServerv4PolicyIPRange
- DhcpServerv4PolicyIPRange.Name
- DhcpServerv4PolicyIPRange.ScopeId
- DhcpServerv4PolicyIPRange.StartRange
- DhcpServerv4PolicyIPRange.EndRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4PolicyIPRange class

Dhcp Server v4Policy IPRange.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4PolicyIPRange
{
  string Name;
  string ScopeId;
  string StartRange;
  string EndRange;
};
```

## Members

The **DhcpServerv4PolicyIPRange** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4PolicyIPRange** class has these properties.

<dl> <dt>

**EndRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

End of Policy IP range

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Unique name for the Policy

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Scope for which the Policy exists.

</dd> <dt>

**StartRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Start of Policy IP range

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





