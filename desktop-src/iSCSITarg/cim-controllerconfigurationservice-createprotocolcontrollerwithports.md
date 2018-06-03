---
title: CreateProtocolControllerWithPorts method of the CIM\_ControllerConfigurationService class
description: This method creates an appropriate subclass of ProtocolController.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b165a001-0c17-4731-a91b-9843d0539557
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateProtocolControllerWithPorts method iSCSI Software Target API
- CreateProtocolControllerWithPorts method iSCSI Software Target API , CIM_ControllerConfigurationService class
- CIM_ControllerConfigurationService class iSCSI Software Target API , CreateProtocolControllerWithPorts method
topic_type:
- apiref
api_name:
- CIM_ControllerConfigurationService.CreateProtocolControllerWithPorts
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateProtocolControllerWithPorts method of the CIM\_ControllerConfigurationService class

This method creates an appropriate subclass of ProtocolController. In addition to its role of controlling downstream devices, a ProtocolControl is used to provide a central management point for access control with respect to those devices. Certain storage system implementations across multiple vendors require permissions to be established atomically with the creation of a ProtocolController. This method provides this capability via the Privilege and Identity properties. By supplying appropriate information in those properties, this method will assure that appropriate AuthorizedTarget and AuthorizedSubject associations, (as defined in the User and Security Model), are instantiated to restrict access to the logical devices 'behind' it.

If multiple target ports are specified in the Ports input parameter, all expose the same view (i.e., have the same unit numbers and permissions). This method does not create the port instances, but does create ProtocolControllerForPort associations between the specified ports and the new ProtocolController. The new ProtocolController is defined to be weak to the same System as the ControllerConfigurationService.

## Syntax


```mof
uint32 CreateProtocolControllerWithPorts(
  [in]  string                     ElementName,
  [in]  string                     Ports[],
  [in]  uint16                     Protocol,
  [in]  CIM_Privilege          REF Privilege,
  [in]  CIM_ManagedElement     REF Identity,
  [out] CIM_ProtocolController REF ProtocolController
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

The string to be used in the ElementName of the new ProtocolController.

</dd> <dt>

*Ports* \[in\]
</dt> <dd>

Array of strings containing representations of references to instances of CIM\_LogicalPort (or subclass) instances. This is the list of target ports that are associated to the ProtocolController. ProtocolControllerForPort associations are created by the instrumentation associating the new ProtocolController to these ports. If this parameter is null, then all ports in the storage system (this Service's 'scoping' System and all its ComponentCS Systems) are attached to the new ProtocolController.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

The protocol type for the new ProtocolController.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="SCSI"></span><span id="scsi"></span>

**SCSI** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*Privilege* \[in\]
</dt> <dd>

Reference to a CIM\_Privilege (or subclass) instance to be used as a template. If supplied, it has a 1:1 correspondence with the Identity parameter and this method will atomically create the new ProtocolController instance and related AuthorizedPrivilege, AuthorizedTarget and AuthorizedSubject instances.

Note: if ProtocolControllerRequiresAuthorizedIdentity is true, then the Identity/Privilege pair MUST be specified. If false, then the Identity/Privilege pair MUST NOT be specified.

</dd> <dt>

*Identity* \[in\]
</dt> <dd>

Reference to a CIM\_ManagedElement (or subclass) instance. This ManagedElement MUST be either a CIM\_Identity, or a CIM\_Collection (or subclass, eg. SystemSpecificCollection, Role, or Group) that has CIM\_Identities as MemberOfCollection. If ProtocolControllerMaskingCapabilities.ProtocolControllerSupportsCollection is false, the reference MUST be to a CIM\_Identity (or subclass). If present, it has a 1:1 correspondence with the Privilege property. If present, this method will atomically create the new ProtocolController instance and instantiate a missing AuthorizedSubject association between the Privilege/Identity pair; and instantiate an AuthorizedTarget association between the AuthorizedPrivilege and the new ProtocolController.

Note: if ProtocolControllerRequiresAuthorizedIdentity is true, then at least the Identity/Privilege pair MUST be specified.

</dd> <dt>

*ProtocolController* \[out\]
</dt> <dd>

A reference to the new ProtocolController that is created.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**DMTF Reserved** (6 4095)
</dt> <dt>

**ID Parameter Missing or Not Unique** (4096)
</dt> <dt>

**Hardware Implementation Requires Null Ports Parameter** (4097)
</dt> <dt>

**Busy** (4098)
</dt> <dt>

**Method Reserved** (4099 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

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

[**CIM\_ControllerConfigurationService**](cim-controllerconfigurationservice.md)
</dt> </dl>

 

 





