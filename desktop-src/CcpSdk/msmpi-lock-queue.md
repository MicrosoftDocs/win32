---
Description: 'An opaque structure representing a thread in the Microsoft MPI lock queue.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'F33F11EA-F1D9-4E3C-AB02-A810F19CA02D'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MSMPI\_Lock\_queue structure'
---

# MSMPI\_Lock\_queue structure

An opaque structure representing a thread in the Microsoft MPI lock queue.

## Syntax


```C++
typedef struct _MSMPI_Lock_queue {
  volatile struct _MSMPI_LOCK_QUEUE  *next;
  volatile  MPI_Aint                flags;
} MSMPI_Lock_queue, *PMSMPI_Lock_queue;
```



## Members

<dl> <dt>

**next**
</dt> <dd>

Points to the next entry in the lock queue.

</dd> <dt>

**flags**
</dt> <dd>

A flag used by the lock queue implementation for synchronization.

</dd> </dl>

## Remarks

Each thread calling the [**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md) creates a unique instance of a **MSMPI\_Lock\_queue** structure. We recommend that you allocate the **MSMPI\_Lock\_queue** structure on the thread’s stack.

> \[!Important\]  
> This structure must be treated as opaque by callers.

 

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |



## See also

<dl> <dt>

[MPI Structs](mpi-structs.md)
</dt> <dt>

[**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md)
</dt> <dt>

[**MSMPI\_Queuelock\_release**](msmpi-queuelock-release.md)
</dt> </dl>

 

 




