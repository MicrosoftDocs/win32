---
Description: 'Closes the connection between the application and the HPC Job Scheduler Service.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5273DF16-E49F-438C-B4D1-AA55ED62DA43'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::Close method'
---

# IScheduler::Close method

Closes the connection between the application and the HPC Job Scheduler Service.

## Syntax


```C++
HRESULT Close();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::Connect**](ischeduler-connect.md)
</dt> </dl>

 

 




