---
title: Msvm\_HostedSwitchService class
description: An association that connects a virtual switch service to transparent bridging service.
ms.assetid: 7fdcf259-2fea-491c-b1da-8cf50949fa37
keywords:
- Msvm_HostedSwitchService class Hyper-V
- Msvm_HostedSwitchService class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_HostedSwitchService
- Msvm_HostedSwitchService.Antecedent
- Msvm_HostedSwitchService.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_HostedSwitchService class

An association that connects a virtual switch service to transparent bridging service.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_HostedSwitchService : CIM_HostedService
{
  Msvm_VirtualSwitch REF Antecedent;
  CIM_Service        REF Dependent;
};
```

## Members

The **Msvm\_HostedSwitchService** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_HostedSwitchService** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSwitch**](msvm-virtualswitch.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

A reference to the hosting system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

A reference to the service hosted on the system.

</dd> </dl>

## Remarks

Access to the **Msvm\_HostedSwitchService** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dt>

[**CIM\_HostedService**](https://msdn.microsoft.com/library/aa387865)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





