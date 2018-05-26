---
title: CIM\_SystemComponent class
description: Represents an association between a system and one of the elements that compose it.
ms.assetid: aa60a6a5-d111-428a-a057-aad4d17d39eb
keywords:
- CIM_SystemComponent class Hyper-V
- CIM_SystemComponent class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_SystemComponent
- CIM_SystemComponent.GroupComponent
- CIM_SystemComponent.PartComponent
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_SystemComponent class

Represents an association between a system and one of the elements that compose it.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Association, Aggregation, Version("2.10.0"), AMENDMENT]
class CIM_SystemComponent : CIM_Component
{
  CIM_System               REF GroupComponent;
  CIM_ManagedSystemElement REF PartComponent;
};
```

## Members

The **CIM\_SystemComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SystemComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_System**](cim-system.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

The system that contains the **PartComponent**.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The child element that is a component of the System.

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

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 





