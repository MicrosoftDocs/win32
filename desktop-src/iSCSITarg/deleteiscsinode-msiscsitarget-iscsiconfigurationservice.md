---
title: DeleteiSCSINode method of the MSISCSITARGET\_iSCSIConfigurationService class
description: Deletes an instance of CIM\_SCSIProtocolController that represents an iSCSI node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'aca45716-2040-42a7-b6d6-06c2c6bb10ec'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DeleteiSCSINode method iSCSI Software Target API", "DeleteiSCSINode method iSCSI Software Target API , MSISCSITARGET_iSCSIConfigurationService class", "MSISCSITARGET_iSCSIConfigurationService class iSCSI Software Target API , DeleteiSCSINode method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConfigurationService.DeleteiSCSINode
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# DeleteiSCSINode method of the MSISCSITARGET\_iSCSIConfigurationService class

Deletes an instance of [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) that represents an iSCSI node.

This method overrides the method that is inherited from the **CIM\_iSCSIConfigurationService** class.

## Syntax


```mof
uint32 DeleteiSCSINode(
  [in] CIM_SCSIProtocolController REF iSCSINode
);
```



## Parameters

<dl> <dt>

*iSCSINode* \[in\]
</dt> <dd>

Specifies the iSCSI node to be deleted.

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

**SCSIProtocolController Non-Existent** (4096)
</dt> <dt>

**Sessions Active on Node Ports** (4097)
</dt> <dt>

**Method Reserved** (4098–32767)
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

[**MSISCSITARGET\_iSCSIConfigurationService**](msiscsitarget-iscsiconfigurationservice.md)
</dt> </dl>

 

 





