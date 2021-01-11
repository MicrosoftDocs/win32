---
description: Paces the service in the stopped state.
ms.assetid: d7469643-bccc-4f55-b2fc-d2bc2e392d84
title: StopService method of the CIM_Service class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Service.StopService
api_type: 
- COM
api_location: 
- vmms.exe
---

# StopService method of the CIM_Service class (Hyper-V management)

Paces the service in the stopped state.

> [!Note]
>
> The semantics of this method overlap with the **RequestStateChange** method that is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md). This method is maintained because it has been widely implemented, and its simple "stop" semantics are convenient to use.

 

## Syntax


```mof
uint32 StopService();
```



## Parameters

This method has no parameters.

## Return value

Returns a 0 on success; otherwise, returns an error.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 




