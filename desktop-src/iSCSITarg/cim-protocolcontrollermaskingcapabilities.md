---
title: CIM\_ProtocolControllerMaskingCapabilities class
description: A subclass of Capabilities that defines the Masking-related capabilities of a ProtocolController.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 90079f1b-2ad5-4873-b222-6274e5d0ee00
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ProtocolControllerMaskingCapabilities class iSCSI Software Target API
- CIM_ProtocolControllerMaskingCapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_ProtocolControllerMaskingCapabilities
- CIM_ProtocolControllerMaskingCapabilities.Caption
- CIM_ProtocolControllerMaskingCapabilities.Description
- CIM_ProtocolControllerMaskingCapabilities.InstanceID
- CIM_ProtocolControllerMaskingCapabilities.ElementName
- CIM_ProtocolControllerMaskingCapabilities.ValidHardwareIdTypes
- CIM_ProtocolControllerMaskingCapabilities.OtherValidHardwareIDTypes
- CIM_ProtocolControllerMaskingCapabilities.PortsPerView
- CIM_ProtocolControllerMaskingCapabilities.ClientSelectableDeviceNumbers
- CIM_ProtocolControllerMaskingCapabilities.AttachDeviceSupported
- CIM_ProtocolControllerMaskingCapabilities.OneHardwareIDPerView
- CIM_ProtocolControllerMaskingCapabilities.UniqueUnitNumbersPerPort
- CIM_ProtocolControllerMaskingCapabilities.PrivilegeDeniedSupported
- CIM_ProtocolControllerMaskingCapabilities.ProtocolControllerRequiresAuthorizedIdentity
- CIM_ProtocolControllerMaskingCapabilities.ProtocolControllerSupportsCollections
- CIM_ProtocolControllerMaskingCapabilities.ExposePathsSupported
- CIM_ProtocolControllerMaskingCapabilities.CreateProtocolControllerSupported
- CIM_ProtocolControllerMaskingCapabilities.MaximumMapCount
- CIM_ProtocolControllerMaskingCapabilities.SPCAllowsNoLUs
- CIM_ProtocolControllerMaskingCapabilities.SPCAllowsNoTargets
- CIM_ProtocolControllerMaskingCapabilities.SPCAllowsNoInitiators
- CIM_ProtocolControllerMaskingCapabilities.SPCSupportsDefaultViews
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ProtocolControllerMaskingCapabilities class

A subclass of Capabilities that defines the Masking-related capabilities of a ProtocolController.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), UMLPackagePath("CIM::Device::ProtocolController")]
class CIM_ProtocolControllerMaskingCapabilities : CIM_Capabilities
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

The **CIM\_ProtocolControllerMaskingCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProtocolControllerMaskingCapabilities** class has these properties.

<dl> <dt>

**AttachDeviceSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system supports the AttachDevice method.

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

</dd> <dt>

**CreateProtocolControllerSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system supports the CreateProtocolControllerWithPorts method.

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

</dd> <dt>

**OneHardwareIDPerView**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if this storage system limits configurations to a single subject hardware ID per view. Otherwise, multiple hardware ID types can be used. The default is FALSE, that multiple ID types MAY be used in a single view.

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

</dd> <dt>

**PortsPerView**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An integer enumeration indicating the way that ports per view (ProtocolController) are handled by the underlying storage system.

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

</dd> <dt>

**ProtocolControllerRequiresAuthorizedIdentity**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, this property indicates that a Privilege/Identity pair MUST be specified when CreateProtocolControllerWithPorts() is called. If false, then the Privilege/Identity pair in CreateProtocolControllerWithPorts() MUST NOT be set.

</dd> <dt>

**ProtocolControllerSupportsCollections**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, this property indicates that the Identity parameter of CreateProtocolConntrollerWithPorts() MUST contain a reference to a CIM\_Collection (or subclass) or to a CIM\_Identity (or subclass). If ExposePathsSupported is true, this property indicates the storage system supports SystemSpecificCollections of StorageHardwareIDs.

</dd> <dt>

**SPCAllowsNoInitiators**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if the instumentation allows a client to create a configuration where an SPC has no StorageHardwareIDs associated via CIM\_AuthorizedTarget/CIM\_AuthorizedPrivilege/CIM\_AuthorizedSubject.

</dd> <dt>

**SPCAllowsNoLUs**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if the instumentation allows a client to create a configuration where an SPC has no LogicalDevices associated via CIM\_ProtocolControllerForUnit associations.

</dd> <dt>

**SPCAllowsNoTargets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if the instumentation allows a client to create a configuration where an SPC has no target SCSIProtocolEndpoints associated via CIM\_SAPAvailableForELement associations.

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

</dd> <dt>

**UniqueUnitNumbersPerPort**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When set to false, different ProtocolContollers attached to a LogicalPort can expose the same unit numbers. If true, then this storage system requires unique unit numbers across all the ProtocolControllers connected to a LogicalPort.

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

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> </dl>

 

 





