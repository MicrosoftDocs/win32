---
title: CreateiSCSINode method of the MSISCSITARGET\_iSCSIConfigurationService class
description: Creates a CIM\_SCSIProtocolController instance that represents an iSCSI node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 96e6dc13-767e-4169-b4a9-8482256c99d8
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateiSCSINode method iSCSI Software Target API
- CreateiSCSINode method iSCSI Software Target API , MSISCSITARGET_iSCSIConfigurationService class
- MSISCSITARGET_iSCSIConfigurationService class iSCSI Software Target API , CreateiSCSINode method
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConfigurationService.CreateiSCSINode
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateiSCSINode method of the MSISCSITARGET\_iSCSIConfigurationService class

Creates a [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instance that represents an iSCSI node. This method also creates a [**CIM\_SystemDevice**](https://msdn.microsoft.com/library/aa388509) instance that associates the new SCSI Protocol Controller (SPC) to the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) instance that represents the hosting network entity.

This method overrides the method that is inherited from the **CIM\_iSCSIConfigurationService** class.

## Syntax


```mof
uint32 CreateiSCSINode(
  [in]  string                         Alias,
  [out] CIM_SCSIProtocolController REF iSCSINode
);
```



## Parameters

<dl> <dt>

*Alias* \[in\]
</dt> <dd>

Specifies the **ElementName** property of the new node. The maximum length is 128 characters.

</dd> <dt>

*iSCSINode* \[out\]
</dt> <dd>

On return, contains the [**CIM\_SCSIProtocolController**](https://msdn.microsoft.com/library/cc136905) instance that represents the new iSCSI node.

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

**Node Creation Not Supported** (4096)
</dt> <dt>

**Alias In Use By Other Node** (4097)
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

[**MSISCSITARGET\_iSCSIConfigurationService**](msiscsitarget-iscsiconfigurationservice.md)
</dt> </dl>

 

 





