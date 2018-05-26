---
title: MSISCSITARGET\_ProtocolControllerMaskingCapabilities class
description: Defines the masking-related capabilities of a protocol controller.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 326803b4-4945-4140-959f-4cc873111145
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_ProtocolControllerMaskingCapabilities class iSCSI Software Target API
- MSISCSITARGET_ProtocolControllerMaskingCapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_ProtocolControllerMaskingCapabilities
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.Caption
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.Description
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.InstanceID
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.ElementName
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.ValidHardwareIdTypes
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.OtherValidHardwareIDTypes
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.PortsPerView
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.ClientSelectableDeviceNumbers
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.AttachDeviceSupported
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.OneHardwareIDPerView
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.UniqueUnitNumbersPerPort
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.PrivilegeDeniedSupported
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.ProtocolControllerRequiresAuthorizedIdentity
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.ProtocolControllerSupportsCollections
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.ExposePathsSupported
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.CreateProtocolControllerSupported
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.MaximumMapCount
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.SPCAllowsNoLUs
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.SPCAllowsNoTargets
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.SPCAllowsNoInitiators
- MSISCSITARGET_ProtocolControllerMaskingCapabilities.SPCSupportsDefaultViews
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_ProtocolControllerMaskingCapabilities class

Defines the masking-related capabilities of a protocol controller.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Static, Version("1.0.0")]
class MSISCSITARGET_ProtocolControllerMaskingCapabilities : CIM_ProtocolControllerMaskingCapabilities
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  uint16  ValidHardwareIdTypes[];
  string  OtherValidHardwareIDTypes[];
  uint16  PortsPerView = 2;
  boolean ClientSelectableDeviceNumbers = TRUE;
  boolean AttachDeviceSupported;
  boolean OneHardwareIDPerView = FALSE;
  boolean UniqueUnitNumbersPerPort = FALSE;
  boolean PrivilegeDeniedSupported = FALSE;
  boolean ProtocolControllerRequiresAuthorizedIdentity = FALSE;
  boolean ProtocolControllerSupportsCollections = FALSE;
  boolean ExposePathsSupported;
  boolean CreateProtocolControllerSupported;
  uint16  MaximumMapCount = 0;
  boolean SPCAllowsNoLUs = FALSE;
  boolean SPCAllowsNoTargets = FALSE;
  boolean SPCAllowsNoInitiators = FALSE;
  boolean SPCSupportsDefaultViews = TRUE;
};
```

## Members

The **MSISCSITARGET\_ProtocolControllerMaskingCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_ProtocolControllerMaskingCapabilities** class has these properties.

<dl> <dt>

**AttachDeviceSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system supports the AttachDevice method.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ClientSelectableDeviceNumbers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system allows the client to specify the DeviceNumber parameter when calling ControllerConfigurationService.AttachDevice() or specify the DeviceNumbers parameter when calling ControllerConfigurationService.ExposePaths(). Set to false if the implementation does not allow unit numbers to vary for a ProtocolController. However, if set to false and a Device is not the Dependent of a ProtocolControllerForUnit association, the client MUST provide a DeviceNumber parameter in ControllerConfigurationService.AttachDevice or ControllerConfigurationService.ExposePaths. If set to false and the Device is already the Dependent of a ProtocolControllerForUnit association, then the client can omit the DeviceNumber parameter (or supply the same value) in subsequent ControllerConfigurationService.AttachDevice calls.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**CreateProtocolControllerSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system supports the CreateProtocolControllerWithPorts method.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

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

The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**ExposePathsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system supports the ExposePaths and HidePaths methods.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**MaximumMapCount**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of ProtocolCOntrollerForUnit associations that can be associated with a single LogicalDevice (for example, StorageVolume). Zero indicates there is no limit.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**OneHardwareIDPerView**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system limits configurations to a single subject hardware ID per view. Otherwise, multiple hardware ID types can be used. The default is FALSE, that multiple ID types MAY be used in a single view.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**OtherValidHardwareIDTypes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

An array of strings describing types for valid StorageHardwareID.IDType. Used when the ValidHardwareIdTypes includes 1 ("Other").

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**PortsPerView**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An integer enumeration indicating the way that ports per view (ProtocolController) are handled by the underlying storage system.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

<dt>

<span id="One_Port_per_View"></span><span id="one_port_per_view"></span><span id="ONE_PORT_PER_VIEW"></span>

**One Port per View** (2)


</dt> <dd></dd> <dt>

<span id="Multiple_Ports_per_View"></span><span id="multiple_ports_per_view"></span><span id="MULTIPLE_PORTS_PER_VIEW"></span>

**Multiple Ports per View** (3)


</dt> <dd></dd> <dt>

<span id="All_Ports_share_the_same_View"></span><span id="all_ports_share_the_same_view"></span><span id="ALL_PORTS_SHARE_THE_SAME_VIEW"></span>

**All Ports share the same View** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**PrivilegeDeniedSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system allows a client to create a Privilege instance with PrivilegeGranted set to FALSE.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**ProtocolControllerRequiresAuthorizedIdentity**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, this property indicates that a Privilege/Identity pair MUST be specified when CreateProtocolControllerWithPorts() is called. If false, then the Privilege/Identity pair in CreateProtocolControllerWithPorts() MUST NOT be set.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**ProtocolControllerSupportsCollections**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, this property indicates that the Identity parameter of CreateProtocolConntrollerWithPorts() MUST contain a reference to a CIM\_Collection (or subclass) or to a CIM\_Identity (or subclass). If ExposePathsSupported is true, this property indicates the storage system supports SystemSpecificCollections of StorageHardwareIDs.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**SPCAllowsNoInitiators**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if the instumentation allows a client to create a configuration where an SPC has no StorageHardwareIDs associated via CIM\_AuthorizedTarget/CIM\_AuthorizedPrivilege/CIM\_AuthorizedSubject.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**SPCAllowsNoLUs**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if the instumentation allows a client to create a configuration where an SPC has no LogicalDevices associated via CIM\_ProtocolControllerForUnit associations.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**SPCAllowsNoTargets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if the instumentation allows a client to create a configuration where an SPC has no target SCSIProtocolEndpoints associated via CIM\_SAPAvailableForELement associations.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**SPCSupportsDefaultViews**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ProtocolControllerMaskingCapabilities.PortsPerView")
</dt> </dl>

Set to true if it the instrumentation supports 'default view' SPCs that exposes logical units to all initiators (so called 'promiscuous LUNs'. Default view SPCs MUST have be associated to a CIM\_StorageHardwareID instance with Name set to the null string. A target port MUST NOT be associated with more a single default view SPC. If PortsPerView is 'All Ports share the same View', then at most one default view SPC MAY be associated with the target system. If SPCAllowsNoLUs is true, the instrumentation MAY instantiate a static default view instance or let the client create one as needed using ExposePaths. For other values of PortsPerView, all default view SPC MUST share the same null-Name CIM\_StorageHardwareID instance.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**UniqueUnitNumbersPerPort**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When set to false, different ProtocolContollers attached to a LogicalPort can expose the same unit numbers. If true, then this storage system requires unique unit numbers across all the ProtocolControllers connected to a LogicalPort.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

</dd> <dt>

**ValidHardwareIdTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

A list of the valid values for StrorageHardwareID.IDType. iSCSI IDs MAY use one of three iSCSI formats - iqn, eui, or naa. This three letter format is the name prefix; so a single iSCSI type is provided here, the prefix can be used to further refine the format.

This property is inherited from [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Port_WWN"></span><span id="port_wwn"></span><span id="PORT_WWN"></span>

**Port WWN** (2)


</dt> <dd></dd> <dt>

<span id="Node_WWN"></span><span id="node_wwn"></span><span id="NODE_WWN"></span>

**Node WWN** (3)


</dt> <dd></dd> <dt>

<span id="Host_Name"></span><span id="host_name"></span><span id="HOST_NAME"></span>

**Host Name** (4)


</dt> <dd></dd> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>

**iSCSI Name** (5)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**CIM\_ProtocolControllerForUnit**](https://msdn.microsoft.com/library/mt432253)
</dt> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> <dt>

[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871)
</dt> </dl>

 

 





