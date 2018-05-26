---
title: CIM\_ElementAllocationCapabilities class
description: TBD
ms.assetid: 2d03781b-aca2-4681-bc44-636209c4e3f2
keywords:
- CIM_ElementAllocationCapabilities class Hyper-V
- CIM_ElementAllocationCapabilities class Hyper-V , described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_ElementAllocationCapabilities class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.13.0")]
class CIM_ElementAllocationCapabilities : CIM_ElementCapabilities
{
  CIM_AllocationCapabilities REF Capabilities;
  CIM_ManagedElement         REF ManagedElement;
};
```

## Members

The **CIM\_ElementAllocationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementAllocationCapabilities** class has these properties.

<dl> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **CIM\_AllocationCapabilities**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Capabilities")
</dt> </dl>

TBD

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ManagedElement"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementCapabilities**](cim-elementcapabilities.md)
</dt> </dl>

 

 





