---
Description: 'Releases the Microsoft MPI library global lock.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'C11D4EC4-E2F7-4DF2-A837-6F863A407085'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MSMPI\_Queuelock\_release function'
---

# MSMPI\_Queuelock\_release function

Releases the Microsoft MPI library global lock.

## Syntax


```C++
void MSMPI_Queuelock_release(
  _In_ MSMPI_Lock_queue *queue
);
```



## Parameters

<dl> <dt>

*queue* \[in\]
</dt> <dd>

The lock queue structure that represents the calling thread in the queue. This structure was initialized by using the [**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md) function.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Users of the [**MSMPI\_Waitsome\_interruptible**](msmpi-waitsome-interruptible.md) function should release and re-acquire the lock when the function is interrupted, in order to enable the interrupting threads to run.

This function is an extension to the standard.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> <dt>

[**MSMPI\_Lock\_queue**](msmpi-lock-queue.md)
</dt> <dt>

[**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md)
</dt> <dt>

[**MSMPI\_Waitsome\_interruptible**](msmpi-waitsome-interruptible.md)
</dt> </dl>

 

 




