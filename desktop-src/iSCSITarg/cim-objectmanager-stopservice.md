---
title: StopService method of the CIM\_ObjectManager class
description: The StopService method places the Service in the stopped state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ad08294c-7e07-4e60-99e3-824cdee6aa37'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["StopService method iSCSI Software Target API", "StopService method iSCSI Software Target API , CIM_ObjectManager class", "CIM_ObjectManager class iSCSI Software Target API , StopService method"]
topic_type:
- apiref
api_name:
- CIM_ObjectManager.StopService
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# StopService method of the CIM\_ObjectManager class

The StopService method places the Service in the stopped state. Note that the function of this method overlaps with the RequestedState property. RequestedState was added to the model to maintain a record (such as a persisted value) of the last state request. Invoking the StopService method should set the RequestedState property appropriately. The method returns an integer value of 0 if the Service was successfully stopped, 1 if the request is not supported, and any other number to indicate an error. In a subclass, the set of possible return codes could be specified using a ValueMap qualifier on the method. The strings to which the ValueMap contents are translated can also be specified in the subclass as a Values array qualifier. Note: The semantics of this method overlap with the RequestStateChange method that is inherited from EnabledLogicalElement. This method is maintained because it has been widely implemented, and its simple "stop" semantics are convenient to use.

## Syntax


```mof
uint32 StopService();
```



## Parameters

This method has no parameters.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>              |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ObjectManager**](cim-objectmanager.md)
</dt> </dl>

 

 





