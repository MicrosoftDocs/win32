---
Description: 'Returns the rank of the calling process in the specified group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '34650411-2dd1-447c-bca0-6122f43234cb'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_rank function'
---

# MPI\_Group\_rank function

Returns the rank of the calling process in the specified group.

## Syntax


```C++
int MPIAPI MPI_Group_rank(
        MPI_Group group,
  _Out_ int       *rank
);
```



## Parameters

<dl> <dt>

*group* 
</dt> <dd>

Specifies the group to query.

</dd> <dt>

*rank* \[out\]
</dt> <dd>

A pointer to an integer that, on return, contains the rank of the calling process in the specified group. A value of **MPI\_UNDEFINED** that the calling process is not a member of the specified group.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_RANK(GROUP, RANK, IERROR)
    INTEGER GROUP, RANK, IERROR 
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
</dt> </dl>

 

 




