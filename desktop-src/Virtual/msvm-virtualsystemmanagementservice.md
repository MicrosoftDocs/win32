---
title: Msvm\_VirtualSystemManagementService class
description: Represents the virtualization service present on a single host system.
ms.assetid: 88f9579c-cd69-4a53-965d-d4386b9c8ef7
keywords:
- Msvm_VirtualSystemManagementService class Hyper-V
- Msvm_VirtualSystemManagementService class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService
- Msvm_VirtualSystemManagementService.RequestStateChange
- Msvm_VirtualSystemManagementService.StartService
- Msvm_VirtualSystemManagementService.StopService
- Msvm_VirtualSystemManagementService.PlanVirtualSystem
- Msvm_VirtualSystemManagementService.InstantiateVirtualSystem
- Msvm_VirtualSystemManagementService.CloneVirtualSystem
- Msvm_VirtualSystemManagementService.Caption
- Msvm_VirtualSystemManagementService.Description
- Msvm_VirtualSystemManagementService.ElementName
- Msvm_VirtualSystemManagementService.InstallDate
- Msvm_VirtualSystemManagementService.OperationalStatus
- Msvm_VirtualSystemManagementService.Status
- Msvm_VirtualSystemManagementService.HealthState
- Msvm_VirtualSystemManagementService.EnabledState
- Msvm_VirtualSystemManagementService.TimeOfLastStateChange
- Msvm_VirtualSystemManagementService.SystemCreationClassName
- Msvm_VirtualSystemManagementService.SystemName
- Msvm_VirtualSystemManagementService.CreationClassName
- Msvm_VirtualSystemManagementService.Name
- Msvm_VirtualSystemManagementService.PrimaryOwnerName
- Msvm_VirtualSystemManagementService.PrimaryOwnerContact
- Msvm_VirtualSystemManagementService.StartMode
- Msvm_VirtualSystemManagementService.Started
- Msvm_VirtualSystemManagementService.StatusDescriptions
- Msvm_VirtualSystemManagementService.OtherEnabledState
- Msvm_VirtualSystemManagementService.RequestedState
- Msvm_VirtualSystemManagementService.EnabledDefault
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

# Msvm\_VirtualSystemManagementService class

Represents the virtualization service present on a single host system. **Msvm\_VirtualSystemManagementService** is used to control the definition, modification, and deletion of virtual systems. It also has methods for performing operations on virtual systems, such as cloning, snapshotting, and the importing or exporting of virtual systems. To retrieve per-VM information, use [**Msvm\_ComputerSystem**](msvm-computersystem.md).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemManagementService : CIM_VirtualSystemManagementService
{
  string   Caption = "Virtual System Management Service";
  string   Description = "Service for creating, manipulating, and managing virtual systems";
  string   ElementName = "Virtual System Management Service";
  datetime InstallDate;
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 2;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName = ;
  string   SystemName;
  string   CreationClassName = "Msvm_VirtualSystemManagementService";
  string   Name = "vmms";
  string   PrimaryOwnerName;
  string   PrimaryOwnerContact;
  string   StartMode;
  boolean  Started = TRUE;
  string   StatusDescriptions[] = { "The service is running normally" };
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
};
```

## Members

The **Msvm\_VirtualSystemManagementService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_VirtualSystemManagementService** class has these methods.



| Method                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                       |
|:-------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddKvpItems**](addkvpitems-msvm-virtualsystemmanagementservice.md)                                             | Adds key-value pairs to a virtual system.<br/>                                                                                                                                                                                                                                                                                              |
| [**AddVirtualSystemResources**](addvirtualsystemresources-msvm-virtualsystemmanagementservice.md)                 | Add resources to an existing virtual computer system.<br/>                                                                                                                                                                                                                                                                                  |
| [**ApplyVirtualSystemSnapshot**](applyvirtualsystemsnapshot-msvm-virtualsystemmanagementservice.md)               | Applies the specified snapshot to the virtual computer system.<br/>                                                                                                                                                                                                                                                                         |
| [**ApplyVirtualSystemSnapshotEx**](msvm-virtualsystemmanagementservice-applyvirtualsystemsnapshotex.md)           | Applies the specified snapshot to the virtual computer system.<br/> **Windows Server 2008:** The [**ApplyVirtualSystemSnapshotEx**](msvm-virtualsystemmanagementservice-applyvirtualsystemsnapshotex.md) method is not supported before Windows Server 2008 R2.<br/>                                                                 |
| [**CheckSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-checksystemcompatibilityinfo.md)           | Verifies whether this computer system is able to host the specified VM.<br/> **Windows Server 2008:** The [**CheckSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-checksystemcompatibilityinfo.md) method is not supported before Windows Server 2008 R2.<br/>                                                        |
| **CloneVirtualSystem**                                                                                             | This method is not supported.<br/>                                                                                                                                                                                                                                                                                                          |
| [**CreateVirtualSystemSnapshot**](createvirtualsystemsnapshot-msvm-virtualsystemmanagementservice.md)             | Creates a new snapshot for the virtual computer system.<br/>                                                                                                                                                                                                                                                                                |
| [**DefineVirtualSystem**](definevirtualsystem-msvm-virtualsystemmanagementservice.md)                             | Creates a new virtual computer system definition.<br/>                                                                                                                                                                                                                                                                                      |
| [**DestroyVirtualSystem**](destroyvirtualsystem-msvm-virtualsystemmanagementservice.md)                           | Deletes an existing virtual computer system definition.<br/>                                                                                                                                                                                                                                                                                |
| [**ExportVirtualSystem**](exportvirtualsystem-msvm-virtualsystemmanagementservice.md)                             | Deprecated. Use the [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) method.<br/>                                                                                                                                                                                                                 |
| [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md)                         | Exports a virtual computer system to a file.<br/> **Windows Server 2008:** The [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) method is not supported before Windows Server 2008 R2.<br/>                                                                                                 |
| [**FormatError**](formaterror-msvm-virtualsystemmanagementservice.md)                                             | Returns the formatted error message string for the specified array of embedded [**Msvm\_Error**](msvm-error.md) instances.<br/>                                                                                                                                                                                                            |
| [**GetSummaryInformation**](getsummaryinformation-msvm-virtualsystemmanagementservice.md)                         | Returns virtual system summary information.<br/>                                                                                                                                                                                                                                                                                            |
| [**GetSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-getsystemcompatibilityinfo.md)               | Generates an opaque blob of data containing compatibility information for the specified system.<br/> **Windows Server 2008:** The [**GetSystemCompatibilityInfo**](msvm-virtualsystemmanagementservice-getsystemcompatibilityinfo.md) method is not supported before Windows Server 2008 R2.<br/>                                    |
| [**GetVirtualSystemImportSettingData**](msvm-virtualsystemmanagementservice-getvirtualsystemimportsettingdata.md) | Returns an embedded instance of [**Msvm\_VirtualSystemImportSettingData**](msvm-virtualsystemimportsettingdata.md).<br/> **Windows Server 2008:** The [**GetVirtualSystemImportSettingData**](msvm-virtualsystemmanagementservice-getvirtualsystemimportsettingdata.md) method is not supported before Windows Server 2008 R2.<br/> |
| [**GetVirtualSystemThumbnailImage**](getvirtualsystemthumbnailimage-msvm-virtualsystemmanagementservice.md)       | Retrieves a thumbnail image of an existing virtual computer system.<br/>                                                                                                                                                                                                                                                                    |
| [**ImportVirtualSystem**](importvirtualsystem-msvm-virtualsystemmanagementservice.md)                             | Deprecated. Use the [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md) method.<br/>                                                                                                                                                                                                                 |
| [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md)                         | Imports a virtual computer system definition from the specified file.<br/> **Windows Server 2008:** The [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md) method is not supported before Windows Server 2008 R2.<br/>                                                                        |
| **InstantiateVirtualSystem**                                                                                       | This method is not supported.<br/>                                                                                                                                                                                                                                                                                                          |
| [**ModifyKvpItems**](modifykvpitems-msvm-virtualsystemmanagementservice.md)                                       | Modifies existing key-value pairs on a virtual computer system.<br/>                                                                                                                                                                                                                                                                        |
| [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md)                         | Modifies the service's setting data.<br/>                                                                                                                                                                                                                                                                                                   |
| [**ModifyVirtualSystem**](modifyvirtualsystem-msvm-virtualsystemmanagementservice.md)                             | Modifies the setting data for an existing virtual computer system.<br/>                                                                                                                                                                                                                                                                     |
| [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md)           | Modifies the setting data for existing resources on a virtual computer system.<br/>                                                                                                                                                                                                                                                         |
| **PlanVirtualSystem**                                                                                              | This method is not supported.<br/>                                                                                                                                                                                                                                                                                                          |
| [**RemoveKvpItems**](removekvpitems-msvm-virtualsystemmanagementservice.md)                                       | Removes existing key-value pairs from a virtual computer system.<br/>                                                                                                                                                                                                                                                                       |
| [**RemoveVirtualSystemResources**](removevirtualsystemresources-msvm-virtualsystemmanagementservice.md)           | Remove resources from an existing virtual computer system.<br/>                                                                                                                                                                                                                                                                             |
| [**RemoveVirtualSystemSnapshot**](removevirtualsystemsnapshot-msvm-virtualsystemmanagementservice.md)             | Deletes an existing snapshot from the virtual computer system.<br/>                                                                                                                                                                                                                                                                         |
| [**RemoveVirtualSystemSnapshotTree**](removevirtualsystemsnapshottree-msvm-virtualsystemmanagementservice.md)     | Removes an existing snapshot and all its children from the virtual computer system.<br/>                                                                                                                                                                                                                                                    |
| **RequestStateChange**                                                                                             | This method is not supported.<br/>                                                                                                                                                                                                                                                                                                          |
| **StartService**                                                                                                   | This method is not supported.<br/>                                                                                                                                                                                                                                                                                                          |
| **StopService**                                                                                                    | This method is not supported.<br/>                                                                                                                                                                                                                                                                                                          |



 

### Properties

The **Msvm\_VirtualSystemManagementService** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Virtual System Management Service".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is always set to "Msvm\_VirtualSystemManagementService".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Service for creating, manipulating, and managing virtual systems".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Virtual System Management Service".

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

The enabled and disabled states of an element. It can also indicate the transitions between these requested states. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 2 (Enabled).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)


</dt> <dd>

Indicates that the element executes or could execute commands, processes any queued commands, and queues new requests.

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

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The label by which the object is known. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is always set to "vmms".

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

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 ("Other"). This property must be set to null when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

Any information about how the primary owner of the service can be reached (for example, phone number, email address, and so on). This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is always set to **NULL**.

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

The name of the primary owner for the service, if one is defined. The primary owner is the initial support contact for the service. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is always set to **NULL**.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. A particular instance of [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) might not support RequestedStateChange. If this occurs, the value 12 ("Not Applicable") is used. This property is inherited from **CIM\_EnabledLogicalElement** and it is always set to 12 (Not Applicable).

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

Indicates whether the service is currently running. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is always set to **TRUE**.

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

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and each array element is always set to "The service is running normally".

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping system's creation class name. This property is inherited from [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) and it is always set to "Msvm\_ComputerSystem".

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

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063).

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemManagementService** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_VirtualSystemManagementService**](https://msdn.microsoft.com/library/cc136952)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850253)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 





