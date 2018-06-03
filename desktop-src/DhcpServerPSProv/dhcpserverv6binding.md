---
title: DhcpServerv6Binding class
description: Dhcp Server v6 Binding.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 323cc0cc-3656-42cc-8bba-6d6a5cb5dfd8
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6Binding class
- DhcpServerv6Binding class, described
topic_type:
- apiref
api_name:
- DhcpServerv6Binding
- DhcpServerv6Binding.InterfaceAlias
- DhcpServerv6Binding.BindingState
- DhcpServerv6Binding.InterfaceGuid
- DhcpServerv6Binding.IPAddress
- DhcpServerv6Binding.InterfaceIndex
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv6Binding class

Dhcp Server v6 Binding.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6Binding
{
  string  InterfaceAlias;
  boolean BindingState;
  string  InterfaceGuid;
  string  IPAddress;
  uint32  InterfaceIndex;
};
```

## Members

The **DhcpServerv6Binding** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6Binding** class has these properties.

<dl> <dt>

**BindingState**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if Dhcp Server is bound to given interface.

</dd> <dt>

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of interface available to Dhcp server for binding.

</dd> <dt>

**InterfaceGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of interface available to Dhcp server for binding.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

index number of interface available to Dhcp server for binding.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPAddress of interface available to Dhcp server for binding.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





