---
title: MSCluster\_NetworkInterface class
description: A dynamic WMI class that represents a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd9669a77-9eae-41e5-86c2-74a62e63ee4d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_NetworkInterface class", "MSCluster_NetworkInterface class, described"]
---

# MSCluster\_NetworkInterface class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [network interface](https://msdn.microsoft.com/library/aa371519).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{3DE393F8-8FD5-4426-901D-8EE017003A61}"), AMENDMENT]
class MSCluster_NetworkInterface : CIM_LogicalDevice
{
  string             Caption;
  string             Status;
  datetime           InstallDate;
  string             SystemCreationClassName;
  string             SystemName;
  string             CreationClassName;
  string             DeviceID;
  boolean            PowerManagementSupported;
  uint16             PowerManagementCapabilities[];
  uint16             Availability;
  uint32             ConfigManagerErrorCode;
  boolean            ConfigManagerUserConfig;
  string             PNPDeviceID;
  uint16             StatusInfo;
  uint32             LastErrorCode;
  string             ErrorDescription;
  boolean            ErrorCleared;
  string             OtherIdentifyingInfo[];
  uint64             PowerOnHours;
  uint64             TotalPowerOnHours;
  string             IdentifyingDescriptions[];
  string             Name;
  string             Description;
  string             Adapter;
  string             AdapterId;
  string             Node;
  string             Address;
  string             Network;
  uint32             State;
  uint32             Flags;
  uint32             Characteristics;
  string             IPv6Addresses[];
  string             IPv4Addresses[];
  boolean            DhcpEnabled;
  MSCluster_Property PrivateProperties;
  string             Id;
};
```

## Members

The **MSCluster\_NetworkInterface** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_NetworkInterface** class has these methods.



| Method                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnableDevice**](mscluster-networkinterface-enabledevice.md)                                     | Requests that the LogicalDevice be enabled ("Enabled" input parameter = **TRUE**) or disabled (= **FALSE**). If successful, the Device's **StatusInfo** property should also reflect the desired state (enabled/disabled). The return code should be 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a **ValueMap** qualifier on the method. The strings to which the **ValueMap** contents are 'translated' may also be specified in the subclass as a **Values** array qualifier.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**ExecuteNetworkInterfaceControl**](mscluster-networkinterface-executenetworkinterfacecontrol.md) | Executes a control code on the network interface.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**Reset**](mscluster-networkinterface-reset.md)                                                   | Requests a reset of the LogicalDevice. The return value should be 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a **ValueMap** qualifier on the method. The strings to which the **ValueMap** contents are 'translated' may also be specified in the subclass as a **Values** array qualifier.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**SetPowerState**](mscluster-networkinterface-setpowerstate.md)                                   | [**SetPowerState**](mscluster-networkinterface-setpowerstate.md) defines the desired power state for a LogicalDevice and when a Device should be put into that state. The desired power state is specified by setting the *PowerState* parameter to one of the following integer values: 1="Full Power", 2="Power Save - Low Power Mode", 3="Power Save - Standby", 4="Power Save - Other", 5="Power Cycle" or 6="Power Off". The *Time* parameter (for all state changes but 5, "Power Cycle") indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). When the *PowerState* parameter is equal to 5, **Power Cycle**, the *Time* parameter indicates when the Device should power on again. **Power Off** (6) is immediate. **SetPowerState** should return 0 if successful, 1 if the specified *PowerState* and *Time* request is not supported, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a **ValueMap** qualifier on the method. The strings to which the **ValueMap** contents are 'translated' may also be specified in the subclass as a **Values** array qualifier.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/> |



 

### Properties

The **MSCluster\_NetworkInterface** class has these properties.

<dl> <dt>

**Adapter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the name that is used to uniquely identify the network interface in the cluster.

</dd> <dt>

**AdapterId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a unique ID for the network interface.

</dd> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the primary network address that the node uses for the network interface.

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|004.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus", "MIF.DMTF\|Host Device\|001.5")
</dt> </dl>

The availability and status of the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884). The following are the possible values.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1 (0x1))


</dt> <dd>

The network interface availability is in another state.

</dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2 (0x2))


</dt> <dd>

The network interface availability is unknown.

</dd> <dt>

<span id="Running_Full_Power"></span><span id="running_full_power"></span><span id="RUNNING_FULL_POWER"></span>

<span id="Running_Full_Power"></span><span id="running_full_power"></span><span id="RUNNING_FULL_POWER"></span>**Running/Full Power** (3 (0x3))


</dt> <dd>

The network interface is available at full power.

</dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (4 (0x4))


</dt> <dd>

The network interface is in a warning state.

</dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>**In Test** (5 (0x5))


</dt> <dd>

The network interface is in a test state.

</dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (6 (0x6))


</dt> <dd>

The network interface availability is not applicable.

</dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>**Power Off** (7 (0x7))


</dt> <dd>

The network interface is powered off.

</dd> <dt>

<span id="Off_Line"></span><span id="off_line"></span><span id="OFF_LINE"></span>

<span id="Off_Line"></span><span id="off_line"></span><span id="OFF_LINE"></span>**Off Line** (8 (0x8))


</dt> <dd>

The network interface is offline.

</dd> <dt>

<span id="Off_Duty"></span><span id="off_duty"></span><span id="OFF_DUTY"></span>

<span id="Off_Duty"></span><span id="off_duty"></span><span id="OFF_DUTY"></span>**Off Duty** (9 (0x9))


</dt> <dd>

The network interface is off duty.

</dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (10 (0xA))


</dt> <dd>

The network interface availability is degraded.

</dd> <dt>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>**Not Installed** (11 (0xB))


</dt> <dd>

The network interface is not installed.

</dd> <dt>

<span id="Install_Error"></span><span id="install_error"></span><span id="INSTALL_ERROR"></span>

<span id="Install_Error"></span><span id="install_error"></span><span id="INSTALL_ERROR"></span>**Install Error** (12 (0xC))


</dt> <dd>

The network interface is not installed properly.

</dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>**Power Save - Unknown** (13 (0xD))


</dt> <dd>

The network interface availability is known to be in a power save mode, but its exact status is unknown.

</dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>**Power Save - Low Power Mode** (14 (0xE))


</dt> <dd>

The network interface is in a power save state but still functioning, and may exhibit degraded performance.

</dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>**Power Save - Standby** (15 (0xF))


</dt> <dd>

The network interface is not functioning but could be brought to full power quickly.

</dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>**Power Cycle** (16 (0x10))


</dt> <dd>

The network interface is being power cycled.

</dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>**Power Save - Warning** (17 (0x11))


</dt> <dd>

The network interface is in a warning state but also in a power save mode.

</dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused** (18 (0x12))


</dt> <dd>

The network interface is paused.

</dd> <dt>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>**Not Ready** (19 (0x13))


</dt> <dd>

The network interface is not ready.

</dd> <dt>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>**Not Configured** (20 (0x14))


</dt> <dd>

The network interface is not configured.

</dd> <dt>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>**Quiesced** (21 (0x15))


</dt> <dd>

The network interface is quiesced.

</dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Provides a short textual description of the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the characteristics set for the network interface. For a list of possible characteristics, see [CLUSCTL\_NETINTERFACE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367258).

</dd> <dt>

**ConfigManagerErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Read**, **Schema** ("Win32")
</dt> </dl>

Indicates the Win32 Configuration Manager error code.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884). The following are the possible values.

<dt>

0 (0x0)
</dt> <dd>

The network interface is working properly.

</dd> <dt>

1 (0x1)
</dt> <dd>

The network interface is not configured correctly.

</dd> <dt>

2 (0x2)
</dt> <dd>

Windows cannot load the driver for the network interface.

</dd> <dt>

3 (0x3)
</dt> <dd>

The driver for the network interface might be corrupted, or the system may be low on memory or other resources.

</dd> <dt>

4 (0x4)
</dt> <dd>

The network interface is not working properly. One of its drivers or the registry might be corrupted.

</dd> <dt>

5 (0x5)
</dt> <dd>

The driver for the network interface requires a resource that Windows cannot manage.

</dd> <dt>

6 (0x6)
</dt> <dd>

Boot configuration for the network interface conflicts with other devices.

</dd> <dt>

7 (0x7)
</dt> <dd>

Cannot filter.

</dd> <dt>

8 (0x8)
</dt> <dd>

The driver loader for the network interface is missing.

</dd> <dt>

9 (0x9)
</dt> <dd>

The network interface is not working properly; the controlling firmware is incorrectly reporting the resources for the device.

</dd> <dt>

10 (0xA)
</dt> <dd>

The network interface cannot start.

</dd> <dt>

11 (0xB)
</dt> <dd>

The network interface failed.

</dd> <dt>

12 (0xC)
</dt> <dd>

The network interface cannot find enough free resources to use.

</dd> <dt>

13 (0xD)
</dt> <dd>

Windows cannot verify the network interface's resources.

</dd> <dt>

14 (0xE)
</dt> <dd>

The network interface cannot work properly until the computer is restarted.

</dd> <dt>

15 (0xF)
</dt> <dd>

The network interface is not working properly due to a possible re-enumeration problem.

</dd> <dt>

16 (0x10)
</dt> <dd>

Windows cannot identify all of the resources that the network interface uses.

</dd> <dt>

17 (0x11)
</dt> <dd>

The network interface is requesting an unknown resource type.

</dd> <dt>

18 (0x12)
</dt> <dd>

The network interface device drivers must be reinstalled.

</dd> <dt>

19 (0x13)
</dt> <dd>

Failure using the VxD loader.

</dd> <dt>

20 (0x14)
</dt> <dd>

The registry might be corrupted.

</dd> <dt>

21 (0x15)
</dt> <dd>

System failure. If changing the device driver is ineffective, see the hardware documentation. Windows is removing the network interface.

</dd> <dt>

22 (0x16)
</dt> <dd>

The network interface is disabled.

</dd> <dt>

23 (0x17)
</dt> <dd>

System failure. If changing the network interface device driver is ineffective, see the hardware documentation.

</dd> <dt>

24 (0x18)
</dt> <dd>

The network interface is not present, not working properly, or does not have all of its drivers installed.

</dd> <dt>

25 (0x19)
</dt> <dd>

Windows is still setting up the network interface.

</dd> <dt>

26 (0x1A)
</dt> <dd>

Windows is still setting up the network interface.

</dd> <dt>

27 (0x1B)
</dt> <dd>

The network interface does not have valid log configuration.

</dd> <dt>

28 (0x1C)
</dt> <dd>

The network interface device drivers are not installed.

</dd> <dt>

29 (0x1D)
</dt> <dd>

The network interface is disabled; the device firmware did not provide the required resources.

</dd> <dt>

30 (0x1E)
</dt> <dd>

The network interface is using an IRQ resource that another device is using.

</dd> <dt>

31 (0x1F)
</dt> <dd>

The network interface is not working properly; Windows cannot load the required device drivers.

</dd> </dl>

</dd> <dt>

**ConfigManagerUserConfig**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Read**, **Schema** ("Win32")
</dt> </dl>

If **TRUE**, the device is using a user-defined configuration.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_KEY**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Indicates the name of the class or the subclass used in the creation of an instance.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides comments about the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Provides an address or other identifying information that uniquely identifies the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**DhcpEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if DHCP is enabled on the network interface.

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the error reported in the **LastErrorCode** property is now cleared.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies more information about the error recorded in the **LastErrorCode** property and information on any corrective actions that may be taken.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the flags set for the [network interface](https://msdn.microsoft.com/library/aa371519). For a list of possible flags, see [CLUSCTL\_NETINTERFACE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367261).

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Id of the network interface.

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**OtherIdentifyingInfo**")
</dt> </dl>

Represents an array of free-form strings that provide explanations and details behind the entries in the **OtherIdentifyingInfo** property array. Note that each entry of this array is related to the entry in the **OtherIdentifyingInfo** property that is located at the same index.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the network interface was installed. A lack of a value does not indicate that the network interface is not installed.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**IPv4Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the IPv4 addresses currently assigned to this network interface.

</dd> <dt>

**IPv6Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the IPv6 addresses currently assigned to this network interface.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Captures the last error code reported by the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the Clustering Service–generated name for the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**Network**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the name of the network to which the network interface is connected.

</dd> <dt>

**Node**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the name of the node in which the network interface is installed.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**IdentifyingDescriptions**")
</dt> </dl>

Captures additional data, in addition to the **DeviceID** property, that can be used to identify a network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**PNPDeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Read**, **Schema** ("Win32")
</dt> </dl>

Indicates the Win32 Plug and Play device identifier of the logical device.

Example: "\*PNP030b"

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the specific power-related capabilities of the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884). The following are the possible values.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

TBD

</dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>**Not Supported** (1)


</dt> <dd>

TBD

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (2)


</dt> <dd>

TBD

</dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (3)


</dt> <dd>

The power management features are currently enabled, but the exact feature set is unknown or the information is unavailable.

</dd> <dt>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>**Power Saving Modes Entered Automatically** (4)


</dt> <dd>

The device can change its power state based on usage or other criteria.

</dd> <dt>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>**Power State Settable** (5)


</dt> <dd>

The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method is supported. This method is found on the parent [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes](https://msdn.microsoft.com/library/aa390351).

</dd> <dt>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>**Power Cycling Supported** (6)


</dt> <dd>

The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle).

</dd> <dt>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>**Timed Power On Supported** (7)


</dt> <dd>

The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle) and *Time* set to a specific date and time, or interval, for power-on.

</dd> </dl>

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the node, with its running operating system, supports power management. If **FALSE**, the integer value 1 ("Not Supported") should be the only entry in the **PowerManagementCapabilities** array. This Boolean does not indicate that power management features are currently enabled, or if enabled, what features are supported. For more information, see the **PowerManagementCapabilities** array.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**PowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Counter**, [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours")
</dt> </dl>

Indicates the number of hours since the last power cycle of the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**PrivateProperties**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Property**](mscluster-property.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the private properties of the network interface.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current state of the network interface. The following are the possible values.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (-1)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **StateUnknown** before Windows Server 2012 R2 .

</dd> <dt>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>**Unavailable** (0)


</dt> <dd></dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (1)


</dt> <dd></dd> <dt>

<span id="Unreachable"></span><span id="unreachable"></span><span id="UNREACHABLE"></span>

<span id="Unreachable"></span><span id="unreachable"></span><span id="UNREACHABLE"></span>**Unreachable** (2)


</dt> <dd></dd> <dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>

<span id="Up"></span><span id="up"></span><span id="UP"></span>**Up** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Indicates the current status of the network interface.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

Values include the following:

"OK"

"Error"

"Degraded"

"Unknown"

"Pred Fail"

"Starting"

"Stopping"

"Service"

"Stressed"

"NonRecover"

"No Contact"

"Lost Comm"

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|004.3")
</dt> </dl>

Indicates whether the network interface is in an enabled, disabled, other, or unknown state.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884). The following are the possible values.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (3)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**CIM\_KEY**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Indicates the scoping system's **CreationClassName**.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Indicates the scoping system's **Name**.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**TotalPowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Counter**, [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours")
</dt> </dl>

Indicates the total number of hours that the network interface has been powered.

Inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> </dl>

## Remarks

The **MSCluster\_NetworkInterface** class is derived from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





