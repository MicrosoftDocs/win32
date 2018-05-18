---
title: InterfaceIpFilter class
description: Represents an IP filter interface.
audience: developer
ms.assetid: '2ad3372c-da8a-468b-91de-a0768cbfa6d8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["InterfaceIpFilter class", "InterfaceIpFilter class, described"]
topic_type:
- apiref
api_name:
- InterfaceIpFilter
- InterfaceIpFilter.InterfaceAlias
- InterfaceIpFilter.Direction
- InterfaceIpFilter.AddressFamily
- InterfaceIpFilter.Action
- InterfaceIpFilter.List
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# InterfaceIpFilter class

Represents an IP filter interface

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class InterfaceIpFilter
{
  string InterfaceAlias;
  uint32 Direction;
  uint32 AddressFamily;
  uint32 Action;
  string List[];
};
```

## Members

The **InterfaceIpFilter** class has these types of members:

-   [Properties](#properties)

### Properties

The **InterfaceIpFilter** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The action for the IP filter.

This possible values for this property are allow or deny.

</dd> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The address family of the IP filter

This possible values for this property are IPv4 or IPv6.

</dd> <dt>

**Direction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The direction of network traffic to filter

This possible values for this property are Inbound or Outbound.

</dd> <dt>

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The interface alias of the IP filter

</dd> <dt>

**List**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The list of IP filters.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





