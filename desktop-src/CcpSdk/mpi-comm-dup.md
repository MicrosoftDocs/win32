---
Description: 'Duplicates an existing communicator with associated key values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f23804db-a2b4-478d-8b1d-c628b52e864d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_dup function'
---

# MPI\_Comm\_dup function

Duplicates an existing communicator with associated key values. For each key value, the respective copy callback function determines the attribute value that is associated with this key in the new communicator. The copy callback can, for example, delete the attribute from the new communicator.

## Syntax


```C++
int MPIAPI MPI_Comm_dup(
        MPI_Comm comm,
  _Out_ MPI_Comm *newcomm
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

The communicator to duplicate.

</dd> <dt>

*newcomm* \[out\]
</dt> <dd>

On return, contains a handle to a new communicator. The new communicator has the same group or groups and any copied cached information from the source, but it contains new context information.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_COMM_DUP(COMM,NEWCOMM,IERROR)
    INTEGER COMM, NEWCOMM, IERROR
```

## Remarks

This function creates a duplicate communication space that has the same properties as the original communicator. This includes any attributes and topologies. This function is valid even if there are pending point-to-point communications that involve the source communicator.

A user can call the **MPI\_Comm\_dup** function at the beginning of the parallel process and later free the duplicate communicator by using the [**MPI\_Comm\_free**](mpi-comm-free.md) function. Other models of communicator management are also possible.

This function applies to both intracommunicators and intercommunicators.

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

 

 




