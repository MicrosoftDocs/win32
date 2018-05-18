---
Description: 'Waits until at least one of the operations that is associated with active handles in the list has finished, or the call is interrupted by another thread that calls MSMPI\_Queuelock\_acquire.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '42CB465D-3923-45C2-BF91-9E4B9308BF59'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MSMPI\_Waitsome\_interruptible function'
---

# MSMPI\_Waitsome\_interruptible function

Waits until at least one of the operations that is associated with active handles in the list has finished, or the call is interrupted by another thread that calls [**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md).

## Syntax


```C++
int MPIAPI MSMPI_Waitsome_interruptible(
        int                                         incount,
        _Inout_count_(incount) MPI_Request          array_of_requests[],
  _Out_ int                                         *outcount,
        _Out_cap_post_count_(incount,*outcount) int array_of_indices[],
        _Out_cap_post_count_(incount,*outcount) int array_of_statuses[]
);
```



## Parameters

<dl> <dt>

*incount* 
</dt> <dd>

The number of requests in the array *array\_of\_requests*.

</dd> <dt>

*array\_of\_requests* 
</dt> <dd>

Array of request handles of the operations on which to wait for completion. If a request handle was allocated by a nonblocking communication function, then it is deallocated, and the associated handle is set to **MPI\_REQUEST\_NULL**.

</dd> <dt>

*outcount* \[out\]
</dt> <dd>

The number of requests that is specified in the *array\_of\_requests* parameter that are completed and the number of elements in the *array\_of\_indices* and *array\_of\_statuses* arrays.

If the *array\_of\_requests* contains no active handles, then the function returns immediately with the *outcount* parameter set to **MPI\_UNDEFINED**.

If this function is interrupted before any requests are completed, then the call returns with the *outcount* parameter set to zero.

</dd> <dt>

*array\_of\_indices* 
</dt> <dd>

Returns the indices within the *array\_of\_requests* parameter of the operations that are completed. Array indexes are zero-based in C and one-based in Fortran.

</dd> <dt>

*array\_of\_statuses* 
</dt> <dd>

Returns the status of the operations that are completed. The elements of this array correspond to the elements of the *array\_of\_indices* array.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

If the function returns an error other than **MPI\_ERR\_IN\_STATUS**, it does not update the error fields of the statuses in the *array\_of\_statuses* parameter.

## Remarks

In a multi-threaded environment, users must obtain the global Microsoft MPI lock by using the [**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md) function before they call **MSMPI\_Waitsome\_interruptible**. This function is interrupted when another thread calls the **MSMPI\_Queuelock\_acquire** function in order to access the MPI library.

This function is an extension to the standard.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> <dt>

[**MSMPI\_Lock\_queue**](msmpi-lock-queue.md)
</dt> <dt>

[**MSMPI\_Queuelock\_acquire**](msmpi-queuelock-acquire.md)
</dt> <dt>

[**MSMPI\_Queuelock\_release**](msmpi-queuelock-release.md)
</dt> <dt>

[**MPI\_Waitsome**](mpi-waitsome.md)
</dt> </dl>

 

 




