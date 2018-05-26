---
title: StartService method of the MSISCSITARGET\_iSCSIConfigurationService class
description: Places the Service in the started state. Deprecated, instead use the RequestStateChange method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 879992a6-59ed-4386-88c2-8815a29d50e8
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StartService method iSCSI Software Target API
- StartService method iSCSI Software Target API , MSISCSITARGET_iSCSIConfigurationService class
- MSISCSITARGET_iSCSIConfigurationService class iSCSI Software Target API , StartService method
topic_type:
- apiref
api_name:
- MSISCSITARGET_iSCSIConfigurationService.StartService
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StartService method of the MSISCSITARGET\_iSCSIConfigurationService class

Places the Service in the started state. Deprecated, instead use the [**RequestStateChange**](requeststatechange-msiscsitarget-storageconfigurationservice.md) method. Invoking this method should set the **RequestedState** property appropriately.

This method is inherited from the [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) class.

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

<dl> <dt>


</dt> <dd>

0

The Service was successfully stopped.

</dd> <dt>


</dt> <dd>

1

The request is not supported.

</dd> <dt>


</dt> <dd>

2 = *value*

Undefined error.

</dd> </dl>

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
</dt> <dt>

[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)
</dt> </dl>

 

 





