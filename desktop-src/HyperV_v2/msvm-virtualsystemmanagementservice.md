---
description: Represents the virtualization service present on a single host system.
ms.assetid: '7f4bd9e0-b034-4882-ad01-f7df740939ae'
title: Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService
- Msvm_VirtualSystemManagementService.InstanceID
- Msvm_VirtualSystemManagementService.Caption
- Msvm_VirtualSystemManagementService.Description
- Msvm_VirtualSystemManagementService.ElementName
- Msvm_VirtualSystemManagementService.InstallDate
- Msvm_VirtualSystemManagementService.Name
- Msvm_VirtualSystemManagementService.OperationalStatus
- Msvm_VirtualSystemManagementService.StatusDescriptions
- Msvm_VirtualSystemManagementService.Status
- Msvm_VirtualSystemManagementService.HealthState
- Msvm_VirtualSystemManagementService.CommunicationStatus
- Msvm_VirtualSystemManagementService.DetailedStatus
- Msvm_VirtualSystemManagementService.OperatingStatus
- Msvm_VirtualSystemManagementService.PrimaryStatus
- Msvm_VirtualSystemManagementService.EnabledState
- Msvm_VirtualSystemManagementService.OtherEnabledState
- Msvm_VirtualSystemManagementService.RequestedState
- Msvm_VirtualSystemManagementService.EnabledDefault
- Msvm_VirtualSystemManagementService.TimeOfLastStateChange
- Msvm_VirtualSystemManagementService.AvailableRequestedStates
- Msvm_VirtualSystemManagementService.TransitioningToState
- Msvm_VirtualSystemManagementService.SystemCreationClassName
- Msvm_VirtualSystemManagementService.SystemName
- Msvm_VirtualSystemManagementService.CreationClassName
- Msvm_VirtualSystemManagementService.PrimaryOwnerName
- Msvm_VirtualSystemManagementService.PrimaryOwnerContact
- Msvm_VirtualSystemManagementService.StartMode
- Msvm_VirtualSystemManagementService.Started
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualSystemManagementService class

Represents the virtualization service present on a single host system. **Msvm\_VirtualSystemManagementService** is used to control the definition, modification, and deletion of virtual machines. It also has methods for performing operations on virtual machines, such as cloning, snapshotting, and the importing or exporting of virtual machines. To retrieve per-virtual machine information, use [**Msvm\_ComputerSystem**](msvm-computersystem.md).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemManagementService : CIM_VirtualSystemManagementService
{
  string   InstanceID;
  string   Caption = "Virtual System Management Service";
  string   Description = "Service for creating, manipulating, and managing virtual machines";
  string   ElementName = "Hyper-V Virtual System Management Service";
  datetime InstallDate;
  string   Name = "vmms";
  uint16   OperationalStatus[] = { 2 };
  string   StatusDescriptions[] = { "The service is running normally" };
  string   Status;
  uint16   HealthState = 5;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  uint16   EnabledState = 2;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  uint16   AvailableRequestedStates[];
  uint16   TransitioningToState;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName;
  string   CreationClassName = "Msvm_VirtualSystemManagementService";
  string   PrimaryOwnerName;
  string   PrimaryOwnerContact;
  string   StartMode;
  boolean  Started = True;
};
```

## Members

The **Msvm\_VirtualSystemManagementService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_VirtualSystemManagementService** class has these methods.



| Method                                                                                                                 | Description                                                                                                                                                                                                                                        |
|:-----------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddBootSourceSettings**](msvm-virtualsystemmanagementservice-addbootsourcesettings.md)                             | Adds boot sources to a virtual system configuration when applied to a "state" virtual system configuration.<br/>                                                                                                                             |
| [**AddFeatureSettings**](addfeaturesettings-msvm-virtualsystemmanagementservice.md)                                   | Adds Ethernet feature settings to the configuration of a virtual machine Ethernet connection.<br/>                                                                                                                                           |
| [**AddFibreChannelChap**](addfibrechannelchap-msvm-virtualsystemmanagementservice.md)                                 | Adds DH-CHAP parameters to a synthetic Fibre Channel port in a virtual machine.<br/>                                                                                                                                                         |
| [**AddGuestServiceSettings**](msvm-virtualsystemmanagementservice-addguestservicesettings.md)                         | Adds guest service settings to a virtual system configuration.<br/> When applied to parts of a "current" virtual system configuration, as a side effect guest services of the active virtual system may be modified.<br/>              |
| [**AddKvpItems**](addkvpitems-msvm-virtualsystemmanagementservice.md)                                                 | Adds key-value pairs to a virtual machine.<br/>                                                                                                                                                                                              |
| [**AddResourceSettings**](addresourcesettings-msvm-virtualsystemmanagementservice.md)                                 | Adds resources to a virtual machine configuration.<br/>                                                                                                                                                                                      |
| [**AddSystemComponentSettings**](msvm-virtualsystemmanagementservice-addsystemcomponentsettings.md)                   | Adds generic settings to a virtual system configuration.<br/>                                                                                                                                                                                |
| [**DefinePlannedSystem**](msvm-virtualsystemmanagementservice-defineplannedsystem.md)                                 | Defines a planned virtual system.<br/> Input that is not completely specified may be filled out with default values.<br/>                                                                                                              |
| [**DefineSystem**](definesystem-msvm-virtualsystemmanagementservice.md)                                               | Creates a new virtual machine definition.<br/>                                                                                                                                                                                               |
| [**DestroySystem**](destroysystem-msvm-virtualsystemmanagementservice.md)                                             | Deletes an existing virtual machine definition.<br/>                                                                                                                                                                                         |
| [**DiagnoseNetworkConnection**](msvm-virtualsystemmanagementservice-diagnosenetworkconnection.md)                     | Diagnoses the network connectivity of a VM in a Windows Network Virtualization Environment.<br/>                                                                                                                                             |
| [**ExportSystemDefinition**](exportsystemdefinition-msvm-virtualsystemmanagementservice.md)                           | Exports a virtual machine, or a snapshot of a virtual machine, to a file.<br/>                                                                                                                                                               |
| [**FormatError**](formaterror-msvm-virtualsystemmanagementservice.md)                                                 | Returns a formatted error message string for the specified array of embedded [**Msvm\_Error**](msvm-error.md) instances.<br/>                                                                                                               |
| [**GenerateWwpn**](generatewwpn-msvm-virtualsystemmanagementservice.md)                                               | Generates a set of World Wide Port Names (WWPNs).<br/>                                                                                                                                                                                       |
| [**GetCurrentWwpnFromGenerator**](getcurrentwwpnfromgenerator-msvm-virtualsystemmanagementservice.md)                 | Provides the ability to preview the current World Wide Port Name (WWPN) without the WWPN being reserved.<br/>                                                                                                                                |
| [**GetDefinitionFileSummaryInformation**](getdefinitionfilesummaryinformation-msvm-virtualsystemmanagementservice.md) | Returns virtual machine summary information for the specified virtual machine definition files.<br/>                                                                                                                                         |
| [**GetSizeOfSystemFiles**](getsizeofsystemfiles-msvm-virtualsystemmanagementservice.md)                               | Retrieves the total size of the system files of virtual machine.<br/>                                                                                                                                                                        |
| [**GetSummaryInformation**](getsummaryinformation-msvm-virtualsystemmanagementservice.md)                             | Returns virtual machine summary information.<br/>                                                                                                                                                                                            |
| [**GetVirtualSystemThumbnailImage**](getvirtualsystemthumbnailimage-msvm-virtualsystemmanagementservice.md)           | Retrieves a thumbnail image of an existing virtual machine.<br/>                                                                                                                                                                             |
| [**ImportSnapshotDefinitions**](importsnapshotdefinitions-msvm-virtualsystemmanagementservice.md)                     | Searches the specified folder for any snapshot definition files associated with the specified planned computer system, and creates a new snapshot on the planned computer system for every associated definition file in this location.<br/> |
| [**ImportSystemDefinition**](importsystemdefinition-msvm-virtualsystemmanagementservice.md)                           | Creates a new planned computer system based on the specified virtual machine definition.<br/>                                                                                                                                                |
| [**ModifyDiskMergeSettings**](modifydiskmergesettings-msvm-virtualsystemmanagementservice.md)                         | Modifies the disk merge setting data.<br/>                                                                                                                                                                                                   |
| [**ModifyFeatureSettings**](modifyfeaturesettings-msvm-virtualsystemmanagementservice.md)                             | Modifies the current feature settings of a virtual machine Ethernet connection.<br/>                                                                                                                                                         |
| [**ModifyGuestServiceSettings**](msvm-virtualsystemmanagementservice-modifyguestservicesettings.md)                   | Modifies guest service settings.<br/> When applied to parts of a "current" virtual system configuration, as a side effect guest services of the active virtual system may be modified.<br/>                                            |
| [**ModifyKvpItems**](modifykvpitems-msvm-virtualsystemmanagementservice.md)                                           | Modifies existing key-value pairs on a virtual machine.<br/>                                                                                                                                                                                 |
| [**ModifyResourceSettings**](modifyresourcesettings-msvm-virtualsystemmanagementservice.md)                           | Modifies virtual resource settings.<br/>                                                                                                                                                                                                     |
| [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md)                             | Modifies the service's setting data.<br/>                                                                                                                                                                                                    |
| [**ModifySystemComponentSettings**](msvm-virtualsystemmanagementservice-modifysystemcomponentsettings.md)             | Modifies generic system component settings.<br/>                                                                                                                                                                                             |
| [**ModifySystemSettings**](modifysystemsettings-msvm-virtualsystemmanagementservice.md)                               | Modifies virtual machine settings.<br/>                                                                                                                                                                                                      |
| [**RealizePlannedSystem**](realizeplannedsystem-msvm-virtualsystemmanagementservice.md)                               | Validates the configuration of a planned virtual machine and converts it to a realized virtual machine.<br/>                                                                                                                                 |
| [**RemoveBootSourceSettings**](msvm-virtualsystemmanagementservice-removebootsourcesettings.md)                       | Removes virtual resource settings from a virtual system configuration.<br/> When applied to parts of a "current" virtual system configuration, as a side effect resources of the active virtual system may be removed.<br/>            |
| [**RemoveFeatureSettings**](removefeaturesettings-msvm-virtualsystemmanagementservice.md)                             | Removes feature settings from a virtual machine Ethernet connection.<br/>                                                                                                                                                                    |
| [**RemoveFibreChannelChap**](removefibrechannelchap-msvm-virtualsystemmanagementservice.md)                           | Removes DH-CHAP parameters from a synthetic Fibre Channel port in a virtual machine.<br/>                                                                                                                                                    |
| [**RemoveGuestServiceSettings**](msvm-virtualsystemmanagementservice-removeguestservicesettings.md)                   | Removes guest service settings from a virtual system configuration.<br/> When applied to parts of a "current" virtual system configuration, as a side effect guest services of the active virtual system may be modified.<br/>         |
| [**RemoveKvpItems**](removekvpitems-msvm-virtualsystemmanagementservice.md)                                           | Removes existing key-value pairs from a virtual machine.<br/>                                                                                                                                                                                |
| [**RemoveResourceSettings**](removeresourcesettings-msvm-virtualsystemmanagementservice.md)                           | Removes virtual resource settings from a virtual machine configuration.<br/>                                                                                                                                                                 |
| [**RemoveSystemComponentSettings**](msvm-virtualsystemmanagementservice-removesystemcomponentsettings.md)             | Removes generic component settings from a virtual system configuration.<br/>                                                                                                                                                                 |
| [**RequestStateChange**](msvm-virtualsystemmanagementservice-requeststatechange.md)                                   | This method is not supported.<br/>                                                                                                                                                                                                           |
| [**SetGuestNetworkAdapterConfiguration**](setguestnetworkadapterconfiguration-msvm-virtualsystemmanagementservice.md) | Configures the network adapters within the guest operating system.<br/>                                                                                                                                                                      |
| [**SetInitialMachineConfigurationData**](msvm-virtualsystemmanagementservice-setinitialmachineconfigurationdata.md)   | Sets a VM's initial machine configuration data.<br/>                                                                                                                                                                                         |
| [**StartService**](msvm-virtualsystemmanagementservice-startservice.md)                                               | This method is not supported.<br/>                                                                                                                                                                                                           |
| [**StopService**](msvm-virtualsystemmanagementservice-stopservice.md)                                                 | This method is not supported.<br/>                                                                                                                                                                                                           |
| [**TestNetworkConnection**](msvm-virtualsystemmanagementservice-testnetworkconnection.md)                             | Tests the network connectivity of a VM in a Windows Network Virtualization Environment.<br/>                                                                                                                                                 |
| [**UpgradeSystemVersion**](msvm-virtualsystemmanagementservice-upgradesystemversion.md)                               | Upgrades the virtual system.<br/> When applied to the system settings of a "current" virtual system configuration<br/>                                                                                                                 |
| [**ValidatePlannedSystem**](validateplannedsystem-msvm-virtualsystemmanagementservice.md)                             | Validates the specified planned system.<br/>                                                                                                                                                                                                 |



 

### Properties

The **Msvm\_VirtualSystemManagementService** class has these properties.

<dl> <dt>

**AvailableRequestedStates**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the possible values for the *RequestedState* parameter of the **RequestStateChange** method. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)), and it is always set to **Null**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Hyper-V Virtual System Management Service".

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the ability of the instrumentation to communicate with the underlying managed element. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)
</dt> <dt>

<span id="Communication_OK"></span><span id="communication_ok"></span><span id="COMMUNICATION_OK"></span>**Communication OK** (2)
</dt> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (3)
</dt> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (4)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

The name of the class or subclass used in the creation of an instance. This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service), and it is always set to "Msvm\_VirtualSystemManagementService".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Service for creating, manipulating, and managing virtual machines".

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Compliments the **PrimaryStatus** property with additional status detail. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (0)
</dt> <dt>

<span id="No_Additional_Information"></span><span id="no_additional_information"></span><span id="NO_ADDITIONAL_INFORMATION"></span>**No Additional Information** (1)
</dt> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (2)
</dt> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (3)
</dt> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (4)
</dt> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (5)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Hyper-V Virtual System Management Service".

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An administrator's default or startup configuration for the enabled state of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)), and it is always set to 2 (Enabled).



| Value                                                                        | Meaning            |
|------------------------------------------------------------------------------|--------------------|
| <dl> <dt>2</dt> </dl> | Enabled<br/> |



 

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled and disabled states of an element. This property can also indicate the transitions between these requested states. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)), and it is always set to 2 (Enabled).



| Value                                                                        | Meaning            |
|------------------------------------------------------------------------------|--------------------|
| <dl> <dt>2</dt> </dl> | Enabled<br/> |



 

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely nonfunctional. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and it is always set to 5 (OK).



| Value                                                                        | Meaning                                 |
|------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>5</dt> </dl> | The health status is normal.<br/> |



 

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time the virtual machine configuration was created. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

The label by which the object is known. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and it is always set to "vmms".

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides current status information for the operational condition of the element and can be used for providing more detail with respect to the value of the **EnabledState** property. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)
</dt> <dt>

<span id="Servicing"></span><span id="servicing"></span><span id="SERVICING"></span>**Servicing** (2)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (3)
</dt> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (4)
</dt> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (5)
</dt> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (6)
</dt> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (7)
</dt> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (8)
</dt> <dt>

<span id="Migrating"></span><span id="migrating"></span><span id="MIGRATING"></span>**Migrating** (9)
</dt> <dt>

<span id="Emigrating"></span><span id="emigrating"></span><span id="EMIGRATING"></span>**Emigrating** (10)
</dt> <dt>

<span id="Immigrating"></span><span id="immigrating"></span><span id="IMMIGRATING"></span>**Immigrating** (11)
</dt> <dt>

<span id="Snapshotting"></span><span id="snapshotting"></span><span id="SNAPSHOTTING"></span>**Snapshotting** (12)
</dt> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>**Shutting Down** (13)
</dt> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>**In Test** (14)
</dt> <dt>

<span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span>**Transitioning** (15)
</dt> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (16)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current statuses of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and each array element is always set to 2 (OK).

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 ("Other"). This property must be set to **Null** when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)), and it is always set to **Null**.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 256 )
</dt> </dl>

Any information about how the primary owner of the service can be reached (for example, phone number, email address, and so on). This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service), and it is always set to **Null**.

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

The name of the primary owner for the service, if one is defined. The primary owner is the initial support contact for the service. This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service), and it is always set to **Null**.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides high level status information. This property should be used in conjunction with the **DetailedStatus** property to provide high level and detailed health status of the element and its subcomponents. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (1)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (2)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (3)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current states for an element. A particular instance of the [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)) class might not support the **RequestedState** property. If this occurs, the value 12 ("Not Applicable") is used. This property is inherited from **CIM\_EnabledLogicalElement**, and it is always set to 12 (Not Applicable).



| Value                                                                         | Meaning                    |
|-------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>12</dt> </dl> | Not applicable.<br/> |



 

</dd> <dt>

**Started**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the service is currently running. This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service), and it is always set to **True**.

</dd> <dt>

**StartMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 10 )
</dt> </dl>

A string value that indicates whether the service is automatically started by a system, an operating system, or is started only upon request. This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service), and it is always set to **Null**.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), but it is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and each array element is always set to "The service is running normally".

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

The scoping system's creation class name. This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service), and it is always set to "Msvm\_ComputerSystem".

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** ( 256 )
</dt> </dl>

The NetBIOS name of the hosting computer system. This property is inherited from [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**TransitioningToState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the target state to which the instance is transitioning. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)), and it is always set to **Null**.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemManagementService** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_VirtualSystemManagementService**](/previous-versions//cc136952(v=vs.85))
</dt> <dt>

[**Msvm\_VirtualSystemManagementService (V1)**](/previous-versions/windows/desktop/legacy/cc136940(v=vs.85))
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

