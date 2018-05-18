---
Description: 'Acquires the Microsoft MPI library global lock.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '185CFDF0-FA10-41A8-A8B1-E4C180E8A175'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MSMPI\_Queuelock\_acquire function'
---

# MSMPI\_Queuelock\_acquire function

Acquires the Microsoft MPI library global lock. The lock queue is a First-In-First-Out (FIFO) queue.

## Syntax


```C++
void MSMPI_Queuelock_acquire(
  _Out_ MSMPI_Lock_queue *queue
);
```



## Parameters

<dl> <dt>

*queue* \[out\]
</dt> <dd>

Points to a user-supplied [**MSMPI\_Lock\_queue**](msmpi-lock-queue.md) structure that represents the position of the calling thread in the queue until the user releases the lock by using the [**MSMPI\_Queuelock\_release**](msmpi-queuelock-release.md) function.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The behavior of this function depends on the level of thread support in use. When the thread support is **MPI\_THREAD\_SERIALIZED** or lower, this function acquires the Microsoft MPI global lock, which provides FIFO serialization of callers and interrupts any [**MSMPI\_Waitsome\_interruptible**](msmpi-waitsome-interruptible.md) function calls that are in-progress.

Applications should normally allocate the queue structure on the stack each time they acquire the lock.

To avoid errors when threads use [**MSMPI\_Waitsome\_interruptible**](msmpi-waitsome-interruptible.md) in multi-threaded applications, all threads must acquire the global lock before they call MPI functions.

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

[**MSMPI\_Queuelock\_release**](msmpi-queuelock-release.md)
</dt> <dt>

[**MSMPI\_Waitsome\_interruptible**](msmpi-waitsome-interruptible.md)
</dt> </dl>

 

 




