---
Description: 'Creates a new group from the intersection of two existing groups.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '06b3f54f-5260-49f6-a5f1-81358daa5413'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_intersection function'
---

# MPI\_Group\_intersection function

Creates a new group from the intersection of two existing groups.

## Syntax


```C++
int MPIAPI MPI_Group_intersection(
        MPI_Group group1,
        MPI_Group group2,
  _Out_ MPI_Group *newgroup
);
```



## Parameters

<dl> <dt>

*group1* 
</dt> <dd>

The first group.

</dd> <dt>

*group2* 
</dt> <dd>

The second group.

</dd> <dt>

*newgroup* \[out\]
</dt> <dd>

A pointer to a handle that represents a new group with those elements that are present in both groups. The function returns **MPI\_GROUP\_EMPTY** if the new group is empty.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_INTERSECTION(GROUP1, GROUP2, NEWGROUP, IERROR)
    INTEGER GROUP1, GROUP2, NEWGROUP, IERROR 
```

## Remarks

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

[**MPI\_Comm\_group**](mpi-comm-group.md)
</dt> </dl>

 

 




