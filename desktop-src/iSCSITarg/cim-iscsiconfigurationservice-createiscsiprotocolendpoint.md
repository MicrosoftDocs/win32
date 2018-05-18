---
title: CreateiSCSIProtocolEndpoint method of the CIM\_iSCSIConfigurationService class
description: This method creates an iSCSI Port in the form of an instance of iSCSIProtocolEndpoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c524a244-f2ad-4dd9-9c85-cce6dd88fb96'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateiSCSIProtocolEndpoint method iSCSI Software Target API", "CreateiSCSIProtocolEndpoint method iSCSI Software Target API , CIM_iSCSIConfigurationService class", "CIM_iSCSIConfigurationService class iSCSI Software Target API , CreateiSCSIProtocolEndpoint method"]
topic_type:
- apiref
api_name:
- CIM_iSCSIConfigurationService.CreateiSCSIProtocolEndpoint
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateiSCSIProtocolEndpoint method of the CIM\_iSCSIConfigurationService class

This method creates an iSCSI Port in the form of an instance of iSCSIProtocolEndpoint. As part of the creation process the iSCSIProtocolEndpoint is 'bound to' the underlying TCP or IP ProtocolEndpoints which are specified as inputs by creating instances of the BindsTo association between the new instance and those instances. In addition, an instance of SAPAvailableForElement is created between the specified SCSIProtocolController and the new instance of iSCSIProtocolEndpoint.

## Syntax


```mof
uint32 CreateiSCSIProtocolEndpoint(
  [in]  CIM_SCSIProtocolController REF iSCSINode,
  [in]  uint16                         Role,
  [in]  string                         Identifier,
  [in]  CIM_ProtocolEndpoint       REF NetworkPortals[],
  [out] CIM_iSCSIProtocolEndpoint  REF iSCSIPort
);
```



## Parameters

<dl> <dt>

*iSCSINode* \[in\]
</dt> <dd>

The SCSIProtocolController instance representing the iSCSI Node that will contain the iSCSI Port.

</dd> <dt>

*Role* \[in\]
</dt> <dd>

For iSCSI, each iSCSIProtocolEndpoint must act as either a target or an initiator endpoint. This property indicates which role this iSCSIProtocolEndpoint implements.

<dt>

<span id="Initiator"></span><span id="initiator"></span><span id="INITIATOR"></span>

**Initiator** (2)


</dt> <dd></dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>

**Target** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*Identifier* \[in\]
</dt> <dd>

If this is an Initiator Port, Identifier MUST contain the ISID, if this is a Target Port, Identifier MUST contain the Target Portal Group Tag (TGPT). Each iSCSIProtocolEndpoint (iSCSI port) associated to a common SCSIProtocolController (iSCSI node) must have a unique Identifier. This field is a string that contains 12 hexadecimal digits. If the property IdentifierSelectionSupported in class iSCSIConfigurationCapabilities is false, this parameter MUST be set to NULL.

</dd> <dt>

*NetworkPortals* \[in\]
</dt> <dd>

Array of References to either TCPProtocolEndpoints representing Target NetworkPortals or IPProtocolEndpoint instances representing Initiator NetworkPortals. If TCPProtocolEndpoints are supplied each MUST be in turn associated to an instance of IPProtocolEndpoint via a BindsTo association in order to provide the Target Network Portal functionality. The selected Portal endpoints MUST be from the same SystemSpecificCollection, which represents a Portal Group.

</dd> <dt>

*iSCSIPort* \[out\]
</dt> <dd>

A reference to the new iSCSIProtocolEndpoint that is created.

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

**Method Reserved** (4104–32767)
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
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_iSCSIConfigurationService**](cim-iscsiconfigurationservice.md)
</dt> </dl>

 

 





