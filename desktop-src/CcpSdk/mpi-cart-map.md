---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ef78cb00-255d-48fc-a5b5-01cd2395165d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Cart\_map function'
---

# MPI\_Cart\_map function

TBD

## Syntax


```C++
int MPIAPI MPI_Cart_map(
        MPI_Comm              comm,
        int                   ndims,
        _In_count_(ndims) int *dims,
        _In_count_(ndims) int *periods,
  _Out_ int                   *newrank
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*ndims* 
</dt> <dd>

TBD

</dd> <dt>

*dims* 
</dt> <dd>

TBD

</dd> <dt>

*periods* 
</dt> <dd>

TBD

</dd> <dt>

*newrank* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_CART_MAP(COMM, NDIMS, DIMS, PERIODS, NEWRANK, IERROR)
    INTEGER COMM, NDIMS, DIMS(*), NEWRANK, IERROR
    LOGICAL PERIODS(*)
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

[MPI Process Topology Functions](mpi-process-topology-functions.md)
</dt> </dl>

 

 




