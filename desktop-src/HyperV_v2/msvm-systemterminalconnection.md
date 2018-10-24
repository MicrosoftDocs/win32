---
Description: Associates a virtual machine with a terminal connection.
ms.assetid: 31979FB8-3870-44D9-9720-AD99237C5268
title: Msvm_SystemTerminalConnection class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SystemTerminalConnection
- Msvm_SystemTerminalConnection.Antecedent
- Msvm_SystemTerminalConnection.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SystemTerminalConnection class

Associates a virtual machine with a terminal connection.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SystemTerminalConnection : CIM_HostedDependency
{
  Msvm_ComputerSystem     REF Antecedent;
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

The virtual machine to which the connection is attached.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_TerminalConnection**](msvm-terminalconnection.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The connection to the virtual machine.

</dd> </dl>

## Remarks

Access to the **Msvm\_SystemTerminalConnection** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> <dt>

[**CIM\_HostedDependency**](https://msdn.microsoft.com/library/cc136861)
</dt> <dt>

[Video Classes](video-classes.md)
</dt> </dl>

 

 




