---
title: GetSupportedConnectionFeatures method of the CIM\_ReplicationServiceCapabilities class
description: This method accepts a connection reference and returns specific features of that connection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 46a9d0fd-500a-4140-b040-4dcca271b8a9
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedConnectionFeatures method iSCSI Software Target API
- GetSupportedConnectionFeatures method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedConnectionFeatures method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSupportedConnectionFeatures
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedConnectionFeatures method of the CIM\_ReplicationServiceCapabilities class

This method accepts a connection reference and returns specific features of that connection.

## Syntax


```mof
uint32 GetSupportedConnectionFeatures(
  [in]  CIM_ServiceAccessPoint REF connection,
  [out] uint16                     SupportedConnectionFeatures[]
);
```



## Parameters

<dl> <dt>

*connection* \[in\]
</dt> <dd>

A value representing the connection.

</dd> <dt>

*SupportedConnectionFeatures* \[out\]
</dt> <dd>

An array supported connection features. Unidirectional to ServiceAccessPoint: Data flow is unidirectional to ServiceAccessPoint such as a protocol end point. Unidirectional from ServiceAccessPoint: Data flow is unidirectional from ServiceAccessPoint such as a protocol end point.

<dt>

<span id="Unidirectional_to_ServiceAccessPoint"></span><span id="unidirectional_to_serviceaccesspoint"></span><span id="UNIDIRECTIONAL_TO_SERVICEACCESSPOINT"></span>

**Unidirectional to ServiceAccessPoint** (2)


</dt> <dd></dd> <dt>

<span id="Unidirectional_from_ServiceAccessPoint"></span><span id="unidirectional_from_serviceaccesspoint"></span><span id="UNIDIRECTIONAL_FROM_SERVICEACCESSPOINT"></span>

**Unidirectional from ServiceAccessPoint** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> </dl>

## Return value

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

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 4294967295)
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

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> </dl>

 

 





