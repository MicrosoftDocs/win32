---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9C4B9B43-3569-4252-8284-5DBE1229915D'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Testany function'
---

# MPI\_Testany function

TBD

## Syntax


```C++
int MPIAPI MPI_Testany(
        int                              count,
        _Inout_count_(count) MPI_Request *array_of_requests,
  _Out_ int                              *index,
  _Out_ MPI_Status                       *status
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of entries in *array\_of\_requests* parameter.

</dd> <dt>

*array\_of\_requests* 
</dt> <dd>

An array of **MPI\_Request** handles of outstanding operations.

</dd> <dt>

*index* \[out\]
</dt> <dd>

A pointer to an integer indicating the index in the *array\_of\_requests* parameter of the operation that completed. The array is indexed from zero in C, and from one in Fortran.

</dd> <dt>

*status* \[out\]
</dt> <dd>

A pointer to an [**MPI\_Status**](mpi-status.md) object describing the completed operation.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_TESTANY(COUNT, ARRAY_OF_REQUESTS, INDEX, FLAG, STATUS, IERROR) LOGICAL FLAG
    INTEGER COUNT, ARRAY_OF_REQUESTS(*), INDEX, STATUS(MPI_STATUS_SIZE), IERROR
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

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> </dl>

 

 




