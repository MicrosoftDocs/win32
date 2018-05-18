---
title: RestoreProperties method of the CIM\_EthernetPort class
description: Requests that the Device re-establish its configuration, setup and/or state information from a backing store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bd652c4c-31b9-4f24-b381-73702cbd1380'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RestoreProperties method iSCSI Software Target API", "RestoreProperties method iSCSI Software Target API , CIM_EthernetPort class", "CIM_EthernetPort class iSCSI Software Target API , RestoreProperties method"]
topic_type:
- apiref
api_name:
- CIM_EthernetPort.RestoreProperties
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# RestoreProperties method of the CIM\_EthernetPort class

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_EthernetPort**](cim-ethernetport.md)
</dt> </dl>

 

 





