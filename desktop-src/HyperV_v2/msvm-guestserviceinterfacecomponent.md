---
description: Represents the state of the guest service interface component, which provides a mechanism to interact with the virtual machine from the management interfaces on the host system.
ms.assetid: 9A158B42-052B-42B3-8539-00927056306D
title: Msvm_GuestServiceInterfaceComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_GuestServiceInterfaceComponent
- Msvm_GuestServiceInterfaceComponent.Availability
- Msvm_GuestServiceInterfaceComponent.Caption
- Msvm_GuestServiceInterfaceComponent.ConfigManagerErrorCode
- Msvm_GuestServiceInterfaceComponent.ConfigManagerUserConfig
- Msvm_GuestServiceInterfaceComponent.CreationClassName
- Msvm_GuestServiceInterfaceComponent.Description
- Msvm_GuestServiceInterfaceComponent.DeviceID
- Msvm_GuestServiceInterfaceComponent.ErrorCleared
- Msvm_GuestServiceInterfaceComponent.ErrorDescription
- Msvm_GuestServiceInterfaceComponent.InstallDate
- Msvm_GuestServiceInterfaceComponent.LastErrorCode
- Msvm_GuestServiceInterfaceComponent.Name
- Msvm_GuestServiceInterfaceComponent.PNPDeviceID
- Msvm_GuestServiceInterfaceComponent.PowerManagementCapabilities
- Msvm_GuestServiceInterfaceComponent.PowerManagementSupported
- Msvm_GuestServiceInterfaceComponent.Status
- Msvm_GuestServiceInterfaceComponent.StatusInfo
- Msvm_GuestServiceInterfaceComponent.SystemCreationClassName
- Msvm_GuestServiceInterfaceComponent.SystemName
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_GuestServiceInterfaceComponent class

Represents the state of the guest service interface component, which provides a mechanism to interact with the virtual machine from the management interfaces on the host system. This class derives from the [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_GuestServiceInterfaceComponent : CIM_LogicalDevice
{
  uint16   Availability;
  string   Caption;
  uint32   ConfigManagerErrorCode;
  boolean  ConfigManagerUserConfig;
  string   CreationClassName;
  string   Description;
  string   DeviceID;
  boolean  ErrorCleared;
  string   ErrorDescription;
  datetime InstallDate;
  uint32   LastErrorCode;
  string   Name;
  string   PNPDeviceID;
  uint16   PowerManagementCapabilities[];
  boolean  PowerManagementSupported;
  string   Status;
  uint16   StatusInfo;
  string   SystemCreationClassName;
  string   SystemName;
};
```

## Members

The **Msvm\_GuestServiceInterfaceComponent** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_GuestServiceInterfaceComponent** class has these methods.



| Method                                                                               | Description                                                                                                                              |
|:-------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestStateChange**](requeststatechange-msvm-guestserviceinterfacecomponent.md) | Requests that the state of the guest service interface component be changed to the specified value.<br/>                           |
| [**Reset**](/windows/desktop/CIMWin32Prov/reset-method-in-class-cim-logicaldevice)                        | Requests a reset of the logical device. Not implemented by WMI.<br/>                                                               |
| [**SetPowerState**](/windows/desktop/CIMWin32Prov/setpowerstate-method-in-class-cim-logicaldevice)        | Defines the desired power state for a logical device and when a device should be put into that state. Not implemented by WMI.<br/> |



 

### Properties

The **Msvm\_GuestServiceInterfaceComponent** class has these properties.

<dl> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Availability and status of the device.



| Value                                                                                                                                                                                                                                                                                                              | Meaning                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1 (0x1)</dt> </dl>                                                                                          |                                                                                                             |
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>2 (0x2)</dt> </dl>                                                                                  |                                                                                                             |
| <span id="Running_Full_Power"></span><span id="running_full_power"></span><span id="RUNNING_FULL_POWER"></span><dl> <dt>**Running/Full Power**</dt> <dt>3 (0x3)</dt> </dl>                                      |                                                                                                             |
| <span id="Warning"></span><span id="warning"></span><span id="WARNING"></span><dl> <dt>**Warning**</dt> <dt>4 (0x4)</dt> </dl>                                                                                  |                                                                                                             |
| <span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span><dl> <dt>**In Test**</dt> <dt>5 (0x5)</dt> </dl>                                                                                  |                                                                                                             |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span><dl> <dt>**Not Applicable**</dt> <dt>6 (0x6)</dt> </dl>                                                      |                                                                                                             |
| <span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span><dl> <dt>**Power Off**</dt> <dt>7 (0x7)</dt> </dl>                                                                          |                                                                                                             |
| <span id="Off_Line"></span><span id="off_line"></span><span id="OFF_LINE"></span><dl> <dt>**Off Line**</dt> <dt>8 (0x8)</dt> </dl>                                                                              |                                                                                                             |
| <span id="Off_Duty"></span><span id="off_duty"></span><span id="OFF_DUTY"></span><dl> <dt>**Off Duty**</dt> <dt>9 (0x9)</dt> </dl>                                                                              |                                                                                                             |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>10 (0xA)</dt> </dl>                                                                             |                                                                                                             |
| <span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span><dl> <dt>**Not Installed**</dt> <dt>11 (0xB)</dt> </dl>                                                         |                                                                                                             |
| <span id="Install_Error"></span><span id="install_error"></span><span id="INSTALL_ERROR"></span><dl> <dt>**Install Error**</dt> <dt>12 (0xC)</dt> </dl>                                                         |                                                                                                             |
| <span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span><dl> <dt>**Power Save - Unknown**</dt> <dt>13 (0xD)</dt> </dl>                             | The device is known to be in a power save mode, but its exact status is unknown.<br/>                 |
| <span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span><dl> <dt>**Power Save - Low Power Mode**</dt> <dt>14 (0xE)</dt> </dl> | The device is in a power save state but still functioning, and may exhibit degraded performance.<br/> |
| <span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span><dl> <dt>**Power Save - Standby**</dt> <dt>15 (0xF)</dt> </dl>                             | The device is not functioning but could be brought to full power quickly.<br/>                        |
| <span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span><dl> <dt>**Power Cycle**</dt> <dt>16 (0x10)</dt> </dl>                                                                |                                                                                                             |
| <span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span><dl> <dt>**Power Save - Warning**</dt> <dt>17 (0x11)</dt> </dl>                            | The device is in a warning state, though also in a power save mode.<br/>                              |



 

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**ConfigManagerErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Win32 Configuration Manager error code.



| Value                                                                                | Meaning                                                                                                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl>   | Device is working properly.<br/>                                                                                                   |
| <dl> <dt>1 (0x1)</dt> </dl>   | Device is not configured correctly.<br/>                                                                                           |
| <dl> <dt>2 (0x2)</dt> </dl>   | Windows cannot load the driver for this device.<br/>                                                                               |
| <dl> <dt>3 (0x3)</dt> </dl>   | Driver for this device might be corrupted, or the system may be low on memory or other resources.<br/>                             |
| <dl> <dt>4 (0x4)</dt> </dl>   | Device is not working properly. One of its drivers or the registry might be corrupted.<br/>                                        |
| <dl> <dt>5 (0x5)</dt> </dl>   | Driver for the device requires a resource that Windows cannot manage.<br/>                                                         |
| <dl> <dt>6 (0x6)</dt> </dl>   | Boot configuration for the device conflicts with other devices.<br/>                                                               |
| <dl> <dt>7 (0x7)</dt> </dl>   | Cannot filter.<br/>                                                                                                                |
| <dl> <dt>8 (0x8)</dt> </dl>   | Driver loader for the device is missing.<br/>                                                                                      |
| <dl> <dt>9 (0x9)</dt> </dl>   | Device is not working properly; the controlling firmware is incorrectly reporting the resources for the device.<br/>               |
| <dl> <dt>10 (0xA)</dt> </dl>  | Device cannot start.<br/>                                                                                                          |
| <dl> <dt>11 (0xB)</dt> </dl>  | Device failed.<br/>                                                                                                                |
| <dl> <dt>12 (0xC)</dt> </dl>  | Device cannot find enough free resources to use.<br/>                                                                              |
| <dl> <dt>13 (0xD)</dt> </dl>  | Windows cannot verify the device's resources.<br/>                                                                                 |
| <dl> <dt>14 (0xE)</dt> </dl>  | Device cannot work properly until the computer is restarted.<br/>                                                                  |
| <dl> <dt>15 (0xF)</dt> </dl>  | Device is not working properly due to a possible re-enumeration problem.<br/>                                                      |
| <dl> <dt>16 (0x10)</dt> </dl> | Windows cannot identify all of the resources that the device uses.<br/>                                                            |
| <dl> <dt>17 (0x11)</dt> </dl> | Device is requesting an unknown resource type.<br/>                                                                                |
| <dl> <dt>18 (0x12)</dt> </dl> | Device drivers must be reinstalled.<br/>                                                                                           |
| <dl> <dt>19 (0x13)</dt> </dl> | Failure using the VxD loader.<br/>                                                                                                 |
| <dl> <dt>20 (0x14)</dt> </dl> | Registry might be corrupted.<br/>                                                                                                  |
| <dl> <dt>21 (0x15)</dt> </dl> | System failure. If changing the device driver is ineffective, see the hardware documentation. Windows is removing the device.<br/> |
| <dl> <dt>22 (0x16)</dt> </dl> | Device is disabled.<br/>                                                                                                           |
| <dl> <dt>23 (0x17)</dt> </dl> | System failure. If changing the device driver is ineffective, see the hardware documentation.<br/>                                 |
| <dl> <dt>24 (0x18)</dt> </dl> | Device is not present, not working properly, or does not have all of its drivers installed.<br/>                                   |
| <dl> <dt>25 (0x19)</dt> </dl> | Windows is still setting up the device.<br/>                                                                                       |
| <dl> <dt>26 (0x1A)</dt> </dl> | Windows is still setting up the device.<br/>                                                                                       |
| <dl> <dt>27 (0x1B)</dt> </dl> | Device does not have valid log configuration.<br/>                                                                                 |
| <dl> <dt>28 (0x1C)</dt> </dl> | Device drivers are not installed.<br/>                                                                                             |
| <dl> <dt>29 (0x1D)</dt> </dl> | Device is disabled; the device firmware did not provide the required resources.<br/>                                               |
| <dl> <dt>30 (0x1E)</dt> </dl> | Device is using an IRQ resource that another device is using.<br/>                                                                 |
| <dl> <dt>31 (0x1F)</dt> </dl> | Device is not working properly; Windows cannot load the required device drivers.<br/>                                              |



 

</dd> <dt>

**ConfigManagerUserConfig**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the device is using a user-defined configuration.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address or other identifying information to uniquely name the logical device.

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the error reported in the **LastErrorCode** property is now cleared.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that supplies information about the error recorded in the **LastErrorCode** property and corrective actions to perform.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last error code reported by the logical device.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**PNPDeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the Win32 Plug and Play device identifier of the logical device.

Example: "\*PNP030b"

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of the specific power-related capabilities of a logical device. This property is inherited from **CIM\_LogicalDevice**.



| Value                                                                                                                                                                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0 (0x0)</dt> </dl>                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                      |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>1 (0x1)</dt> </dl>                                                                                                             |                                                                                                                                                                                                                                                                                                                                      |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>2 (0x2)</dt> </dl>                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                      |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>3 (0x3)</dt> </dl>                                                                                                                                     | The power management features are currently enabled but the exact feature set is unknown or the information is unavailable.<br/>                                                                                                                                                                                               |
| <span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span><dl> <dt>**Power Saving Modes Entered Automatically**</dt> <dt>4 (0x4)</dt> </dl> | The device can change its power state based on usage or other criteria.<br/>                                                                                                                                                                                                                                                   |
| <span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span><dl> <dt>**Power State Settable**</dt> <dt>5 (0x5)</dt> </dl>                                                                                 | The [**SetPowerState**](/windows/desktop/CIMWin32Prov/setpowerstate-method-in-class-cim-controller) method is supported. This method is found on the parent **CIM\_LogicalDevice** class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes](/windows/desktop/WmiSdk/designing-managed-object-format--mof--classes).<br/> |
| <span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span><dl> <dt>**Power Cycling Supported**</dt> <dt>6 (0x6)</dt> </dl>                                                                     | The [**SetPowerState**](/windows/desktop/CIMWin32Prov/setpowerstate-method-in-class-cim-controller) method can be invoked with the *PowerState* parameter set to 5 ("Power Cycle").<br/>                                                                                                                                                            |
| <span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span><dl> <dt>**Timed Power On Supported**</dt> <dt>7 (0x7)</dt> </dl>                                                                 | The [**SetPowerState**](/windows/desktop/CIMWin32Prov/setpowerstate-method-in-class-cim-controller) method can be invoked with the *PowerState*parameter set to 5 ("Power Cycle") and *Time* set to a specific date and time, or interval, for power-on.<br/>                                                                                       |



 

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the device can be power managed, that is, put into a power-save state. If **FALSE**, the integer value 1 ("Not Supported") should be the only entry in the **PowerManagementCapabilities** array.

This property does not indicate whether power management features are currently enabled, or if enabled, which features are supported. For more information, see the **PowerManagementCapabilities** array.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

Values include the following:

<dl><span id="OK"></span><span id="ok"></span><dt>

**"OK"**
</dt><span id="Error"></span><span id="error"></span><span id="ERROR"></span><dt>

**"Error"**
</dt><span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dt>

**"Degraded"**
</dt><span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dt>

**"Unknown"**
</dt><span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span><dt>

**"Pred Fail"**
</dt><span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dt>

**"Starting"**
</dt><span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dt>

**"Stopping"**
</dt><span id="Service"></span><span id="service"></span><span id="SERVICE"></span><dt>

**"Service"**
</dt><span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dt>

**"Stressed"**
</dt><span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span><dt>

**"NonRecover"**
</dt><span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dt>

**"No Contact"**
</dt><span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span><dt>

**"Lost Comm"**
</dt> </dl>

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State of the logical device. If this property does not apply to the logical device, the value 5 ("Not Applicable") should be used. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice).

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1 (0x1))
</dt> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2 (0x2))
</dt> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (3 (0x3))
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (4 (0x4))
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (5 (0x5))
</dt> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scoping system's creation class name.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scoping system's name.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> <dt>

[**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice)
</dt> </dl>

 

