---
title: CIM\_VirtualEthernetSwitchSettingData class
description: Describes settings data for a virtual ethernet switch.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ebe2c10a-513d-4bb4-a5f3-64f21cc346aa
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_VirtualEthernetSwitchSettingData class
- CIM_VirtualEthernetSwitchSettingData class, described
topic_type:
- apiref
api_name:
- CIM_VirtualEthernetSwitchSettingData
- CIM_VirtualEthernetSwitchSettingData.Caption
- CIM_VirtualEthernetSwitchSettingData.Description
- CIM_VirtualEthernetSwitchSettingData.InstanceID
- CIM_VirtualEthernetSwitchSettingData.ElementName
- CIM_VirtualEthernetSwitchSettingData.VirtualSystemIdentifier
- CIM_VirtualEthernetSwitchSettingData.VirtualSystemType
- CIM_VirtualEthernetSwitchSettingData.Notes
- CIM_VirtualEthernetSwitchSettingData.CreationTime
- CIM_VirtualEthernetSwitchSettingData.ConfigurationID
- CIM_VirtualEthernetSwitchSettingData.ConfigurationDataRoot
- CIM_VirtualEthernetSwitchSettingData.ConfigurationFile
- CIM_VirtualEthernetSwitchSettingData.SnapshotDataRoot
- CIM_VirtualEthernetSwitchSettingData.SuspendDataRoot
- CIM_VirtualEthernetSwitchSettingData.SwapFileDataRoot
- CIM_VirtualEthernetSwitchSettingData.LogDataRoot
- CIM_VirtualEthernetSwitchSettingData.AutomaticStartupAction
- CIM_VirtualEthernetSwitchSettingData.AutomaticStartupActionDelay
- CIM_VirtualEthernetSwitchSettingData.AutomaticStartupActionSequenceNumber
- CIM_VirtualEthernetSwitchSettingData.AutomaticShutdownAction
- CIM_VirtualEthernetSwitchSettingData.AutomaticRecoveryAction
- CIM_VirtualEthernetSwitchSettingData.RecoveryFile
- CIM_VirtualEthernetSwitchSettingData.VLANConnection
- CIM_VirtualEthernetSwitchSettingData.AssociatedResourcePool
- CIM_VirtualEthernetSwitchSettingData.MaxNumMACAddress
api_location:
- VMMS.exe
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_VirtualEthernetSwitchSettingData class

Describes settings data for a virtual ethernet switch.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.26.0"), UMLPackagePath("CIM::Core::Virtualization")]
class CIM_VirtualEthernetSwitchSettingData : CIM_VirtualSystemSettingData
{
  string   Caption;
  string   Description;
  string   InstanceID;
  string   ElementName;
  string   VirtualSystemIdentifier;
  string   VirtualSystemType;
  string   Notes[];
  datetime CreationTime;
  string   ConfigurationID;
  string   ConfigurationDataRoot;
  string   ConfigurationFile;
  string   SnapshotDataRoot;
  string   SuspendDataRoot;
  string   SwapFileDataRoot;
  string   LogDataRoot;
  uint16   AutomaticStartupAction;
  datetime AutomaticStartupActionDelay;
  uint16   AutomaticStartupActionSequenceNumber;
  uint16   AutomaticShutdownAction;
  uint16   AutomaticRecoveryAction;
  string   RecoveryFile;
  string   VLANConnection[];
  string   AssociatedResourcePool[];
  uint32   MaxNumMACAddress;
};
```

## Members

The **CIM\_VirtualEthernetSwitchSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VirtualEthernetSwitchSettingData** class has these properties.

<dl> <dt>

**AssociatedResourcePool**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the host resource pools that are currently associated, or to associate with the ethernet switch, in order to allocate ethernet connections between the ethernet switch and a virtual machine. Each non-Null value of this property must conform to **WBEM\_URI\_UntypedInstancePath** as defined in the DMTF "DSP0207" specification.

</dd> <dt>

**AutomaticRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The action to take for the virtual system when the software executed by the virtual system fails. The failures addressed by this property only include those that are detectable by the host platform, such as a non-interruptible wait state condition.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="Restart"></span><span id="restart"></span><span id="RESTART"></span>

**Restart** (3)


</dt> <dd></dd> <dt>

<span id="Revert_to_snapshot"></span><span id="revert_to_snapshot"></span><span id="REVERT_TO_SNAPSHOT"></span>

**Revert to snapshot** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 65535</dd> </dl>

</dd> <dt>

**AutomaticShutdownAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The action to take for the virtual system when the host is shut down.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

<dt>

<span id="Turn_Off"></span><span id="turn_off"></span><span id="TURN_OFF"></span>

**Turn Off** (2)


</dt> <dd></dd> <dt>

<span id="Save_state"></span><span id="save_state"></span><span id="SAVE_STATE"></span>

**Save state** (3)


</dt> <dd></dd> <dt>

<span id="Shutdown"></span><span id="shutdown"></span><span id="SHUTDOWN"></span>

**Shutdown** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 65535</dd> </dl>

</dd> <dt>

**AutomaticStartupAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The action to take on the virtual system when the host is started.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="Restart_if_previously_active"></span><span id="restart_if_previously_active"></span><span id="RESTART_IF_PREVIOUSLY_ACTIVE"></span>

**Restart if previously active** (3)


</dt> <dd></dd> <dt>

<span id="Always_startup"></span><span id="always_startup"></span><span id="ALWAYS_STARTUP"></span>

**Always startup** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 65535</dd> </dl>

</dd> <dt>

**AutomaticStartupActionDelay**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The delay for the startup action. This value is an interval variant of the **datetime** data type.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**AutomaticStartupActionSequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The sequence number fo virtual system activation when the host system is started. A lower number indicates earlier activation. If one or more configurations show the same value, the sequence is implementation dependent. A value of "0" indicates that the sequence is implementation dependent.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ConfigurationDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file path of the directory where information about the virtual system configuration is stored. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**ConfigurationFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path of the file where information about the virtual system configuration is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**ConfigurationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique id of the virtual system configuration.

> [!Note]  
> **ConfigurationID** is different from the **InstanceID**, and is assigned by the implementation to a virtual system or a virtual system configuration. **ConfigurationID** is not a key, and the same value may occur for more than one instance.

 

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when the virtual system configuration was created.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for an instance of this class. In addition, the user-friendly name can be used as an index for a search or query. The name does not have to be unique within a namespace.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> -   *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID** property, or be a registered ID that is assigned by a recognized global authority.
> -   *OrgID* must not contain a colon. The first colon in **InstanceID** must be between the *OrgID* and*LocalID*.
> -   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
> -   If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
> -   For DMTF defined instances, the pattern must be used with the *OrgID* set to "CIM".

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**LogDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative file path of the directory where log information for the virtual system is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**MaxNumMACAddress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unique MAC addresses that the switch can learn for MAC address learning, as defined in the IEEE 802.1 standard.

</dd> <dt>

**Notes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains user supplied notes that are related to the virtual system.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**RecoveryFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of the file where recovery related information of the virtual system is stored. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**SnapshotDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path of the directory where information about virtual system snapshots is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**SuspendDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative path of the directory where suspend related information about the virtual system is stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**SwapFileDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative file path of the directory where swap files of the virtual system are stored. The relative path appends to the value of the **ConfigurationDataRoot** property. The format of this property is a URI based on RFC 2079.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**VirtualSystemIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique name for the system within the virtualization platform. **VirtualSystemIdentifier** is not the hostname assigned to the operating system instance running within the virtual system, nor is it an IP address or MAC address assigned to any of its network ports.

The **VirtualSystemIdentifier** may contain implementation specific rules, like simple patterns or a regular expression that may be interpreted by the implementation when setting **VirtualSystemIdentifier**.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**VirtualSystemType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the virtual system.

> [!Note]  
> If the virtual system type is unknown, this value must be set to "DMTF:unknown".

 

This property is formatted using the following Augmented Backus Naur Form (ABNF) format:

vs-type = dmtf-value / other-org-value / legacy-value; dmtf-value = "DMTF:" defining-org ":" org-vs-type; other-org-value = defining-org ":" org-vs-type;

The value of the above ABNF format are:

-   *dmtf-value*   a property value defined by DMTF and is defined in the description of this property.
-   *other-org-value*   is a property value defined by a business entity other than DMTF and is not defined in the description of this property.
-   *legacy-value*   a property value defined by a business entity other than DMTF and is not defined in the description of this property. These values are permitted but recommended to be deprecated over time.
-   *defining-org*   an identifier for the business entity that defines the virtual system type. It should include a copyrighted, trademarked, or a unique name that is owned by the business entity. It should not be "DMTF" and shall not contain a colon.
-   *org-vs-type*   an identifier for the virtual system type within the defining business entity. It should be unique within defining-org. org-vs-type may use any character allowed for CIM strings, except the following: U0000-U001F (Unicode C0 controls), U0020 (space), U007F (Unicode C0 controls), or U0080-U009F (Unicode C1 controls).
-   If there is a need to structure the value into segments, the segments should be separated with a single colon.
-   The values of this property should be processed case sensitively. They are intended to be processed programmatically, instead of being a display name, and should be short.

This property is inherited from [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).

</dd> <dt>

**VLANConnection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the VLAN IDs that the switch can access.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





