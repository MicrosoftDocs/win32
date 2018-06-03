---
title: SetPowerState method of the MicrosoftNLB\_Node class
description: Currently not used by the Network Load Balancing provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 086bd6cf-60f5-4ac5-ab01-d89f91b362b0
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method
- SetPowerState method, MicrosoftNLB_Node class
- MicrosoftNLB_Node class, SetPowerState method
topic_type:
- apiref
api_name:
- MicrosoftNLB_Node.SetPowerState
api_location:
- WlbsProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetPowerState method of the MicrosoftNLB\_Node class

The **SetPowerState** method is inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626) and is currently not used by the Network Load Balancing provider.

## Syntax


```mof
uint32 SetPowerState();
```



## Parameters

This method has no parameters.

## Return value

This method returns a **uint32** set to one of the [standard return values](standard-return-values.md).

## Remarks

This method will fail if called on an instance of a [**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151) object that represents a remote node.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151)
</dt> <dt>

[**MicrosoftNLB\_Node**](microsoftnlb-node.md)
</dt> </dl>

 

 





