---
title: Msvm\_VirtualizationComponent class
description: Represents a service of the Microsoft Windows Hyper-V platform.
ms.assetid: c99b5a82-05a2-4a77-96a4-6ea8a66618a2
keywords:
- Msvm_VirtualizationComponent class Hyper-V
- Msvm_VirtualizationComponent class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualizationComponent
- Msvm_VirtualizationComponent.Name
- Msvm_VirtualizationComponent.CLSID
- Msvm_VirtualizationComponent.Context
- Msvm_VirtualizationComponent.Enabled
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

# Msvm\_VirtualizationComponent class

Represents a service of the Microsoft Windows Hyper-V platform.

The following syntax is simplified Managed Object Format (MOF) code.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class Msvm_VirtualizationComponent
{
  string  Name;
  string  CLSID;
  uint32  Context = 1;
  boolean Enabled = True;
};
```

## Members

The **Msvm\_VirtualizationComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualizationComponent** class has these properties.

<dl> <dt>

**CLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A **GUID** that represents the class identifier of the service's COM object.

</dd> <dt>

**Context**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The context in which the newly created object will run. This value is passed in the *dwClsContext* parameter to [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615). This property is always set to 1.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, this instance is enabled and can be used to complete client requests. This property is always set to **True**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A language-neutral string that uniquely identifies the service. The following format is suggested to prevent naming conflicts: "vendor\|component\|version". For example, this name represents version 1.0 of the Microsoft Emulated Network Port Component: "Microsoft\|EmulatedNetworkPortComponent\|V1.0".

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualizationComponent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[Profile Registration Classes](profile-registration.md)
</dt> </dl>

 

 





