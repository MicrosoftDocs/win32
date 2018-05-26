---
title: SaveProperties method of the CIM\_EthernetPort class
description: Requests that the Device capture its current configuration, setup and/or state information in a backing store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2cc4eee5-fb85-4531-9eec-e0ca9a28a962
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SaveProperties method iSCSI Software Target API
- SaveProperties method iSCSI Software Target API , CIM_EthernetPort class
- CIM_EthernetPort class iSCSI Software Target API , SaveProperties method
topic_type:
- apiref
api_name:
- CIM_EthernetPort.SaveProperties
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SaveProperties method of the CIM\_EthernetPort class

Requests that the Device capture its current configuration, setup and/or state information in a backing store. The goal would be to use this information at a later time (via the RestoreProperties method), to return a Device to its present "condition". This method may not be supported by all Devices. The method should return 0 if successful, 1 if the request is not supported, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 SaveProperties();
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

[**CIM\_EthernetPort**](cim-ethernetport.md)
</dt> </dl>

 

 





