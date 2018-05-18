---
Description: 'Initiates barrier synchronization across all members of a group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '92ef641a-b65b-4e3b-8f64-98d9c0810b29'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Barrier function'
---

# MPI\_Barrier function

Initiates barrier synchronization across all members of a group.

## Syntax


```C++
int MPIAPI MPI_Barrier(
  _In_ MPI_Comm comm
);
```



## Parameters

<dl> <dt>

*comm* \[in\]
</dt> <dd>

The communicator to synchronize.

If this is an intracommunicator, the **MPI\_Barrier** function blocks the caller until all group members have called it. The function does not return on any process until all group processes have called the function.

If this is an intercommunicator, the **MPI\_Barrier** function involves two groups. The function returns on processes in one group, group A, only after all members of the other group, group B, have called the function, and vice versa. The function can return for a process before all processes in its own group have called the function.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_BARRIER(COMM, IERROR)
    INTEGER COMM, IERROR
```

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Collective Functions](mpi-collective-functions.md)
</dt> </dl>

 

 




