---
Description: 'Creates a new group by removing processes from an existing group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '635a803a-a5a9-4d1c-a324-602048154f27'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_range\_excl function'
---

# MPI\_Group\_range\_excl function

Creates a new group by removing processes from an existing group.

## Syntax


```C++
int MPIAPI MPI_Group_range_excl(
        MPI_Group         group,
        int               n,
        _In_count_(n) int ranges[][3],
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

The number of ranges of processes to exclude from the new group.

</dd> <dt>

*ranges* 
</dt> <dd>

An array of specifications of processes to exclude from the existing group. Each element of the array specifies a range of process in the form of three integers for the first rank, last rank, and stride.

</dd> <dt>

*newgroup* \[out\]
</dt> <dd>

A pointer to a handle that represents the new group that contains those processes that were not excluded. The order of the group is preserved.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_RANGE_EXCL(GROUP, N, RANGES, NEWGROUP, IERROR)
    INTEGER GROUP, N, RANGES(3,*), NEWGROUP, IERROR
```

## Remarks

Each computed rank must be a valid rank in the existing group and all computed ranks must be distinct; otherwise the function returns an error.

This is a local operation. Different processes can define distinct groups. A process can define a group that does not include itself.

The MPI implementation does not provide a mechanism to build a group from scratch, but only from existing groups. The base group, upon which all other groups are defined, can be retrieved by using the [**MPI\_Comm\_group**](mpi-comm-group.md) function. It is the group that is associated with the initial communicator **MPI\_COMM\_WORLD**.

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

[**MPI\_Group\_excl**](mpi-group-excl.md)
</dt> <dt>

[**MPI\_Comm\_group**](mpi-comm-group.md)
</dt> </dl>

 

 




