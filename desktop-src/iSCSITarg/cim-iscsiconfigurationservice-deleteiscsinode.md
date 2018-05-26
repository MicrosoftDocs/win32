---
title: DeleteiSCSINode method of the CIM\_iSCSIConfigurationService class
description: This method deletes an instance of SCSIProtocolController respresenting an iSCSI Node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 456bbb87-e810-4ce6-9551-c9d60a01dd2b
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteiSCSINode method iSCSI Software Target API
- DeleteiSCSINode method iSCSI Software Target API , CIM_iSCSIConfigurationService class
- CIM_iSCSIConfigurationService class iSCSI Software Target API , DeleteiSCSINode method
topic_type:
- apiref
api_name:
- CIM_iSCSIConfigurationService.DeleteiSCSINode
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteiSCSINode method of the CIM\_iSCSIConfigurationService class

This method deletes an instance of SCSIProtocolController respresenting an iSCSI Node. If Sessions are active on iSCSIProtocolEndpoints belonging to this node an error will be returned. If no Sessions are active the scoped iSCSIProtocolEndpoints will be deleted.

## Syntax


```mof
uint32 DeleteiSCSINode(
  [in] CIM_SCSIProtocolController REF iSCSINode
);
```



## Parameters

<dl> <dt>

*iSCSINode* \[in\]
</dt> <dd>

The SCSIProtocolController instance representing the iSCSI Node that will be deleted.

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

**SCSIProtocolController Non-Existent** (4096)
</dt> <dt>

**Sessions Active on Node Ports** (4097)
</dt> <dt>

**Method Reserved** (4098 32767)
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

 

 





