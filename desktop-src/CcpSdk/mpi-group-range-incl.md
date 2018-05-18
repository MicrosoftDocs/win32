---
Description: 'A group constructor that is used to define a new group by adding additional sets of ranks to an existing group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c6e95b30-78ad-45a2-adcc-78cf343c8681'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_range\_incl function'
---

# MPI\_Group\_range\_incl function

A group constructor that is used to define a new group by adding additional sets of ranks to an existing group.

## Syntax


```C++
int MPIAPI MPI_Group_range_incl(
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

The number of triplets in array ranges.

</dd> <dt>

*ranges* 
</dt> <dd>

An array of specifications of processes to include in the new group. Each element of the array specifies a range of process in the form of three integers for the first rank, last rank, and stride.

</dd> <dt>

*newgroup* \[out\]
</dt> <dd>

A pointer to a handle that represents the new group. The new group contains the additional sets of ranks. The order is defined by *ranges*.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_RANGE_INCL(GROUP, N, RANGES, NEWGROUP, IERROR)
    INTEGER GROUP, N, RANGES(3,*), NEWGROUP, IERROR
```

## Remarks

If ranges consist of the triplets (first1 , last1, stride1) , ..., (firstn, lastn, striden), then *newgroup* consists of the sequence of processes in *group* with ranks TBD.

Each computed rank must be a valid rank in the new group, and all computed ranks must be distinct. Otherwise, the function returns an error.

> [!Note]  
> Note that you can set *first\[i\]* greater than *last\[i\]*, and *stride\[i\]* can be negative, but it cannot be zero.

 

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

[**MPI\_Group\_incl**](mpi-group-incl.md)
</dt> <dt>

[**MPI\_Comm\_group**](mpi-comm-group.md)
</dt> </dl>

 

 




