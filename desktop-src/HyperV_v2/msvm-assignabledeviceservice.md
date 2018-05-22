---
Description: 'Manages the assignable devices on a host computer system.'
ms.assetid: 'd958e978-682e-49eb-bd10-d31d9563fdbf'
title: 'Msvm\_AssignableDeviceService class'
---

# Msvm\_AssignableDeviceService class

Manages the assignable devices on a host computer system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_AssignableDeviceService : CIM_Service
{
};
```

## Members

The **Msvm\_AssignableDeviceService** class has these types of members:

-   [Methods](#methods)

### Methods

The **Msvm\_AssignableDeviceService** class has these methods.



| Method                                                                                    | Description                                                                                    |
|:------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**DismountAssignableDevice**](msvm-assignabledeviceservice-dismountassignabledevice.md) | Dismounts the specified PCI device so that it can be assigned.<br/>                      |
| [**MountAssignableDevice**](msvm-assignabledeviceservice-mountassignabledevice.md)       | Mounts the specified PCI device so that it can be used by the host computer system.<br/> |



 

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 




