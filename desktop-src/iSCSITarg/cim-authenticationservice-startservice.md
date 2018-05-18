---
title: StartService method of the CIM\_AuthenticationService class
description: The StartService method places the Service in the started state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7f43b22c-6057-48ec-b2a3-dd252a991904'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["StartService method iSCSI Software Target API", "StartService method iSCSI Software Target API , CIM_AuthenticationService class", "CIM_AuthenticationService class iSCSI Software Target API , StartService method"]
topic_type:
- apiref
api_name:
- CIM_AuthenticationService.StartService
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# StartService method of the CIM\_AuthenticationService class

The StartService method places the Service in the started state. Note that the function of this method overlaps with the RequestedState property. RequestedState was added to the model to maintain a record (such as a persisted value) of the last state request. Invoking the StartService method should set the RequestedState property appropriately. The method returns an integer value of 0 if the Service was successfully started, 1 if the request is not supported, and any other number to indicate an error. In a subclass, the set of possible return codes could be specified using a ValueMap qualifier on the method. The strings to which the ValueMap contents are translated can also be specified in the subclass as a Values array qualifier. Note: The semantics of this method overlap with the RequestStateChange method that is inherited from EnabledLogicalElement. This method is maintained because it has been widely implemented, and its simple "start" semantics are convenient to use.

## Syntax


```mof
uint32 StartService();
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

[**CIM\_AuthenticationService**](cim-authenticationservice.md)
</dt> </dl>

 

 





