---
title: CreateiSCSINode method of the CIM\_iSCSIConfigurationService class
description: This method creates an iSCSI Node in the form of an instance of SCSIProtocolController.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '934945ec-61e4-4ec8-8fd1-79f18f146294'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateiSCSINode method iSCSI Software Target API", "CreateiSCSINode method iSCSI Software Target API , CIM_iSCSIConfigurationService class", "CIM_iSCSIConfigurationService class iSCSI Software Target API , CreateiSCSINode method"]
topic_type:
- apiref
api_name:
- CIM_iSCSIConfigurationService.CreateiSCSINode
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# CreateiSCSINode method of the CIM\_iSCSIConfigurationService class

This method creates an iSCSI Node in the form of an instance of SCSIProtocolController. As part of the creation process a SystemDevice association is created between the new SCSIProtocolController and the scoping Network Entity (CIM\_ComputerSystem) hosting this service.

## Syntax


```mof
uint32 CreateiSCSINode(
  [in]  string                         Alias,
  [out] CIM_SCSIProtocolController REF iSCSINode
);
```



## Parameters

<dl> <dt>

*Alias* \[in\]
</dt> <dd>

The iSCSI Alias for the new Node.

</dd> <dt>

*iSCSINode* \[out\]
</dt> <dd>

The SCSIProtocolController instance representing the created iSCSI Node.

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

**Node Creation Not Supported** (4096)
</dt> <dt>

**Alias In Use By Other Node** (4097)
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

[**CIM\_iSCSIConfigurationService**](cim-iscsiconfigurationservice.md)
</dt> </dl>

 

 





