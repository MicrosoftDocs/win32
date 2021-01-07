---
description: Stops the guest service.
ms.assetid: 67FFA46C-0B61-4845-A617-BA10F4D42CBC
title: Msvm_GuestService::StopService method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_GuestService.StopService
api_type: 
- COM
api_location: 
- vmms.exe
---

# Msvm\_GuestService::StopService method

Stops the guest service.

## Syntax


```C++
uint32 StopService();
```



## Parameters

This method has no parameters.

## Return value

This method returns one of the following values.



| Return code/value                                                                                                                                             | Description         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl> | Success.<br/> |
| <dl> <dt>**Not supported**</dt> <dt>1</dt> </dl>           |                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | \\\\Root\\Virtualization\\V2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_GuestService**](msvm-guestservice.md)
</dt> </dl>

 

 




