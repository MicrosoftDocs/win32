---
title: Reset method of the CIM\_SCSIProtocolController class
description: Requests a reset of the LogicalDevice.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3924e4dd-21d4-4b7a-ba62-078e2f39199c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Reset method iSCSI Software Target API", "Reset method iSCSI Software Target API , CIM_SCSIProtocolController class", "CIM_SCSIProtocolController class iSCSI Software Target API , Reset method"]
topic_type:
- apiref
api_name:
- CIM_SCSIProtocolController.Reset
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# Reset method of the CIM\_SCSIProtocolController class

Requests a reset of the LogicalDevice. The return value should be 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

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

[**CIM\_SCSIProtocolController**](cim-scsiprotocolcontroller.md)
</dt> </dl>

 

 





