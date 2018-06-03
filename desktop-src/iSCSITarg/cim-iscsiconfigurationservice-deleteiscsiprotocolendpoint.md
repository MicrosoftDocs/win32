---
title: DeleteiSCSIProtocolEndpoint method of the CIM\_iSCSIConfigurationService class
description: The method deletes an instance of iSCSIProtocolEndpoint and all associations in which this iSCSIProtocolEndpoint is referenced.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 61535e53-81f4-4ffb-a6be-4820bf900c6a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteiSCSIProtocolEndpoint method iSCSI Software Target API
- DeleteiSCSIProtocolEndpoint method iSCSI Software Target API , CIM_iSCSIConfigurationService class
- CIM_iSCSIConfigurationService class iSCSI Software Target API , DeleteiSCSIProtocolEndpoint method
topic_type:
- apiref
api_name:
- CIM_iSCSIConfigurationService.DeleteiSCSIProtocolEndpoint
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteiSCSIProtocolEndpoint method of the CIM\_iSCSIConfigurationService class

The method deletes an instance of iSCSIProtocolEndpoint and all associations in which this iSCSIProtocolEndpoint is referenced.

## Syntax


```mof
uint32 DeleteiSCSIProtocolEndpoint(
  [in] CIM_iSCSIProtocolEndpoint REF iSCSIPort
);
```



## Parameters

<dl> <dt>

*iSCSIPort* \[in\]
</dt> <dd>

The iSCSIProtocolEndpoint to be deleted.

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

**Endpoint Non-Existent** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
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

[**CIM\_iSCSIConfigurationService**](cim-iscsiconfigurationservice.md)
</dt> </dl>

 

 





