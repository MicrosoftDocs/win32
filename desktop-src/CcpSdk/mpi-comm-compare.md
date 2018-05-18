---
Description: 'Compares two communicator handles.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '881e2ef6-ad94-413b-82e0-89fe27534419'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_compare function'
---

# MPI\_Comm\_compare function

Compares two communicator handles.

## Syntax


```C++
int MPIAPI MPI_Comm_compare(
        MPI_Comm comm1,
        MPI_Comm comm2,
  _Out_ int      *result
);
```



## Parameters

<dl> <dt>

*comm1* 
</dt> <dd>

A handle for the first communicator to compare.

</dd> <dt>

*comm2* 
</dt> <dd>

A handle for the second communicator to compare.

</dd> <dt>

*result* \[out\]
</dt> <dd>

On return, a pointer to the results of the comparison.

The possible values are.

<dt>

<span id="MPI_IDENT"></span><span id="mpi_ident"></span>

<span id="MPI_IDENT"></span><span id="mpi_ident"></span>****MPI\_IDENT****


</dt> <dd>

Indicates that the two handles are for the same object. The handles reference identical groups and contexts.

</dd> <dt>

<span id="MPI_CONGRUENT"></span><span id="mpi_congruent"></span>

<span id="MPI_CONGRUENT"></span><span id="mpi_congruent"></span>****MPI\_CONGRUENT****


</dt> <dd>

Indicates that the underlying groups have identical members in the same rank order. These communicators differ only by context.

</dd> <dt>

<span id="MPI_SIMILAR"></span><span id="mpi_similar"></span>

<span id="MPI_SIMILAR"></span><span id="mpi_similar"></span>****MPI\_SIMILAR****


</dt> <dd>

Indicates that the underlying groups have identical members, but they are in different rank orders.

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
MPI_COMM_COMPARE(COMM1,COMM2,RESULT,IERROR)
    INTEGER COMM1, COMM1, RESULT, IERROR
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

[MPI Communicator Functions](mpi-communicator-functions.md)
</dt> </dl>

 

 




