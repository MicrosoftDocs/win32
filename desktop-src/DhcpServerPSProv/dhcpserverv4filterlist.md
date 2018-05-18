---
title: DhcpServerv4FilterList class
description: Dhcp Server v4 Filter List.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9946013d-3396-4470-b23c-870fefe646d1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4FilterList class", "DhcpServerv4FilterList class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4FilterList
- DhcpServerv4FilterList.Allow
- DhcpServerv4FilterList.Deny
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4FilterList class

Dhcp Server v4 Filter List.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4FilterList
{
  boolean Allow;
  boolean Deny;
};
```

## Members

The **DhcpServerv4FilterList** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4FilterList** class has these properties.

<dl> <dt>

**Allow**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicate status of the Allow List on Dhcp Server.

</dd> <dt>

**Deny**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicate status of the Deny List on Dhcp Server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





