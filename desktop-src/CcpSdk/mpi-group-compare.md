---
Description: 'Compares two groups for member equality.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2549da8a-673e-4ac3-8985-e5b49796582c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Group\_compare function'
---

# MPI\_Group\_compare function

Compares two groups for member equality.

## Syntax


```C++
int MPIAPI MPI_Group_compare(
        MPI_Group group1,
        MPI_Group group2,
  _Out_ int       *result
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

*result* \[out\]
</dt> <dd>

On return, points to an integer that indicates the results of the comparison.

<dt>

<span id="MPI_IDENT"></span><span id="mpi_ident"></span>

<span id="MPI_IDENT"></span><span id="mpi_ident"></span>****MPI\_IDENT****


</dt> <dd>

Indicates that the group members and group order is exactly the same in both groups. For example, the function returns this value if group1 and group2 are the same handle.

</dd> <dt>

<span id="MPI_SIMILAR"></span><span id="mpi_similar"></span>

<span id="MPI_SIMILAR"></span><span id="mpi_similar"></span>****MPI\_SIMILAR****


</dt> <dd>

Indicates that the group members are the same but the order is different.

</dd> <dt>

<span id="MPI_UNEQUAL"></span><span id="mpi_unequal"></span>

<span id="MPI_UNEQUAL"></span><span id="mpi_unequal"></span>****MPI\_UNEQUAL****


</dt> <dd>

Indicates that the handles are for different objects.

</dd> </dl> </dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_GROUP_COMPARE(GROUP1, GROUP2, RESULT, IERROR)
    INTEGER GROUP1, GROUP2, RESULT, IERROR
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

 

 




