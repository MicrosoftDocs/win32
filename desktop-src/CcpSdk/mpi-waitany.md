---
Description: 'Completes one out of several outstanding operations.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bb03d8e6-8af9-43aa-a4b9-c7ff50d6fb22'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Waitany function'
---

# MPI\_Waitany function

Completes one out of several outstanding operations.

## Syntax


```C++
int MPIAPI MPI_Waitany(
        int                              count,
        _Inout_count_(count) MPI_Request *array_of_requests,
  _Out_ int                              *index,
  _Out_ MPI_Status                       *status
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of entries in the *array\_of\_requests* parameter.

</dd> <dt>

*array\_of\_requests* 
</dt> <dd>

An array of **MPI\_Request** handles of outstanding operations.

</dd> <dt>

*index* \[out\]
</dt> <dd>

A pointer to an integer that indicates the index in the *array\_of\_requests* parameter of the operation that is completed. The array is indexed from zero in C, and from one in Fortran.

</dd> <dt>

*status* \[out\]
</dt> <dd>

A pointer to an [**MPI\_Status**](mpi-status.md) object that describes the completed operation.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_WAITANY(COUNT, ARRAY_OF_REQUESTS, INDEX, STATUS, IERROR)
    INTEGER COUNT, ARRAY_OF_REQUESTS, INDEX, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

This function is a non-local operation. Successful completion might depend on matching operations at other processes.

This function returns when one of the operations that is associated with active requests in the *array\_of\_requests* parameter is completed. If more than one outstanding operation is completed, one is arbitrarily chosen. If the completed operation is a persistent communication operation, the persistent request is marked as inactive. A nonpersistent operation is deallocated, and its corresponding entry in the *array\_of\_requests* parameter is set to **MPI\_REQUEST\_NULL**.

Entries in the *array\_of\_requests* parameter can be **MPI\_REQUEST\_NULL** or a handle to an inactive persistent communication request. If the *count* parameter is zero, or all entries in *array\_of\_requests* are **MPI\_REQUEST\_NULL** or inactive persistent communication requests, then the function returns immediately with the *index* parameter set to **MPI\_UNDEFINED** and an empty status.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> <dt>

[**MPI\_Testany**](mpi-testany.md)
</dt> <dt>

[**MPI\_Wait**](mpi-wait.md)
</dt> <dt>

[**MPI\_Waitall**](mpi-waitall.md)
</dt> <dt>

[**MPI\_Waitsome**](mpi-waitsome.md)
</dt> <dt>

[**MPI\_Status**](mpi-status.md)
</dt> </dl>

 

 




