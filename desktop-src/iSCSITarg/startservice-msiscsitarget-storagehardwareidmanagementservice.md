---
title: StartService method of the MSISCSITARGET\_StorageHardwareIDManagementService class
description: Places the service in the started state. Deprecated. Instead, use the RequestStateChange method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e07dd497-bd2f-43ec-920e-06813b3f4eb3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["StartService method iSCSI Software Target API", "StartService method iSCSI Software Target API , MSISCSITARGET_StorageHardwareIDManagementService class", "MSISCSITARGET_StorageHardwareIDManagementService class iSCSI Software Target API , StartService method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageHardwareIDManagementService.StartService
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# StartService method of the MSISCSITARGET\_StorageHardwareIDManagementService class

Places the service in the started state. Deprecated. Instead, use the [**RequestStateChange**](requeststatechange-msiscsitarget-storagehardwareidmanagementservice.md) method. Invoking this method should set the **RequestedState** property appropriately.

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

The service was successfully stopped.

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**RequestStateChange**](requeststatechange-msiscsitarget-storagehardwareidmanagementservice.md)
</dt> <dt>

[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)
</dt> </dl>

 

 





