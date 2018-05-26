---
title: DeleteiSCSIProtocolEndpoint method of the MSISCSITARGET\_iSCSIConfigurationService class
description: Deletes an instance of the MSISCSITARGET\_iSCSIProtocolEndpoint class and all associations in which it is referenced.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91217f19-5bbf-473f-be7b-b9e707f0b435
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteiSCSIProtocolEndpoint method iSCSI Software Target API
- DeleteiSCSIProtocolEndpoint method iSCSI Software Target API , MSISCSITARGET_iSCSIConfigurationService class
- MSISCSITARGET_iSCSIConfigurationService class iSCSI Software Target API , DeleteiSCSIProtocolEndpoint method
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConfigurationService.DeleteiSCSIProtocolEndpoint
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteiSCSIProtocolEndpoint method of the MSISCSITARGET\_iSCSIConfigurationService class

Deletes an instance of the [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md) class and all associations in which it is referenced.

This method is inherited from the **CIM\_iSCSIConfigurationService** class.

## Syntax


```mof
uint32 DeleteiSCSIProtocolEndpoint(
  [in] CIM_iSCSIProtocolEndpoint Ref iSCSIPort
);
```



## Parameters

<dl> <dt>

*iSCSIPort* \[in\]
</dt> <dd>

Specifies the **CIM\_iSCSIProtocolEndpoint** instance to be deleted.

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
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_iSCSIConfigurationService**](msiscsitarget-iscsiconfigurationservice.md)
</dt> </dl>

 

 





