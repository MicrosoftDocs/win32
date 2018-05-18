---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6d87963c-d013-4944-bd45-78c016477969'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Cart\_create function'
---

# MPI\_Cart\_create function

TBD

## Syntax


```C++
int MPIAPI MPI_Cart_create(
        MPI_Comm              comm_old,
        int                   ndims,
        _In_count_(ndims) int *dims,
        _In_count_(ndims) int *periods,
        int                   reorder,
  _Out_ MPI_Comm              *comm_cart
);
```



## Parameters

<dl> <dt>

*comm\_old* 
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

*reorder* 
</dt> <dd>

TBD

</dd> <dt>

*comm\_cart* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_CART_CREATE(COMM_OLD, NDIMS, DIMS, PERIODS, REORDER, COMM_CART, IERROR)
    INTEGER COMM_OLD, NDIMS, DIMS(*), COMM_CART, IERROR
    LOGICAL PERIODS(*), REORDER
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

 

 




