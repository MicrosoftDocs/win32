---
Description: 'Completes multiple outstanding operations.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '89393f53-3b4b-4427-9c66-a0d2732b56ed'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Waitall function'
---

# MPI\_Waitall function

Completes multiple outstanding operations.

## Syntax


```C++
int MPIAPI MPI_Waitall(
   int                              count,
   _Inout_count_(count) MPI_Request *array_of_requests,
   _Out_cap_(count) MPI_Status      *array_of_statuses
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

*array\_of\_statuses* 
</dt> <dd>

An array of [**MPI\_Status**](mpi-status.md) objects that describe the completed operations. It might be **MPI\_STATUSES\_IGNORE** if no status information is requested.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

Returns **MPI\_ERR\_IN\_STATUS** if one or more operations are completed in error. The status of failed operations is returned in the corresponding entry in the *array\_of\_statuses* parameter.

In Fortran the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_WAITALL(COUNT, ARRAY_OF_REQUESTS, INDEX, STATUS, IERROR)
    INTEGER COUNT, ARRAY_OF_REQUESTS, INDEX, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

This function is a non-local operation, successful completion might depend on matching operations at other processes.

A call to **MPI\_Waitall** returns when all of the operations that are associated with active requests in the *array\_of\_requests* array are completed. Any entries that are associated with persistent communication operations result in the persistent request are marked as inactive. Other operations are deallocated, and their corresponding entries in *array\_of\_requests* are set to **MPI\_REQUEST\_NULL**.

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

[**MPI\_Testall**](mpi-testall.md)
</dt> <dt>

[**MPI\_Wait**](mpi-wait.md)
</dt> <dt>

[**MPI\_Waitany**](mpi-waitany.md)
</dt> <dt>

[**MPI\_Waitsome**](mpi-waitsome.md)
</dt> <dt>

[**MPI\_Status**](mpi-status.md)
</dt> </dl>

 

 




