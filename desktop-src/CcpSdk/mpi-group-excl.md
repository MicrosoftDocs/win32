---
Description: 'A group constructor that is used to define a new group by deleting ranks from an existing group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd5b17422-4ff1-4c64-ba0e-72d8365f066b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_excl function'
---

# MPI\_Group\_excl function

A group constructor that is used to define a new group by deleting ranks from an existing group.

## Syntax


```C++
int MPIAPI MPI_Group_excl(
        MPI_Group         group,
        int               n,
        _In_count_(n) int *ranks,
  _Out_ MPI_Group         *newgroup
);
```



## Parameters

<dl> <dt>

*group* 
</dt> <dd>

The existing group.

</dd> <dt>

*n* 
</dt> <dd>

The number of elements in the *ranks* parameter.

</dd> <dt>

*ranks* 
</dt> <dd>

The arrays of processes in *group* that are not to appear in *newgroup*. The specified ranks must be valid in the existing group. Each element in the array must be distinct. If the array is empty then the new group will be identical to the existing group.

</dd> <dt>

*newgroup* \[out\]
</dt> <dd>

A pointer to a handle that represents the new group that is derived from the existing group. The order of the existing group is preserved in the new group.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_EXCL(GROUP, N, RANKS, NEWGROUP, IERROR)
    INTEGER GROUP, N, RANKS(*), NEWGROUP, IERROR
```

## Remarks

This function creates a new group of processes that is derived by removing specified processes from an existing group while preserving the order of the ranks in the group.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Group Functions](mpi-group-functions.md)
</dt> </dl>

 

 




