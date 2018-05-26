---
title: Msvm\_TerminalService class
description: Manages all remote terminal connections to a particular host.
ms.assetid: 2eb5ebab-4241-4d64-a32c-eaa87bfdb6f4
keywords:
- Msvm_TerminalService class Hyper-V
- Msvm_TerminalService class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_TerminalService
- Msvm_TerminalService.RequestStateChange
- Msvm_TerminalService.StartService
- Msvm_TerminalService.StopService
- Msvm_TerminalService.Caption
- Msvm_TerminalService.Description
- Msvm_TerminalService.ElementName
- Msvm_TerminalService.InstallDate
- Msvm_TerminalService.OperationalStatus
- Msvm_TerminalService.StatusDescriptions
- Msvm_TerminalService.Status
- Msvm_TerminalService.HealthState
- Msvm_TerminalService.EnabledState
- Msvm_TerminalService.OtherEnabledState
- Msvm_TerminalService.RequestedState
- Msvm_TerminalService.EnabledDefault
- Msvm_TerminalService.TimeOfLastStateChange
- Msvm_TerminalService.SystemCreationClassName
- Msvm_TerminalService.SystemName
- Msvm_TerminalService.CreationClassName
- Msvm_TerminalService.Name
- Msvm_TerminalService.PrimaryOwnerName
- Msvm_TerminalService.PrimaryOwnerContact
- Msvm_TerminalService.StartMode
- Msvm_TerminalService.Started
- Msvm_TerminalService.ListenerPort
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

# Msvm\_TerminalService class

Manages all remote terminal connections to a particular host. The service uses a configurable port to initiate all terminal connections.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_TerminalService : CIM_Service
{
  string   Caption = ;
  string   Description = "Microsoft Virtual Terminal Service";
  string   ElementName = "Microsoft Virtual Terminal Connection Management Service";
  datetime InstallDate;
  uint16   OperationalStatus[] = 2;
  string   StatusDescriptions[] = { "The virtual terminal connection management service is fully operational" };
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName;
  string   CreationClassName = "Msvm_TerminalService";
  string   Name = "Microsoft Virtual Terminal Connection Management Service";
  string   PrimaryOwnerName;
  string   PrimaryOwnerContact;
  string   StartMode;
  boolean  Started;
  uint32   ListenerPort;
};
```

## Members

The **Msvm\_TerminalService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_TerminalService** class has these methods.



| Method                 | Description                              |
|:-----------------------|:-----------------------------------------|
| **RequestStateChange** | This method is not supported.<br/> |
| **StartService**       | This method is not supported.<br/> |
| **StopService**        | This method is not supported.<br/> |



 

### Properties

The **Msvm\_TerminalService** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Terminal Service".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is set to "Msvm\_TerminalService".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Microsoft Virtual Terminal Service".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Microsoft Virtual Terminal Connection Management Service" by default.

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An administrator's default or startup configuration for the enabled state of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 2 (Enabled).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**OtherEnabledState**")
</dt> </dl>

The enabled and disabled states of an element. It can also indicate the transitions between these requested states. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is set to 5 (Enabled).

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

The current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 5 (OK).

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

The date and time the virtual machine configuration was created. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**ListenerPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network port on which the initial remote session connection will be made.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The label by which the object is known. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is the same as the **ElementName** property.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

The current statuses of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and each array element is always set to 2 (OK).

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

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property must be set to **null** when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

A value that provides information about how the primary owner of the service can be reached (for example, phone number, email address, and so on). This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is set to **NULL**.

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

The name of the primary owner for the service, if one is defined. The primary owner is the initial support contact for the service. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is set to **NULL**.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. A particular instance of [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) might not support the **RequestStateChange** method. If this occurs, the value 12 (Not Applicable) is used. This property is inherited from **CIM\_EnabledLogicalElement** and it is set to 12 (Not Applicable).

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
</dt> <dt>

Qualifiers: 
</dt> </dl>

Indicates whether the service is currently running. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_Service**](cim-service.md).**EnabledDefault**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string value that indicates whether the service is automatically started by a system, an operating system, or is started only upon request. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is always set to **NULL**.

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

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and each array element is always set to "The virtual terminal connection management service is fully operational".

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping system's creation class name. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is set to "Msvm\_ComputerSystem".

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the hosting computer system. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is set to **NULL**.

</dd> </dl>

## Remarks

Access to the **Msvm\_TerminalService** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[Video Classes](video-classes.md)
</dt> </dl>

 

 





