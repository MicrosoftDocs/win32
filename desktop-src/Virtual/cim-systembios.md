---
title: CIM\_SystemBIOS class
description: Associates a BIOS with a computer system.
ms.assetid: 48d75e5c-59df-4c8b-892c-9ca64a0690db
keywords:
- CIM_SystemBIOS class Hyper-V
- CIM_SystemBIOS class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_SystemBIOS
- CIM_SystemBIOS.GroupComponent
- CIM_SystemBIOS.PartComponent
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

# CIM\_SystemBIOS class

Associates a BIOS with a computer system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Aggregation, Version("2.7.0"), AMENDMENT]
class CIM_SystemBIOS : CIM_SystemComponent
{
  CIM_ComputerSystem REF GroupComponent;
  CIM_BIOSElement    REF PartComponent;
};
```

## Members

The **CIM\_SystemBIOS** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SystemBIOS** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The computer system that boots from the BIOS.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BIOSElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The BIOS.

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

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> </dl>

 

 





