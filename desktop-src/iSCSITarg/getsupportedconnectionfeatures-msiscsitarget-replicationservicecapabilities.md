---
title: GetSupportedConnectionFeatures method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves specific features of a specified protocol endpoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 35d68908-a690-4c5c-aafb-b659a3137143
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedConnectionFeatures method iSCSI Software Target API
- GetSupportedConnectionFeatures method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class
- MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedConnectionFeatures method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSupportedConnectionFeatures
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedConnectionFeatures method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves specific features of a specified protocol endpoint.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSupportedConnectionFeatures(
  [in]  CIM_ServiceAccessPoint Ref connection,
  [out] uint16                     SupportedConnectionFeatures[]
);
```



## Parameters

<dl> <dt>

*connection* \[in\]
</dt> <dd>

Specifies the protocol endpoint to query.

</dd> <dt>

*SupportedConnectionFeatures* \[out\]
</dt> <dd>

On return, indicates the supported connection features.

The possible values are.

<dt>

<span id="Unidirectional_to_ServiceAccessPoint"></span><span id="unidirectional_to_serviceaccesspoint"></span><span id="UNIDIRECTIONAL_TO_SERVICEACCESSPOINT"></span>

**Unidirectional to ServiceAccessPoint** (2)


</dt> <dd></dd> <dt>

<span id="Unidirectional_from_ServiceAccessPoint"></span><span id="unidirectional_from_serviceaccesspoint"></span><span id="UNIDIRECTIONAL_FROM_SERVICEACCESSPOINT"></span>

**Unidirectional from ServiceAccessPoint** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
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

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md)
</dt> <dt>

[**MSISCSITARGET\_TCPProtocolEndpoint**](msiscsitarget-tcpprotocolendpoint.md)
</dt> </dl>

 

 





