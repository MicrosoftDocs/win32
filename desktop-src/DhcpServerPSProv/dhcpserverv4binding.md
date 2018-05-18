---
title: DhcpServerv4Binding class
description: Dhcp Server v4 Binding.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dae21291-c833-43e2-a97d-a4a23079fc55'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4Binding class", "DhcpServerv4Binding class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4Binding
- DhcpServerv4Binding.InterfaceAlias
- DhcpServerv4Binding.BindingState
- DhcpServerv4Binding.InterfaceGuid
- DhcpServerv4Binding.IPAddress
- DhcpServerv4Binding.SubnetMask
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4Binding class

Dhcp Server v4 Binding.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Binding
{
  string  InterfaceAlias;
  boolean BindingState;
  string  InterfaceGuid;
  string  IPAddress;
  string  SubnetMask;
};
```

## Members

The **DhcpServerv4Binding** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Binding** class has these properties.

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

Interface Id of interface available to Dhcp server for binding.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPAddress of interface available to Dhcp server for binding.

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Subnet Mask of interface available to Dhcp server for binding.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





