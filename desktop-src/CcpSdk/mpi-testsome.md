---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0cc7936e-e68b-4693-98a8-53d52b05d4b2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Testsome function'
---

# MPI\_Testsome function

TBD

## Syntax


```C++
int MPIAPI MPI_Testsome(
        int                                                incount,
        _Inout_count_(incount) MPI_Request                 *array_of_requests,
  _Out_ int                                                *outcount,
        _Out_cap_post_count_(incount,*outcount) int        *array_of_indices,
        _Out_cap_post_count_(incount,*outcount) MPI_Status *array_of_statuses
);
```



## Parameters

<dl> <dt>

*incount* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_requests* 
</dt> <dd>

TBD

</dd> <dt>

*outcount* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_indices* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_statuses* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_TESTSOME(INCOUNT, ARRAY_OF_REQUESTS, OUTCOUNT, ARRAY_OF_INDICES, ARRAY_OF_STATUSES, IERROR)
    INTEGER INCOUNT, ARRAY_OF_REQUESTS(*), OUTCOUNT, ARRAY_OF_INDICES(*),
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

 

 




