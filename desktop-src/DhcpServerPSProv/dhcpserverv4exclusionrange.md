---
title: DhcpServerv4ExclusionRange class
description: Dhcp Server v4 Exclusion Range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0be282ac-787d-4414-8017-c850258783b7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4ExclusionRange class", "DhcpServerv4ExclusionRange class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4ExclusionRange
- DhcpServerv4ExclusionRange.ScopeId
- DhcpServerv4ExclusionRange.StartRange
- DhcpServerv4ExclusionRange.EndRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4ExclusionRange class

Dhcp Server v4 Exclusion Range.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4ExclusionRange
{
  string ScopeId;
  string StartRange;
  string EndRange;
};
```

## Members

The **DhcpServerv4ExclusionRange** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4ExclusionRange** class has these properties.

<dl> <dt>

**EndRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

End point or last address of Exclusion Range (IPRange from which IPAddress can't be leased out) for a given scope on the Dhcp server.

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifier of a given scope on the Dhcp server.

</dd> <dt>

**StartRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Starting point or first address of Exclusion Range (IPRange from which IPAddress can't be leased out) for a given scope on the Dhcp server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





