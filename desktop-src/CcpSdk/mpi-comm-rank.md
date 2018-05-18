---
Description: 'Retrieves the rank of the calling process in the group of the specified communicator.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f42f18ed-4a0a-4c4a-b5a8-11bb8ad8a0b9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_rank function'
---

# MPI\_Comm\_rank function

Retrieves the rank of the calling process in the group of the specified communicator.

## Syntax


```C++
int MPIAPI MPI_Comm_rank(
        MPI_Comm comm,
  _Out_ int      *rank
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

The communicator.

</dd> <dt>

*rank* \[out\]
</dt> <dd>

On return, a pointer to the identifier of the calling process within the group of the communicator.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_COMM_RANK(COMM,RANK,IERROR)
    INTEGER COMM, RANK, IERROR
```

## Remarks

This function enables the user to retrieve the process rank with a single function call. Otherwise, it would be necessary to create a temporary group by using the [**MPI\_Comm\_group**](mpi-comm-group.md) function, get the rank in the group by using the [**MPI\_Group\_rank**](mpi-group-rank.md) function, and then free the temporary group by using the [**MPI\_Group\_free**](mpi-group-free.md) function.

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

[**MPI\_Comm\_size**](mpi-comm-size.md)
</dt> </dl>

 

 




