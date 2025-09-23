---
description: Requests a reset of the LogicalDevice.
ms.assetid: d048be64-fa0c-4006-b0a9-58591006bdca
title: Reset method of the CIM\_NetworkPort class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Reset method of the CIM\_NetworkPort class

Requests a reset of the LogicalDevice. The return value should be 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are \\'translated\\' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

TBD

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_NetworkPort**](cim-networkport.md)
</dt> </dl>

 

 




