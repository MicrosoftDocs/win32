---
title: CreateProtocolControllerWithPorts method of the MSISCSITARGET\_ControllerConfigurationService class
description: Atomically creates a specified instance of the CIM\_ProtocolController class or subclass along with any required CIM\_AuthorizedPrivilege, CIM\_AuthorizedTarget, and CIM\_AuthorizedSubject instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '576977d5-7241-4575-8d86-faf5677f2cc7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateProtocolControllerWithPorts method iSCSI Software Target API", "CreateProtocolControllerWithPorts method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class", "MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , CreateProtocolControllerWithPorts method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.CreateProtocolControllerWithPorts
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateProtocolControllerWithPorts method of the MSISCSITARGET\_ControllerConfigurationService class

Atomically creates a specified instance of the [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) class or subclass along with any required **CIM\_AuthorizedPrivilege**, **CIM\_AuthorizedTarget**, and **CIM\_AuthorizedSubject** instances.

Some implementations require permissions to be established atomically with the creation of a protocol controller. This method provides this capability by specifying the *Privilege* and *Identity* properties. This method will instantiate appropriate **CIM\_AuthorizedTarget** and **CIM\_AuthorizedSubject** associations, as defined in the User and Security Model, to restrict access to the downstream logical devices.

This method is inherited from the **CIM\_ControllerConfigurationService** class.

## Syntax


```mof
uint32 CreateProtocolControllerWithPorts(
  [in]  string                     ElementName,
  [in]  string                     Ports[],
  [in]  uint16                     Protocol,
  [in]  CIM_Privilege Ref          Privilege,
  [in]  CIM_ManagedElement Ref     Identity,
  [out] CIM_ProtocolController Ref ProtocolController
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Specifies the **ElementName** of the new [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) instance.

</dd> <dt>

*Ports* \[in\]
</dt> <dd>

Contains string representations of references to instances of [**CIM\_LogicalPort**](https://msdn.microsoft.com/library/cc136869) or subclass instances. This is the list of target ports that are associated to the protocol controller. **CIM\_ProtocolControllerForPort** associations are created by the instrumentation that associate the new protocol controller to these ports. If this parameter is null, then all ports in the scope of the [**CIM\_System**](https://msdn.microsoft.com/library/aa388503) instance are attached to the new [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) instance.

If multiple target ports are specified in this parameter, all expose the same view, that is they have the same unit numbers and permissions.

> [!Note]  
> This method does not create the port instances, but does create **CIM\_ProtocolControllerForPort** associations between the specified ports and the new [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) instance.

 

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

Specifies the protocol type for the new [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) instance.

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

Specifies a **CIM\_Privilege** or subclass instance to be used as a template.

If supplied, this parameter and the *Identity* parameter specify how this method will create the related **CIM\_AuthorizedPrivilege**, **CIM\_AuthorizedTarget**, and **CIM\_AuthorizedSubject** instances.

> [!Note]  
> If the **CIM\_ProtocolControllerMaskingCapabilities.ProtocolControllerRequiresAuthorizedIdentity** is **True**, then both the *Identity* and *Privilege* parameters must be specified. If false, then neither can be specified.

 

</dd> <dt>

*Identity* \[in\]
</dt> <dd>

Specifies a [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) subclass instance. If **CIM\_ProtocolControllerMaskingCapabilities.ProtocolControllerSupportsCollection** is **True**, the reference may be either a collection of **CIM\_Identity** or subclass instances or a single instance. If false, it must be a single instance.

If supplied, this parameter and the *Privilege* parameter specify how this method will create the related **CIM\_AuthorizedPrivilege**, **CIM\_AuthorizedTarget**, and **CIM\_AuthorizedSubject** instances.

> [!Note]  
> If the **CIM\_ProtocolControllerMaskingCapabilities.ProtocolControllerRequiresAuthorizedIdentity** is **True**, then both the *Identity* and *Privilege* parameters must be specified. If false, then neither can be specified.

 

</dd> <dt>

*ProtocolController* \[out\]
</dt> <dd>

On return contains a reference to the new [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) that is created.

</dd> </dl>

## Return value

This method returns one of the following values.

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

**DMTF Reserved** (6–4095)
</dt> <dt>

**ID Parameter Missing or Not Unique** (4096)
</dt> <dt>

**Hardware Implementation Requires Null Ports Parameter** (4097)
</dt> <dt>

**Busy** (4098)
</dt> <dt>

**Method Reserved** (4099–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_ProtocolControllerMaskingCapabilities**](msiscsitarget-protocolcontrollermaskingcapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedPrivilege**](msiscsitarget-authorizedprivilege.md)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedSubject**](msiscsitarget-authorizedsubject.md)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedTarget**](msiscsitarget-authorizedtarget.md)
</dt> </dl>

 

 





