---
Description: 'Creates a new group from the union of two existing groups.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c68c09cf-212c-45b6-b2d7-f4bbeda3d395'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_union function'
---

# MPI\_Group\_union function

Creates a new group from the union of two existing groups.

## Syntax


```C++
int MPIAPI MPI_Group_union(
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

On return, contains a pointer to a new group that represents all elements in either group.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_UNION(GROUP1, GROUP2, NEWGROUP, IERROR)
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

 

 




