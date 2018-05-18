---
title: Msvm\_VirtualSwitch class
description: Represents a virtual switch.
ms.assetid: '4bd532e1-6252-4f18-89d7-37e0ce7ea152'
keywords: ["Msvm_VirtualSwitch class Hyper-V", "Msvm_VirtualSwitch class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitch
- Msvm_VirtualSwitch.RequestStateChange
- Msvm_VirtualSwitch.SetPowerState
- Msvm_VirtualSwitch.Caption
- Msvm_VirtualSwitch.Description
- Msvm_VirtualSwitch.ElementName
- Msvm_VirtualSwitch.InstallDate
- Msvm_VirtualSwitch.OperationalStatus
- Msvm_VirtualSwitch.Status
- Msvm_VirtualSwitch.HealthState
- Msvm_VirtualSwitch.EnabledState
- Msvm_VirtualSwitch.OtherEnabledState
- Msvm_VirtualSwitch.RequestedState
- Msvm_VirtualSwitch.TimeOfLastStateChange
- Msvm_VirtualSwitch.Name
- Msvm_VirtualSwitch.PrimaryOwnerName
- Msvm_VirtualSwitch.IdentifyingDescriptions
- Msvm_VirtualSwitch.OtherIdentifyingInfo
- Msvm_VirtualSwitch.Dedicated
- Msvm_VirtualSwitch.ResetCapability
- Msvm_VirtualSwitch.PowerManagementCapabilities
- Msvm_VirtualSwitch.StatusDescriptions
- Msvm_VirtualSwitch.EnabledDefault
- Msvm_VirtualSwitch.CreationClassName
- Msvm_VirtualSwitch.PrimaryOwnerContact
- Msvm_VirtualSwitch.Roles
- Msvm_VirtualSwitch.NameFormat
- Msvm_VirtualSwitch.OtherDedicatedDescriptions
- Msvm_VirtualSwitch.ScopeOfResidence
- Msvm_VirtualSwitch.NumLearnableAddresses
- Msvm_VirtualSwitch.MaxVMQOffloads
- Msvm_VirtualSwitch.MaxChimneyOffloads
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VirtualSwitch class

Represents a virtual switch. Each switch has many different ports to which network adapters can be attached. The switch itself is not highly configurable and acts mostly as a placeholder.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSwitch : CIM_ComputerSystem
{
  string   Caption = "Virtual Switch";
  string   Description;
  string   ElementName;
  datetime InstallDate;
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  datetime TimeOfLastStateChange;
  string   Name;
  string   PrimaryOwnerName;
  string   IdentifyingDescriptions[];
  string   OtherIdentifyingInfo[];
  uint16   Dedicated[] = 0;
  uint16   ResetCapability = 5;
  uint16   PowerManagementCapabilities[];
  string   StatusDescriptions[] = { "OK" };
  uint16   EnabledDefault = 2;
  string   CreationClassName = "Msvm_VirtualSwitch";
  string   PrimaryOwnerContact;
  string   Roles[];
  string   NameFormat;
  string   OtherDedicatedDescriptions[];
  string   ScopeOfResidence;
  uint32   NumLearnableAddresses;
  uint32   MaxVMQOffloads;
  uint32   MaxChimneyOffloads;
};
```

## Members

The **Msvm\_VirtualSwitch** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_VirtualSwitch** class has these methods.



| Method                 | Description                              |
|:-----------------------|:-----------------------------------------|
| **RequestStateChange** | This method is not supported.<br/> |
| **SetPowerState**      | This method is not supported.<br/> |



 

### Properties

The **Msvm\_VirtualSwitch** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one- line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is always set to "Virtual Switch".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or the subclass that is used in the creation of an instance. This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503) and is always set to "Msvm\_VirtualSwitch".

</dd> <dt>

**Dedicated**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|MIB-II.sysServices", "FC-GS.INCITS-T11 \| Platform \| PlatformType"), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**OtherDedicatedDescriptions**")
</dt> </dl>

Indicates whether the computer system is a special-purpose system (dedicated to a particular use), versus being a general-purpose system. This property is inherited from [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) and it is set to 0 (Not Dedicated).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

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

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**OtherIdentifyingInfo**")
</dt> </dl>

This property is inherited from [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) and it is set to **NULL**.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A datetime value that indicates when the object was installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**MaxChimneyOffloads**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of Chimney offloads allowed for a port on this switch.

**Windows Server 2008:** The **MaxChimneyOffloads** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**MaxVMQOffloads**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of VM queue (VMQ) offloads allowed for a port on this switch.

**Windows Server 2008:** The **MaxVMQOffloads** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

A name that uniquely identifies the service and provides an indication of the functionality that is managed. This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503).

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that identifies how the system name was generated, using the subclass heuristic. This property is inherited from [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) and it is set to **NULL**.

</dd> <dt>

**NumLearnableAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of learnable addresses for this switch.

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

**OtherDedicatedDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**Dedicated**")
</dt> </dl>

A string that describes how or why the system is dedicated when the **Dedicated** array includes the value 2 (Other). This property is inherited from [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) and it is set to **NULL**.

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**IdentifyingDescriptions**")
</dt> </dl>

This property is inherited from [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) and it is set to **NULL**.

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities.PowerCapabilities"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System Power Controls\|001.2")
</dt> </dl>

This property is inherited from [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) but it is not used.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

A string that provides information on how the primary owner of the service can be reached. This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503) and is not used.

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

The name of the primary owner for the service, if one is defined. This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503) and is not used.

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

**ResetCapability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System Hardware Security\|001.4")
</dt> </dl>

This property is inherited from [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) and it is set to 5 (Not Implemented).

<dt>

<span id="Not_Implemented"></span><span id="not_implemented"></span><span id="NOT_IMPLEMENTED"></span>

<span id="Not_Implemented"></span><span id="not_implemented"></span><span id="NOT_IMPLEMENTED"></span>**Not Implemented** (5)


</dt> <dd>

Not Implemented.

</dd> </dl>

</dd> <dt>

**Roles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings that describe the roles the system plays in the information technology environment. This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503) and it is set to **NULL**.

</dd> <dt>

**ScopeOfResidence**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The authorization manager scope for the switch service.

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

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to "OK".

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

Access to the **Msvm\_VirtualSwitch** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

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

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> <dt>

[**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





