---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2509A007-140B-45B5-93B0-60A8987635B8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Testall function'
---

# MPI\_Testall function

TBD

## Syntax


```C++
int MPIAPI MPI_Testall(
   int                              count,
   _Inout_count_(count) MPI_Request *array_of_requests,
   _Out_cap_(count) MPI_Status      *array_of_statuses
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of entries in *array\_of\_requests* parameter.

</dd> <dt>

*array\_of\_requests* 
</dt> <dd>

An array of **MPI\_Request** handles of outstanding operations.

</dd> <dt>

*array\_of\_statuses* 
</dt> <dd>

An array of [**MPI\_Status**](mpi-status.md) objects describing the completed operations. Might be **MPI\_STATUSES\_IGNORE** if no status information is desired.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

Returns **MPI\_ERR\_IN\_STATUS** if one or more operations complete in error. The status of failed operations is returned in the corresponding entry in the *array\_of\_statuses* parameter.

In Fortran the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_TESTALL(COUNT, ARRAY_OF_REQUESTS, FLAG, ARRAY_OF_STATUSES, IERROR)
    LOGICAL FLAG
    INTEGER COUNT, ARRAY_OF_REQUESTS(*),
    ARRAY_OF_STATUSES(MPI_STATUS_SIZE,*), IERROR
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

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> </dl>

 

 




