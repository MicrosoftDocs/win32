---
title: BindiSCSIProtocolEndPoint method of the CIM\_iSCSIConfigurationService class
description: This method provides for modification of an existing iSCSIProtocolEndpoint by associating a TCPProtocolEndpoint representing an Target NetworkPortal or an IPProtocolEndpoint instance representing an Initiator NetworkPortal to the iSCSIProtocolEndpoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '44c6f895-a837-49de-8f87-07bd9d769a6c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["BindiSCSIProtocolEndPoint method iSCSI Software Target API", "BindiSCSIProtocolEndPoint method iSCSI Software Target API , CIM_iSCSIConfigurationService class", "CIM_iSCSIConfigurationService class iSCSI Software Target API , BindiSCSIProtocolEndPoint method"]
topic_type:
- apiref
api_name:
- CIM_iSCSIConfigurationService.BindiSCSIProtocolEndPoint
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# BindiSCSIProtocolEndPoint method of the CIM\_iSCSIConfigurationService class

This method provides for modification of an existing iSCSIProtocolEndpoint by associating a TCPProtocolEndpoint representing an Target NetworkPortal or an IPProtocolEndpoint instance representing an Initiator NetworkPortal to the iSCSIProtocolEndpoint. The association is persisted as an instance of BindsTo. The selected Portal endpoint must be from the same SystemSpecificCollection, which represents a Portal Group, as the endpoints currently bound to the iSCSIProtocolEndpoint. This action is intended to be reversed by the use of the intrinsic method 'DeleteInstance'.

## Syntax


```mof
uint32 BindiSCSIProtocolEndPoint(
  [in] CIM_iSCSIProtocolEndpoint REF iSCSIPort,
  [in] CIM_ProtocolEndpoint      REF NetworkPortal
);
```



## Parameters

<dl> <dt>

*iSCSIPort* \[in\]
</dt> <dd>

A reference to the iSCSIProtocolEndpoint.

</dd> <dt>

*NetworkPortal* \[in\]
</dt> <dd>

The ProtocolEndpoint instance. If an iSCSI Initiator Port is being modified this will be an IPProtocolEndpoint. If an iSCSI Target Port is being modified this will be a TCPProtocolEndpoint.

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

**ProtocolEndpoint Non-Existent** (4096)
</dt> <dt>

**TCPProtocolEndpoint Not Bound To Underlying IPProtocolEndpoint** (4097)
</dt> <dt>

**ProtocolEndpoint In Use By Other iSCSIProtocolEndpoint In Same Target SCSIProtocolController** (4098)
</dt> <dt>

**ProtocolEndpoint Not From Same Endpoint Collection** (4099)
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
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_iSCSIConfigurationService**](cim-iscsiconfigurationservice.md)
</dt> </dl>

 

 





