---
title: Msvm\_SystemTerminalConnection class
description: Associates a virtual computer system with a terminal connection.
ms.assetid: '7de615d4-f89f-42b2-a043-05c8a0f85f32'
keywords: ["Msvm_SystemTerminalConnection class Hyper-V", "Msvm_SystemTerminalConnection class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_SystemTerminalConnection
- Msvm_SystemTerminalConnection.Antecedent
- Msvm_SystemTerminalConnection.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_SystemTerminalConnection class

Associates a virtual computer system with a terminal connection.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SystemTerminalConnection : CIM_HostedDependency
{
  Msvm_ComputerSystem     REF Antecedent;
  Msvm_TerminalConnection REF Dependent;
};
```

## Members

The **Msvm\_SystemTerminalConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SystemTerminalConnection** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ComputerSystem**](msvm-computersystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The virtual system to which the connection is attached.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_TerminalConnection**](msvm-terminalconnection.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The connection to the virtual system.

</dd> </dl>

## Remarks

Access to the **Msvm\_SystemTerminalConnection** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> <dt>

[**CIM\_HostedDependency**](https://msdn.microsoft.com/library/mt446122)
</dt> <dt>

[Video Classes](video-classes.md)
</dt> </dl>

 

 





