---
title: DhcpServerv4MulticastExclusionRange class
description: Dhcp Server v4 Multicast Exclusion Range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '858fa9e2-3582-4468-8ab0-8cc545e01238'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4MulticastExclusionRange class", "DhcpServerv4MulticastExclusionRange class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4MulticastExclusionRange
- DhcpServerv4MulticastExclusionRange.Name
- DhcpServerv4MulticastExclusionRange.StartRange
- DhcpServerv4MulticastExclusionRange.EndRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4MulticastExclusionRange class

Dhcp Server v4 Multicast Exclusion Range

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4MulticastExclusionRange
{
  string Name;
  string StartRange;
  string EndRange;
};
```

## Members

The **DhcpServerv4MulticastExclusionRange** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4MulticastExclusionRange** class has these properties.

<dl> <dt>

**EndRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Ending IP address in exclusion range, string formatted as an IPv4 Address.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the multicast scope.

</dd> <dt>

**StartRange**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Starting IP address in exclusion range, string formatted as an IPv4 Address.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





