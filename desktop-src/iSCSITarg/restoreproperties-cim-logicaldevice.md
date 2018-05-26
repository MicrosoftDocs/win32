---
title: RestoreProperties method of the CIM\_LogicalDevice class
description: Requests that the Device re-establish its configuration, setup and/or state information from a backing store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cf1dc101-ed6f-4204-9c72-67d6f9588ff7
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RestoreProperties method iSCSI Software Target API
- RestoreProperties method iSCSI Software Target API , CIM_LogicalDevice class
- CIM_LogicalDevice class iSCSI Software Target API , RestoreProperties method
topic_type:
- apiref
api_name:
- CIM_LogicalDevice.RestoreProperties
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RestoreProperties method of the CIM\_LogicalDevice class

Requests that the Device re-establish its configuration, setup and/or state information from a backing store. The intent is to capture this information at an earlier time (via the SaveProperties method), and use it to return a Device to this earlier "condition". This method may not be supported by all Devices. The method should return 0 if successful, 1 if the request is not supported, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 RestoreProperties();
```



## Parameters

This method has no parameters.

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

[**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)
</dt> </dl>

 

 





