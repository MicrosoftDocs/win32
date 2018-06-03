---
title: Msvm\_VirtualSwitchManagementService class
description: Controls the definition, modification, and destruction of global networking resources such as virtual switches, switch ports, and internal Ethernet ports.
ms.assetid: a6c8a685-9c1c-45f2-8a24-d42120912883
keywords:
- Msvm_VirtualSwitchManagementService class Hyper-V
- Msvm_VirtualSwitchManagementService class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService
- Msvm_VirtualSwitchManagementService.RequestStateChange
- Msvm_VirtualSwitchManagementService.StartService
- Msvm_VirtualSwitchManagementService.StopService
- Msvm_VirtualSwitchManagementService.Caption
- Msvm_VirtualSwitchManagementService.Description
- Msvm_VirtualSwitchManagementService.ElementName
- Msvm_VirtualSwitchManagementService.InstallDate
- Msvm_VirtualSwitchManagementService.OperationalStatus
- Msvm_VirtualSwitchManagementService.Status
- Msvm_VirtualSwitchManagementService.HealthState
- Msvm_VirtualSwitchManagementService.EnabledState
- Msvm_VirtualSwitchManagementService.OtherEnabledState
- Msvm_VirtualSwitchManagementService.RequestedState
- Msvm_VirtualSwitchManagementService.TimeOfLastStateChange
- Msvm_VirtualSwitchManagementService.SystemCreationClassName
- Msvm_VirtualSwitchManagementService.SystemName
- Msvm_VirtualSwitchManagementService.Name
- Msvm_VirtualSwitchManagementService.PrimaryOwnerName
- Msvm_VirtualSwitchManagementService.StartMode
- Msvm_VirtualSwitchManagementService.Started
- Msvm_VirtualSwitchManagementService.StatusDescriptions
- Msvm_VirtualSwitchManagementService.EnabledDefault
- Msvm_VirtualSwitchManagementService.CreationClassName
- Msvm_VirtualSwitchManagementService.PrimaryOwnerContact
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

# Msvm\_VirtualSwitchManagementService class

Controls the definition, modification, and destruction of global networking resources such as virtual switches, switch ports, and internal Ethernet ports.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSwitchManagementService : CIM_Service
{
  string   Caption = "Hyper-V Networking Management Service";
  string   Description = "Provides Hyper-V Networking WMI management";
  string   ElementName = "Hyper-V Networking Management Service";
  datetime InstallDate;
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName;
  string   Name = "nvspwmi";
  string   PrimaryOwnerName;
  string   StartMode = "Automatic";
  boolean  Started = TRUE;
  string   StatusDescriptions[] = { "OK" };
  uint16   EnabledDefault = 2;
  string   CreationClassName = "Msvm_VirtualSwitchManagementService";
  string   PrimaryOwnerContact;
};
```

## Members

The **Msvm\_VirtualSwitchManagementService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_VirtualSwitchManagementService** class has these methods.



| Method                                                                                                                   | Description                                                                                                                                                                                                                         |
|:-------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BindExternalEthernetPort**](bindexternalethernetport-msvm-virtualswitchmanagementservice.md)                         | Binds an external Ethernet port to the Microsoft Windows Virtualization network subsystem. After this call is made, virtual machines can use the external Ethernet port to send data out over the physical network.<br/>      |
| [**ConnectSwitchPort**](connectswitchport-msvm-virtualswitchmanagementservice.md)                                       | Connects a switch port to a LAN endpoint. Upon success of the connection, a [**CIM\_ActiveConnection**](https://msdn.microsoft.com/library/cc136779) instance will be created that associates the port with the LAN endpoint.<br/>               |
| [**CreateInternalEthernetPort**](createinternalethernetport-msvm-virtualswitchmanagementservice.md)                     | Creates an internal Ethernet port with a static MAC address.<br/>                                                                                                                                                             |
| [**CreateInternalEthernetPortDynamicMac**](createinternalethernetportdynamicmac-msvm-virtualswitchmanagementservice.md) | Creates an internal Ethernet port with a dynamic MAC address.<br/>                                                                                                                                                            |
| [**CreateSwitch**](createswitch-msvm-virtualswitchmanagementservice.md)                                                 | Creates a new virtual switch.<br/>                                                                                                                                                                                            |
| [**CreateSwitchPort**](createswitchport-msvm-virtualswitchmanagementservice.md)                                         | Connects a NIC to a virtual switch port.<br/>                                                                                                                                                                                 |
| [**DeleteInternalEthernetPort**](deleteinternalethernetport-msvm-virtualswitchmanagementservice.md)                     | Deletes an internal Ethernet port.<br/>                                                                                                                                                                                       |
| [**DeleteSwitch**](deleteswitch-msvm-virtualswitchmanagementservice.md)                                                 | Deletes a virtual switch.<br/>                                                                                                                                                                                                |
| [**DeleteSwitchPort**](deleteswitchport-msvm-virtualswitchmanagementservice.md)                                         | Deletes a virtual switch port.<br/>                                                                                                                                                                                           |
| [**DisconnectSwitchPort**](disconnectswitchport-msvm-virtualswitchmanagementservice.md)                                 | Disconnects a virtual switch port.<br/>                                                                                                                                                                                       |
| **RequestStateChange**                                                                                                   | This method is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063)and is not supported.<br/>                                                                                                       |
| [**SetupSwitch**](setupswitch-msvm-virtualswitchmanagementservice.md)                                                   | Sets up a switch such that the existing network architecture is maintained.<br/>                                                                                                                                              |
| **StartService**                                                                                                         | This method is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is not supported.<br/>                                                                                                                             |
| **StopService**                                                                                                          | This method is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is not supported.<br/>                                                                                                                             |
| [**TeardownSwitch**](teardownswitch-msvm-virtualswitchmanagementservice.md)                                             | Deletes the internal port for a switch and unbinds the external adapter.<br/>                                                                                                                                                 |
| [**UnbindExternalEthernetPort**](unbindexternalethernetport-msvm-virtualswitchmanagementservice.md)                     | Unbinds an external Ethernet port to the Microsoft Windows Virtualization network subsystem. After this call is made, virtual machines cannot use the external Ethernet port to send data out over the physical network.<br/> |



 

### Properties

The **Msvm\_VirtualSwitchManagementService** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to "Hyper-V Networking Management Service".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is always set to "Msvm\_VirtualSwitchManagementService".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to "Provides Hyper-V Networking WMI management".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to "Hyper-V Networking Management Service".

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An administrator's default or startup configuration for the enabled state of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 2 (Enabled).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**OtherEnabledState**")
</dt> </dl>

The enabled and disabled states of this element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 5 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (5)


</dt> <dd>

Indicates the element does not support to be enabled or disabled.

</dd> </dl>

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to 5 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and operates within normal operational parameters and without error.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date and time the object was installed. This property does not need a value to indicate that the object is installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is not used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is always set to "nvspwmi".

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

The current status of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to 2 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> </dl>

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The enabled or disabled state of the element when the enabled state property is set to 1 ("Other"). This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

A string that provides information on how the primary owner of the service can be reached. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is not used.

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

The name of the primary owner for the service, if one is defined. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is not used.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the management service. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 12 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (12)


</dt> <dd>

Indicates that this instance does not support the **RequestedState** property.

</dd> </dl>

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the service has been started (**TRUE**), or stopped (**FALSE**). This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is always set to **TRUE**.

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_Service**](cim-service.md).**EnabledDefault**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Indicates whether the service is automatically started by a system, an operating system, and so on, or is started only upon request. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is always set to "Automatic".

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) but it is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and each array element is always set to "OK".

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The creation class name of the scoping system. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and is always set to "Msvm\_ComputerSystem".

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The NetBIOS name of the hosting computer system. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSwitchManagementService** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

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

[**CIM\_Service**](cim-service.md)
</dt> <dt>

[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





