---
Description: 'Determines the relative numbering of the same processes in two different groups.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3c93c90e-2c99-4e37-8662-c7adea21f291'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_translate\_ranks function'
---

# MPI\_Group\_translate\_ranks function

Determines the relative numbering of the same processes in two different groups.

## Syntax


```C++
int MPIAPI MPI_Group_translate_ranks(
        MPI_Group         group1,
        int               n,
        _In_count_(n) int *ranks1,
        MPI_Group         group2,
  _Out_ int               *ranks2
);
```



## Parameters

<dl> <dt>

*group1* 
</dt> <dd>

The first group.

</dd> <dt>

*n* 
</dt> <dd>

The number or ranks in the *ranks1* and *ranks2* parameter arrays.

</dd> <dt>

*ranks1* 
</dt> <dd>

Zero or more valid ranks in the first group.

> [!Note]  
> The **MPI\_PROC\_NULL** constant is valid for this parameter. The corresponding rank that is returned in the *ranks2* parameter is also **MPI\_PROC\_NULL**.

 

</dd> <dt>

*group2* 
</dt> <dd>

The second group.

</dd> <dt>

*ranks2* \[out\]
</dt> <dd>

On return, points to the corresponding ranks in the second group. The value **MPI\_UNDEFINED** indicates that a process is in the first group, but not the second.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_TRANSLATE_RANKS( GROUP1, N, RANKS1, GROUP2, RANKS2, IERROR)
    INTEGER GROUP1, N, RANKS1(*), GROUP2, RANKS2(*), IERROR
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

[MPI Group Functions](mpi-group-functions.md)
</dt> <dt>

[**MPI\_Group\_incl**](mpi-group-incl.md)
</dt> </dl>

 

 




