---
description: A logical network adapters.
ms.assetid: 0d09f9e4-abca-4767-8d03-9b59dd2a5f38
title: MSFT\_NetAdapter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter
- MSFT_NetAdapter.Caption
- MSFT_NetAdapter.Description
- MSFT_NetAdapter.InstallDate
- MSFT_NetAdapter.Name
- MSFT_NetAdapter.Status
- MSFT_NetAdapter.Availability
- MSFT_NetAdapter.ConfigManagerErrorCode
- MSFT_NetAdapter.ConfigManagerUserConfig
- MSFT_NetAdapter.CreationClassName
- MSFT_NetAdapter.DeviceID
- MSFT_NetAdapter.ErrorCleared
- MSFT_NetAdapter.ErrorDescription
- MSFT_NetAdapter.LastErrorCode
- MSFT_NetAdapter.PNPDeviceID
- MSFT_NetAdapter.PowerManagementCapabilities
- MSFT_NetAdapter.PowerManagementSupported
- MSFT_NetAdapter.StatusInfo
- MSFT_NetAdapter.SystemCreationClassName
- MSFT_NetAdapter.SystemName
- MSFT_NetAdapter.Speed
- MSFT_NetAdapter.MaxSpeed
- MSFT_NetAdapter.RequestedSpeed
- MSFT_NetAdapter.UsageRestriction
- MSFT_NetAdapter.PortType
- MSFT_NetAdapter.OtherPortType
- MSFT_NetAdapter.OtherNetworkPortType
- MSFT_NetAdapter.PortNumber
- MSFT_NetAdapter.LinkTechnology
- MSFT_NetAdapter.OtherLinkTechnology
- MSFT_NetAdapter.PermanentAddress
- MSFT_NetAdapter.NetworkAddresses
- MSFT_NetAdapter.FullDuplex
- MSFT_NetAdapter.AutoSense
- MSFT_NetAdapter.SupportedMaximumTransmissionUnit
- MSFT_NetAdapter.ActiveMaximumTransmissionUnit
- MSFT_NetAdapter.InterfaceDescription
- MSFT_NetAdapter.InterfaceName
- MSFT_NetAdapter.NetLuid
- MSFT_NetAdapter.InterfaceGuid
- MSFT_NetAdapter.InterfaceIndex
- MSFT_NetAdapter.DeviceName
- MSFT_NetAdapter.NetLuidIndex
- MSFT_NetAdapter.Virtual
- MSFT_NetAdapter.Hidden
- MSFT_NetAdapter.NotUserRemovable
- MSFT_NetAdapter.IMFilter
- MSFT_NetAdapter.InterfaceType
- MSFT_NetAdapter.HardwareInterface
- MSFT_NetAdapter.WdmInterface
- MSFT_NetAdapter.EndPointInterface
- MSFT_NetAdapter.iSCSIInterface
- MSFT_NetAdapter.State
- MSFT_NetAdapter.NdisMedium
- MSFT_NetAdapter.NdisPhysicalMedium
- MSFT_NetAdapter.InterfaceOperationalStatus
- MSFT_NetAdapter.OperationalStatusDownDefaultPortNotAuthenticated
- MSFT_NetAdapter.OperationalStatusDownMediaDisconnected
- MSFT_NetAdapter.OperationalStatusDownInterfacePaused
- MSFT_NetAdapter.OperationalStatusDownLowPowerState
- MSFT_NetAdapter.InterfaceAdminStatus
- MSFT_NetAdapter.MediaConnectState
- MSFT_NetAdapter.MtuSize
- MSFT_NetAdapter.VlanID
- MSFT_NetAdapter.TransmitLinkSpeed
- MSFT_NetAdapter.ReceiveLinkSpeed
- MSFT_NetAdapter.PromiscuousMode
- MSFT_NetAdapter.DeviceWakeUpEnable
- MSFT_NetAdapter.ConnectorPresent
- MSFT_NetAdapter.MediaDuplexState
- MSFT_NetAdapter.DriverDate
- MSFT_NetAdapter.DriverDateData
- MSFT_NetAdapter.DriverVersionString
- MSFT_NetAdapter.DriverName
- MSFT_NetAdapter.DriverDescription
- MSFT_NetAdapter.MajorDriverVersion
- MSFT_NetAdapter.MinorDriverVersion
- MSFT_NetAdapter.DriverMajorNdisVersion
- MSFT_NetAdapter.DriverMinorNdisVersion
- MSFT_NetAdapter.PnPDeviceID
- MSFT_NetAdapter.DriverProvider
- MSFT_NetAdapter.ComponentID
- MSFT_NetAdapter.LowerLayerInterfaceIndices
- MSFT_NetAdapter.HigherLayerInterfaceIndices
- MSFT_NetAdapter.AdminLocked
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter class

A logical network adapters

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter : CIM_NetworkPort
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  uint16   Availability;
  uint32   ConfigManagerErrorCode;
  boolean  ConfigManagerUserConfig;
  string   CreationClassName;
  string   DeviceID;
  boolean  ErrorCleared;
  string   ErrorDescription;
  uint32   LastErrorCode;
  string   PNPDeviceID;
  uint16   PowerManagementCapabilities[];
  boolean  PowerManagementSupported;
  uint16   StatusInfo;
  string   SystemCreationClassName;
  string   SystemName;
  uint64   Speed;
  uint64   MaxSpeed;
  uint64   RequestedSpeed;
  uint16   UsageRestriction;
  uint16   PortType;
  string   OtherPortType;
  string   OtherNetworkPortType;
  uint16   PortNumber;
  uint16   LinkTechnology;
  string   OtherLinkTechnology;
  string   PermanentAddress;
  string   NetworkAddresses[];
  boolean  FullDuplex;
  boolean  AutoSense;
  uint64   SupportedMaximumTransmissionUnit;
  uint64   ActiveMaximumTransmissionUnit;
  string   InterfaceDescription;
  string   InterfaceName;
  uint64   NetLuid;
  string   InterfaceGuid;
  uint32   InterfaceIndex;
  string   DeviceName;
  uint32   NetLuidIndex;
  boolean  Virtual;
  boolean  Hidden;
  boolean  NotUserRemovable;
  boolean  IMFilter;
  uint32   InterfaceType;
  boolean  HardwareInterface;
  boolean  WdmInterface;
  boolean  EndPointInterface;
  boolean  iSCSIInterface;
  uint32   State;
  uint32   NdisMedium;
  uint32   NdisPhysicalMedium;
  uint32   InterfaceOperationalStatus;
  boolean  OperationalStatusDownDefaultPortNotAuthenticated;
  boolean  OperationalStatusDownMediaDisconnected;
  boolean  OperationalStatusDownInterfacePaused;
  boolean  OperationalStatusDownLowPowerState;
  uint32   InterfaceAdminStatus;
  uint32   MediaConnectState;
  uint32   MtuSize;
  uint16   VlanID;
  uint64   TransmitLinkSpeed;
  uint64   ReceiveLinkSpeed;
  boolean  PromiscuousMode;
  boolean  DeviceWakeUpEnable;
  boolean  ConnectorPresent;
  uint32   MediaDuplexState;
  string   DriverDate;
  uint64   DriverDateData;
  string   DriverVersionString;
  string   DriverName;
  string   DriverDescription;
  uint16   MajorDriverVersion;
  uint16   MinorDriverVersion;
  uint8    DriverMajorNdisVersion;
  uint8    DriverMinorNdisVersion;
  string   PnPDeviceID;
  string   DriverProvider;
  string   ComponentID;
  uint32   LowerLayerInterfaceIndices[];
  uint32   HigherLayerInterfaceIndices[];
  boolean  AdminLocked;
};
```

## Members

The **MSFT\_NetAdapter** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapter** class has these methods.



| Method                                     | Description                            |
|:-------------------------------------------|:---------------------------------------|
| [**Disable**](disable-msft-netadapter.md) | Disables a network adapter.<br/> |
| [**Enable**](enable-msft-netadapter.md)   | Enables a network adapter.<br/>  |
| [**Lock**](lock-msft-netadapter.md)       | Locks a network adapter.<br/>    |
| [**Rename**](msft-netadapter-rename.md)   | Renames a network adapter.<br/>  |
| [**Restart**](restart-msft-netadapter.md) | Restarts a network adapter.<br/> |
| [**Unlock**](unlock-msft-netadapter.md)   | Unlocks a network adapter.<br/>  |



 

### Properties

The **MSFT\_NetAdapter** class has these properties.

<dl> <dt>

**ActiveMaximumTransmissionUnit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** ( "Bytes" )
</dt> </dl>

The active or negotiated maximum transmission unit (MTU) that can be supported. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**AdminLocked**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The management state of the network adapter. If True, the network adapter is locked and many of its properties cannot be changed unless the adapter is unlocked.

</dd> <dt>

**AutoSense**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A Boolean that indicates whether the network port is capable of automatically determining the speed or other communications characteristics of the attached network media. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Availability and status of the device. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).



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

Short textual description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**ComponentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The PnP component ID, also known as the Hardware ID of the network adapter.

</dd> <dt>

**ConfigManagerErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Win32 Configuration Manager error code. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).



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

If **TRUE**, the device is using a user-defined configuration. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**ConnectorPresent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a connector is present on the network adapter. This value is set to TRUE if this is a physical adapter or FALSE if this is not a physical adapter.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address or other identifying information to uniquely name the logical device. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**DeviceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the device object for this adapter.

</dd> <dt>

**DeviceWakeUpEnable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TRUE if the network adapter supports wake-on-LAN capability and the capability is enabled, or FALSE if it does not.

</dd> <dt>

**DriverDate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network adapter driver date in YYYY-MM-DD format.

</dd> <dt>

**DriverDateData**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network adapter driver date in FILETIME format. This is a 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601 (UTC).

</dd> <dt>

**DriverDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description for the network adapter driver.

</dd> <dt>

**DriverMajorNdisVersion**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major NDIS version the network adapter driver conforms to.

</dd> <dt>

**DriverMinorNdisVersion**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor NDIS version the network adapter driver conforms to.

</dd> <dt>

**DriverName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the network adapter driver.

</dd> <dt>

**DriverProvider**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The driver provider name.

</dd> <dt>

**DriverVersionString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representing the network adapter driver version.

</dd> <dt>

**EndPointInterface**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This interface is an endpoint device and is not a true network interface that connects to a network.

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the error reported in the **LastErrorCode** property is now cleared. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that supplies information about the error recorded in the **LastErrorCode** property and corrective actions to perform. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**FullDuplex**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean that indicates that the port is operating in full duplex mode. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**HardwareInterface**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interface for the network adapter is provided by a hardware device.

</dd> <dt>

**Hidden**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network adapter is hidden and does not appear in any user interface.

</dd> <dt>

**HigherLayerInterfaceIndices**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interface indices of higher layer interfaces.

</dd> <dt>

**IMFilter**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network adapter is the adapter edge of an intermediate filter component.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/win32/cimwin32prov/cim-managedsystemelement).

</dd> <dt>

**InterfaceAdminStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network adapter administrative status, as described in RFC 2863.

<dl> <dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>**Up** (1)
</dt> <dt>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>**Down** (2)
</dt> <dt>

<span id="Testing_"></span><span id="testing_"></span><span id="TESTING_"></span>**Testing** (3)
</dt> </dl>

</dd> <dt>

**InterfaceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Interface Description, also known as "ifDesc" or display name is a unique name assigned to the network adapter during installation. This name cannot be changed and is persisted as long as the network adapter is not uninstalled.

</dd> <dt>

**InterfaceGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GUID for the network interface.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The index that identifies the network interface. This index value may change when a network adapter is disabled and then enabled, and should not be considered persistent.

</dd> <dt>

**InterfaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The locally unique identifier for the network interface. in InterfaceType\_NetluidIndex format. Ex: Ethernet\_2.

</dd> <dt>

**InterfaceOperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current network interface operational status.

<dl> <dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>**Up** (1)
</dt> <dt>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>**Down** (2)
</dt> <dt>

<span id="Testing"></span><span id="testing"></span><span id="TESTING"></span>**Testing** (3)
</dt> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (4)
</dt> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (5)
</dt> <dt>

<span id="Not_Present"></span><span id="not_present"></span><span id="NOT_PRESENT"></span>**Not Present** (6)
</dt> <dt>

<span id="Lower_layer_down_"></span><span id="lower_layer_down_"></span><span id="LOWER_LAYER_DOWN_"></span>**Lower layer down** (7)
</dt> </dl>

</dd> <dt>

**InterfaceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interface type as defined by the Internet Assigned Names Authority (IANA).

</dd> <dt>

**iSCSIInterface**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interface is used by iSCSI software initiator and is in the paging path.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last error code reported by the logical device. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**LinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration of the types of links. When set to 1 ("Other"), the related property **OtherLinkTechnology** contains a string description of the type of link. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>**Ethernet** (2)
</dt> <dt>

<span id="IB"></span><span id="ib"></span>**IB** (3)
</dt> <dt>

<span id="FC"></span><span id="fc"></span>**FC** (4)
</dt> <dt>

<span id="FDDI"></span><span id="fddi"></span>**FDDI** (5)
</dt> <dt>

<span id="ATM"></span><span id="atm"></span>**ATM** (6)
</dt> <dt>

<span id="Token_Ring"></span><span id="token_ring"></span><span id="TOKEN_RING"></span>**Token Ring** (7)
</dt> <dt>

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>**Frame Relay** (8)
</dt> <dt>

<span id="Infrared"></span><span id="infrared"></span><span id="INFRARED"></span>**Infrared** (9)
</dt> <dt>

<span id="BlueTooth"></span><span id="bluetooth"></span><span id="BLUETOOTH"></span>**BlueTooth** (10)
</dt> <dt>

<span id="Wireless_LAN"></span><span id="wireless_lan"></span><span id="WIRELESS_LAN"></span>**Wireless LAN** (11)
</dt> </dl>

</dd> <dt>

**LowerLayerInterfaceIndices**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interface indices of lower layer interfaces.

</dd> <dt>

**MajorDriverVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major version of network adapter driver.

</dd> <dt>

**MaxSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** ( "Bits per Second" )
</dt> </dl>

The maximum bandwidth, in bits per second, of the port. This property inherits from [**CIM\_LogicalPort**](/previous-versions//cc136869(v=vs.85)).

</dd> <dt>

**MediaConnectState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the network adapter connection state.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Connected"></span><span id="connected"></span><span id="CONNECTED"></span>**Connected** (1)
</dt> <dt>

<span id="Disconnected_"></span><span id="disconnected_"></span><span id="DISCONNECTED_"></span>**Disconnected** (2)
</dt> </dl>

</dd> <dt>

**MediaDuplexState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The media duplex state of the network adapter.

</dd> <dt>

**MinorDriverVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor version of network adapter driver.

</dd> <dt>

**MtuSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum transfer unit (MTU) size the network adapter supports. This value does not include the size of the link-layer header.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/win32/cimwin32prov/cim-managedsystemelement).

</dd> <dt>

**NdisMedium**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network adapter media type.

<dl> <dt>

<span id="802.3"></span>**802.3** (0)
</dt> <dt>

<span id="802.5"></span>**802.5** (1)
</dt> <dt>

<span id="FDDI"></span><span id="fddi"></span>**FDDI** (2)
</dt> <dt>

<span id="WAN"></span><span id="wan"></span>**WAN** (3)
</dt> <dt>

<span id="Local_Talk"></span><span id="local_talk"></span><span id="LOCAL_TALK"></span>**Local Talk** (4)
</dt> <dt>

<span id="DIX"></span><span id="dix"></span>**DIX** (5)
</dt> <dt>

<span id="Raw_Arcnet"></span><span id="raw_arcnet"></span><span id="RAW_ARCNET"></span>**Raw Arcnet** (6)
</dt> <dt>

<span id="878.2"></span>**878.2** (7)
</dt> <dt>

<span id="ATM"></span><span id="atm"></span>**ATM** (8)
</dt> <dt>

<span id="Wireless_WAN"></span><span id="wireless_wan"></span><span id="WIRELESS_WAN"></span>**Wireless WAN** (9)
</dt> <dt>

<span id="IRDA"></span><span id="irda"></span>**IRDA** (10)
</dt> <dt>

<span id="BPC"></span><span id="bpc"></span>**BPC** (11)
</dt> <dt>

<span id="Connection_Oriented_WAN"></span><span id="connection_oriented_wan"></span><span id="CONNECTION_ORIENTED_WAN"></span>**Connection Oriented WAN** (12)
</dt> <dt>

<span id="IP_1394"></span><span id="ip_1394"></span>**IP 1394** (13)
</dt> <dt>

<span id="IB"></span><span id="ib"></span>**IB** (14)
</dt> <dt>

<span id="Tunnel"></span><span id="tunnel"></span><span id="TUNNEL"></span>**Tunnel** (15)
</dt> <dt>

<span id="Native_802.11"></span><span id="native_802.11"></span><span id="NATIVE_802.11"></span>**Native 802.11** (16)
</dt> <dt>

<span id="Loopback"></span><span id="loopback"></span><span id="LOOPBACK"></span>**Loopback** (17)
</dt> <dt>

<span id="WiMAX"></span><span id="wimax"></span><span id="WIMAX"></span>**WiMAX** (18)
</dt> <dt>

<span id="IP_"></span><span id="ip_"></span>**IP** (19)
</dt> </dl>

</dd> <dt>

**NdisPhysicalMedium**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The types of physical media that the network adapter supports.

<dl> <dt>

<span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span>**Unspecified** (0)
</dt> <dt>

<span id="Wireless_LAN"></span><span id="wireless_lan"></span><span id="WIRELESS_LAN"></span>**Wireless LAN** (1)
</dt> <dt>

<span id="Cable_Modem"></span><span id="cable_modem"></span><span id="CABLE_MODEM"></span>**Cable Modem** (2)
</dt> <dt>

<span id="Phone_Line"></span><span id="phone_line"></span><span id="PHONE_LINE"></span>**Phone Line** (3)
</dt> <dt>

<span id="Power_Line"></span><span id="power_line"></span><span id="POWER_LINE"></span>**Power Line** (4)
</dt> <dt>

<span id="DSL"></span><span id="dsl"></span>**DSL** (5)
</dt> <dt>

<span id="FC"></span><span id="fc"></span>**FC** (6)
</dt> <dt>

<span id="1394"></span>**1394** (7)
</dt> <dt>

<span id="Wireless_WAN"></span><span id="wireless_wan"></span><span id="WIRELESS_WAN"></span>**Wireless WAN** (8)
</dt> <dt>

<span id="Native_802.11"></span><span id="native_802.11"></span><span id="NATIVE_802.11"></span>**Native 802.11** (9)
</dt> <dt>

<span id="BlueTooth"></span><span id="bluetooth"></span><span id="BLUETOOTH"></span>**BlueTooth** (10)
</dt> <dt>

<span id="Infiniband"></span><span id="infiniband"></span><span id="INFINIBAND"></span>**Infiniband** (11)
</dt> <dt>

<span id="WiMAX"></span><span id="wimax"></span><span id="WIMAX"></span>**WiMAX** (12)
</dt> <dt>

<span id="UWB"></span><span id="uwb"></span>**UWB** (13)
</dt> <dt>

<span id="802.3"></span>**802.3** (14)
</dt> <dt>

<span id="802.5"></span>**802.5** (15)
</dt> <dt>

<span id="IRDA"></span><span id="irda"></span>**IRDA** (16)
</dt> <dt>

<span id="Wired_WAN"></span><span id="wired_wan"></span><span id="WIRED_WAN"></span>**Wired WAN** (17)
</dt> <dt>

<span id="Wired_Connection_Oriented_WAN"></span><span id="wired_connection_oriented_wan"></span><span id="WIRED_CONNECTION_ORIENTED_WAN"></span>**Wired Connection Oriented WAN** (18)
</dt> <dt>

<span id="Other_"></span><span id="other_"></span><span id="OTHER_"></span>**Other** (19)
</dt> </dl>

</dd> <dt>

**NetLuid**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The locally unique identifier (LUID) for the network interface as a 64 bit number.

</dd> <dt>

**NetLuidIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An index assigned to the network adapter at the time of installation.This index is unique in the scope of interface type.

</dd> <dt>

**NetworkAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

An array of strings that indicates the network addresses for the port. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**NotUserRemovable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network adapter cannot be removed by the user.

</dd> <dt>

**OperationalStatusDownDefaultPortNotAuthenticated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The default port of the network adapter is not authenticated.

</dd> <dt>

**OperationalStatusDownInterfacePaused**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network adapter is in the paused state.

</dd> <dt>

**OperationalStatusDownLowPowerState**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network adapter is in a low power state.

</dd> <dt>

**OperationalStatusDownMediaDisconnected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network adapter is not in a media-connected state.

</dd> <dt>

**OtherLinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string value that describes **LinkTechnology** when it is set to 1, "Other". This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**OtherNetworkPortType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Note: The use of this property is deprecated in lieu of CIM\_LogicalPort.PortType. Deprecated description: The type of module, when PortType is set to 1 ("Other".) This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**OtherPortType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Describes the type of module, when **PortType** is set to 1 ("Other"). This property inherits from [**CIM\_LogicalPort**](/previous-versions//cc136869(v=vs.85)).

</dd> <dt>

**PermanentAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

The network address that is hardcoded into a port. This hardcoded address can be changed using a firmware upgrade or a software configuration. When this change is made, the field should be updated at the same time. **PermanentAddress** should be left blank if no hardcoded address exists for the network adapter. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**PnPDeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Plug and Play Device ID.

</dd> <dt>

**PNPDeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the Win32 Plug and Play device identifier of the logical device. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

Example: "\*PNP030b"

</dd> <dt>

**PortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network ports are often numbered relative to either a logical module or a network element. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**PortType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Forces consistent naming of the 'type' property in subclasses and to guarantee unique enum values for all instances of NetworkPort. When set to 1 ("Other"), related property OtherPortType contains a string description of the type of port. A range of values, DMTF\_Reserved, has been defined that allows subclasses to override and define their specific types of ports. This property inherits from [**CIM\_LogicalPort**](/previous-versions//cc136869(v=vs.85)).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (2)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (3..15999)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (16000..65535)
</dt> </dl>

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of the specific power-related capabilities of a logical device. This property is inherited from **CIM\_LogicalDevice**. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).



| Value                                                                                                                                                                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0 (0x0)</dt> </dl>                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                      |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>1 (0x1)</dt> </dl>                                                                                                             |                                                                                                                                                                                                                                                                                                                                      |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>2 (0x2)</dt> </dl>                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                      |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>3 (0x3)</dt> </dl>                                                                                                                                     | The power management features are currently enabled but the exact feature set is unknown or the information is unavailable.<br/>                                                                                                                                                                                               |
| <span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span><dl> <dt>**Power Saving Modes Entered Automatically**</dt> <dt>4 (0x4)</dt> </dl> | The device can change its power state based on usage or other criteria.<br/>                                                                                                                                                                                                                                                   |
| <span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span><dl> <dt>**Power State Settable**</dt> <dt>5 (0x5)</dt> </dl>                                                                                 | The [**SetPowerState**](/windows/win32/cimwin32prov/setpowerstate-method-in-class-cim-controller) method is supported. This method is found on the parent **CIM\_LogicalDevice** class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes](/windows/win32/wmisdk/designing-managed-object-format--mof--classes).<br/> |
| <span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span><dl> <dt>**Power Cycling Supported**</dt> <dt>6 (0x6)</dt> </dl>                                                                     | The [**SetPowerState**](/windows/win32/cimwin32prov/setpowerstate-method-in-class-cim-controller) method can be invoked with the *PowerState* parameter set to 5 ("Power Cycle").<br/>                                                                                                                                                            |
| <span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span><dl> <dt>**Timed Power On Supported**</dt> <dt>7 (0x7)</dt> </dl>                                                                 | The [**SetPowerState**](/windows/win32/cimwin32prov/setpowerstate-method-in-class-cim-controller) method can be invoked with the *PowerState*parameter set to 5 ("Power Cycle") and *Time* set to a specific date and time, or interval, for power-on.<br/>                                                                                       |



 

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the device can be power managed, that is, put into a power-save state. If **FALSE**, the integer value 1 ("Not Supported") should be the only entry in the **PowerManagementCapabilities** array.

This property does not indicate whether power management features are currently enabled, or if enabled, which features are supported. For more information, see the **PowerManagementCapabilities** array.

This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**PromiscuousMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TRUE if the interface is in promiscuous mode or FALSE if it is not.

</dd> <dt>

**ReceiveLinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The receive link speed in bits per second.

</dd> <dt>

**RequestedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Write-only
</dt> <dt>

Qualifiers: **Units** ( "Bits per Second" )
</dt> </dl>

The requested bandwidth, in bits per second, of the port. The actual bandwidth is reported in the **Speed** property. This property inherits from [**CIM\_LogicalPort**](/previous-versions//cc136869(v=vs.85)).

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** ( "Bits per Second" )
</dt> </dl>

The bandwidth, in bits per second, of the port. This property inherits from [**CIM\_LogicalPort**](/previous-versions//cc136869(v=vs.85)).

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The plug and play state of the network adapter.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Present"></span><span id="present"></span><span id="PRESENT"></span>**Present** (1)
</dt> <dt>

<span id="Started"></span><span id="started"></span><span id="STARTED"></span>**Started** (2)
</dt> <dt>

<span id="Disabled_"></span><span id="disabled_"></span><span id="DISABLED_"></span>**Disabled** (3)
</dt> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/win32/cimwin32prov/cim-managedsystemelement).

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

State of the logical device. If this property does not apply to the logical device, the value 5 ("Not Applicable") should be used. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

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

**SupportedMaximumTransmissionUnit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** ( "Bytes" )
</dt> </dl>

The maximum transmission unit (MTU) that can be supported. This property inherits from [**CIM\_NetworkPort**](/previous-versions/cc136873(v=vs.85)).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scoping system's creation class name. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scoping system's name. This property inherits from [**CIM\_LogicalDevice**](/windows/win32/cimwin32prov/cim-logicaldevice).

</dd> <dt>

**TransmitLinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The transmit link speed in bits per second.

</dd> <dt>

**UsageRestriction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Write-only
</dt> </dl>

In some cases, a logical port might be identifiable as a front end or back end port. An example of this situation would be a storage array that might have back end ports to communicate with disk drives and front end ports to communicate with hosts. If there is no restriction on the use of the port, then the value should be set to 'not restricted'. This property inherits from [**CIM\_LogicalPort**](/previous-versions//cc136869(v=vs.85)).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Front-end_only"></span><span id="front-end_only"></span><span id="FRONT-END_ONLY"></span>**Front-end only** (2)
</dt> <dt>

<span id="Back-end_only"></span><span id="back-end_only"></span><span id="BACK-END_ONLY"></span>**Back-end only** (3)
</dt> <dt>

<span id="Not_restricted"></span><span id="not_restricted"></span><span id="NOT_RESTRICTED"></span>**Not restricted** (4)
</dt> </dl>

</dd> <dt>

**Virtual**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network adapter emulates a physical network card.

</dd> <dt>

**VlanID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Virtual LAN Identifier set on the network adapter.

</dd> <dt>

**WdmInterface**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The lower-level interface of the network adapter is a WDM bus driver such as USB.

</dd> </dl>

## Remarks

The **MSFT\_NetAdapter** class is commonly used with the [Network Adapter Cmdlets](/powershell/module/netadapter/).

## Examples

The following PowerShell example retrieves a local MSFT\_NetAdapter with the specified device ID.


```PowerShell
$deviceID = "{11111111-2222-3333-4444-555555555555}"
Get-WmiObject -ComputerName "." -Namespace Root\StandardCimv2 -class MSFT_NetAdapter | Where-Object {$_.DeviceID -eq $deviceID}
```



## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

