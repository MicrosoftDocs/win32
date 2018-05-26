---
title: Msvm\_ElementCapabilities class
description: Represents the association between managed elements and their capabilities.
ms.assetid: c31aa704-e5fd-4c97-853a-30f7cf4e117f
keywords:
- Msvm_ElementCapabilities class Hyper-V
- Msvm_ElementCapabilities class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ElementCapabilities
- Msvm_ElementCapabilities.ManagedElement
- Msvm_ElementCapabilities.Capabilities
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_ElementCapabilities class

Represents the association between managed elements and their capabilities.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ElementCapabilities : CIM_ElementCapabilities
{
  CIM_ManagedElement REF ManagedElement;
  CIM_Capabilities   REF Capabilities;
};
```

## Members

The **Msvm\_ElementCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementCapabilities** class has these properties.

<dl> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Capabilities**](cim-capabilities.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The capabilities associated with the managed element.

This property is inherited from [**CIM\_ElementCapabilities**](cim-elementcapabilities.md).

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The managed element.

This property is inherited from [**CIM\_ElementCapabilities**](cim-elementcapabilities.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ElementCapabilities** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementCapabilities**](cim-elementcapabilities.md)
</dt> <dt>

[**CIM\_ElementCapabilities**](https://msdn.microsoft.com/library/mt446044)
</dt> <dt>

[**Msvm\_ElementCapabilities (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850129)
</dt> <dt>

[Resource Management Classes](resource-management-classes.md)
</dt> </dl>

 

 





