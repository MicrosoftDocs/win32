---
description: Requests a reset of the LogicalDevice.
ms.assetid: f7655825-3de5-421f-a3e9-97d2f605affd
title: Reset method of the CIM_LogicalDevice class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_LogicalDevice.Reset
api_type: 
- COM
api_location: 
- vmms.exe
---

# Reset method of the CIM_LogicalDevice class (Hyper-V management)

Requests a reset of the LogicalDevice. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 Reset();
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

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 

 




