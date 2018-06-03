---
title: BindiSCSIProtocolEndPoint method of the MSISCSITARGET\_iSCSIConfigurationService class
description: Modifies an existing MSISCSITARGET\_iSCSIProtocolEndpoint instance by associating a Target Network Port or an Initiator Network Port to the MSISCSITARGET\_iSCSIProtocolEndpoint instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ef5f8a4b-1714-45c5-830b-9ea5c5899f13
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BindiSCSIProtocolEndPoint method iSCSI Software Target API
- BindiSCSIProtocolEndPoint method iSCSI Software Target API , MSISCSITARGET_iSCSIConfigurationService class
- MSISCSITARGET_iSCSIConfigurationService class iSCSI Software Target API , BindiSCSIProtocolEndPoint method
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConfigurationService.BindiSCSIProtocolEndPoint
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BindiSCSIProtocolEndPoint method of the MSISCSITARGET\_iSCSIConfigurationService class

Modifies an existing [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md) instance by associating a Target Network Port or an Initiator Network Port to the **MSISCSITARGET\_iSCSIProtocolEndpoint** instance. The association is persisted as a [**CIM\_BindsTo**](https://msdn.microsoft.com/library/cc150664) instance.

This action is intended to be reversed by the use of the intrinsic [CimSession](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimsession.aspx).[**DeleteInstance**](Overload:Microsoft.Management.Infrastructure.CimSession.DeleteInstance) method.

This method is inherited from the **CIM\_iSCSIConfigurationService** class.

## Syntax


```mof
uint32 BindiSCSIProtocolEndPoint(
  [in] CIM_iSCSIProtocolEndpoint Ref iSCSIPort,
  [in] CIM_ProtocolEndpoint Ref      NetworkPortal
);
```



## Parameters

<dl> <dt>

*iSCSIPort* \[in\]
</dt> <dd>

Specifies the iSCSI protocol endpoint to modify.

</dd> <dt>

*NetworkPortal* \[in\]
</dt> <dd>

Specifies the protocol endpoint instance to associate.

An iSCSI Initiator Port is represented by a **CIM\_IPProtocolEndpoint** instance. An iSCSI Target Port is represented by a **CIM\_TCPProtocolEndpoint** instance.

The selected endpoint must be from the same portal group, that is a system specific collection, as the endpoints that are currently bound to the [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md) instance.

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

**DMTF Reserved** (6 4095)
</dt> <dt>

**ProtocolEndpoint Non-Existent** (4096)
</dt> <dt>

**TCPProtocolEndpoint Not Bound To Underlying IPProtocolEndpoint** (4097)
</dt> <dt>

**ProtocolEndpoint In Use By Other iSCSIProtocolEndpoint In Same Target SCSIProtocolController** (4098)
</dt> <dt>

**ProtocolEndpoint Not From Same Endpoint Collection** (4099)
</dt> <dt>

**Method Reserved** (4100 32767)
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
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_iSCSIConfigurationService**](msiscsitarget-iscsiconfigurationservice.md)
</dt> </dl>

 

 





