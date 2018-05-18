---
Description: 'Creates a new group that contains a subset of the processes in an existing group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '59def9d7-933a-43e2-8218-1bf874b786da'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_incl function'
---

# MPI\_Group\_incl function

Creates a new group that contains a subset of the processes in an existing group.

## Syntax


```C++
int MPIAPI MPI_Group_incl(
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

The number of elements in the *ranks* parameter and the size of the new group.

</dd> <dt>

*ranks* 
</dt> <dd>

The processes to be included in the new group.

</dd> <dt>

*newgroup* \[out\]
</dt> <dd>

A pointer to a handle that represents the new group, which contains the included processes in the order that they are specified in the *ranks* parameter.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_INCL(GROUP, N, RANKS, NEWGROUP, IERROR)
    INTEGER GROUP, N, RANKS(*), NEWGROUP, IERROR
```

## Remarks

This function can be used to reorder the elements of a group.

This is a local operation. Different processes can define distinct groups. A process can define a group that does not include itself.

The MPI implementation does not provide a mechanism to build a group from scratch, but only from existing groups. The base group, upon which all other groups are defined, can be retrieved by using the [**MPI\_Comm\_group**](mpi-comm-group.md) function. It is the group that is associated with the initial communicator **MPI\_COMM\_WORLD**.

## Requirements



|                    |                                                                                                                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HHPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                            |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                      |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                      |



## See also

<dl> <dt>

[MPI Group Functions](mpi-group-functions.md)
</dt> <dt>

[**MPI\_Comm\_group**](mpi-comm-group.md)
</dt> </dl>

 

 




