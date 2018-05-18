---
title: DhcpServerv6ExclusionRange class
description: Dhcp Server v6 Exclusion Range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6d570046-fde4-4ebd-af08-41706d0df80f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv6ExclusionRange class", "DhcpServerv6ExclusionRange class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv6ExclusionRange
- DhcpServerv6ExclusionRange.Prefix
- DhcpServerv6ExclusionRange.StartRange
- DhcpServerv6ExclusionRange.EndRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv6ExclusionRange class

Dhcp Server v6 Exclusion Range.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6ExclusionRange
{
  string Prefix;
  string StartRange;
  string EndRange;
};
```

## Members

The **DhcpServerv6ExclusionRange** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6ExclusionRange** class has these properties.

<dl> <dt>

**EndRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

End point or last address of Exclusion Range(IPRange from which IPAddress can't be leased out) for given scope on Dhcp server

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifier of given scope on Dhcp server

</dd> <dt>

**StartRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Starting point or first address of Exclusion Range(IPRange from which IPAddress can't be leased out) for given scope on Dhcp server

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





