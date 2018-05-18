---
title: CreateiSCSIProtocolEndpoint method of the MSISCSITARGET\_iSCSIConfigurationService class
description: Creates an iSCSI port in the form of an MSISCSITARGET\_iSCSIProtocolEndpoint instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b70454fa-ddd8-489c-acaf-8c32e7a158b7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateiSCSIProtocolEndpoint method iSCSI Software Target API", "CreateiSCSIProtocolEndpoint method iSCSI Software Target API , MSISCSITARGET_iSCSIConfigurationService class", "MSISCSITARGET_iSCSIConfigurationService class iSCSI Software Target API , CreateiSCSIProtocolEndpoint method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConfigurationService.CreateiSCSIProtocolEndpoint
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateiSCSIProtocolEndpoint method of the MSISCSITARGET\_iSCSIConfigurationService class

Creates an iSCSI port in the form of an [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md) instance.

This method is inherited from the **CIM\_iSCSIConfigurationService** class.

## Syntax


```mof
uint32 CreateiSCSIProtocolEndpoint(
  [in]           CIM_SCSIProtocolController Ref iSCSINode,
  [in]           uint16                         Role,
  [in, optional] string                         Identifier,
  [in]           CIM_ProtocolEndpoint Ref       NetworkPortals[],
  [out]          CIM_iSCSIProtocolEndpoint Ref  iSCSIPort
);
```



## Parameters

<dl> <dt>

*iSCSINode* \[in\]
</dt> <dd>

Specifies the iSCSI node that will contain the iSCSI port.

</dd> <dt>

*Role* \[in\]
</dt> <dd>

Specifies whether the new **CIM\_iSCSIProtocolEndpoint** instance acts as a target or an initiator endpoint.

The possible values are.

<dt>

<span id="Initiator"></span><span id="initiator"></span><span id="INITIATOR"></span>

**Initiator** (2)


</dt> <dd></dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>

**Target** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*Identifier* \[in, optional\]
</dt> <dd>

Specifies the **Identifier** property of the new **CIM\_iSCSIProtocolEndpoint** instance in the form of 12 hexadecimal digits. The *Identifier* for an initiator port is the initiator-side identifier (ISID) of the port. The *Identifier* for a target port is the Target Portal Group Tag (TGPT) of the port.

Each [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md) instance that is associated to a common [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instance must have a unique **Identifier**.

> [!Note]  
> If the [**MSISCSITARGET\_iSCSIConfigurationCapabilities**](msiscsitarget-iscsiconfigurationcapabilities.md).**IdentifierSelectionSupported** property is **false**, this parameter must be set to **NULL**.

 

</dd> <dt>

*NetworkPortals* \[in\]
</dt> <dd>

Specifies either **CIM\_TCPProtocolEndpoint** instances that represent target network portals or **CIM\_IPProtocolEndpoint** instances that represent initiator network portals. If **CIM\_TCPProtocolEndpoint** instances are supplied, each must be associated to a **CIM\_IPProtocolEndpoint** instance through a [**CIM\_BindsTo**](https://msdn.microsoft.com/library/cc150664) association to provide the target network portal functionality. The selected portal endpoints must be from the same system specific collection, which represents a portal group.

</dd> <dt>

*iSCSIPort* \[out\]
</dt> <dd>

On return, contains a reference to the new [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md) instance.

The new [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md) instance is associated with the specified underlying instances of TCP/IP protocol endpoints by using [**CIM\_BindsTo**](https://msdn.microsoft.com/library/cc150664) instances. In addition, a [**MSISCSITARGET\_SAPAvailableForElement**](msiscsitarget-sapavailableforelement.md) instance is created that associates the specified [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) and the new **MSISCSITARGET\_iSCSIProtocolEndpoint** instance.

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

**SCSIProtocolController Non-existent** (4096)
</dt> <dt>

**Role Not Supported By Specified SCSIProtocolController** (4097)
</dt> <dt>

**Identifier In Use, Not Unique** (4098)
</dt> <dt>

**Identifier Selection Not Supported** (4099)
</dt> <dt>

**ProtocolEndpoint Non-Existent** (4100)
</dt> <dt>

**TCPProtocolEndpoint Not Bound To Underlying IPProtocolEndpoint** (4101)
</dt> <dt>

**TCPProtocolEndpoint In Use By Other iSCSIProtocolEndpoint In Same Target SCSIProtocolController** (4102)
</dt> <dt>

**ProtocolEndpoints Not From Same Endpoint Collection** (4103)
</dt> <dt>

**Method Reserved** (4100–32767)
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

[**MSISCSITARGET\_iSCSIConfigurationService**](msiscsitarget-iscsiconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_iSCSIConfigurationCapabilities**](msiscsitarget-iscsiconfigurationcapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md)
</dt> <dt>

[**MSISCSITARGET\_SAPAvailableForElement**](msiscsitarget-sapavailableforelement.md)
</dt> </dl>

 

 





