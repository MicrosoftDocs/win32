---
Description: 'Frees a communicator that is allocated with the MPI\_Comm\_dup, MPI\_Comm\_create, or MPI\_Comm\_split functions.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fd2c2e53-09dc-4438-bec8-9c4384db4497'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_free function'
---

# MPI\_Comm\_free function

Frees a communicator that is allocated with the [**MPI\_Comm\_dup**](mpi-comm-dup.md), [**MPI\_Comm\_create**](mpi-comm-create.md), or [**MPI\_Comm\_split**](mpi-comm-split.md) functions.

## Syntax


```C++
int MPIAPI MPI_Comm_free(
   _Inout_ MPI_Comm *comm
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

The pointer to a communicator handle to free.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_COMM_FREE(COMM,IERROR)
    INTEGER COMM, IERROR
```

## Remarks

This collective operation marks the communication object for deallocation. The handle is set to **MPI\_COMM\_NULL**. Any pending operations that use this communicator finish normally. The object is not deallocated until there are no active references to it.

This function applies to both intracommunicators and intercommunicators.

The delete callback functions for all cached attributes are called in an indeterminate order.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Communicator Functions](mpi-communicator-functions.md)
</dt> <dt>

[**MPI\_Comm\_create**](mpi-comm-create.md)
</dt> <dt>

[**MPI\_Comm\_split**](mpi-comm-split.md)
</dt> <dt>

[**MPI\_Comm\_dup**](mpi-comm-dup.md)
</dt> </dl>

 

 




