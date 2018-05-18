---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7255cdf7-1fdf-4780-9c50-9c7eb8b28297'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Get function'
---

# MPI\_Get function

TBD

## Syntax


```C++
int MPIAPI MPI_Get(
  _Out_ void         *origin_addr,
        int          origin_count,
        MPI_Datatype origin_datatype,
        int          target_rank,
        MPI_Aint     target_disp,
        int          target_count,
        MPI_Datatype datatype,
        MPI_Win      win
);
```



## Parameters

<dl> <dt>

*origin\_addr* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*origin\_count* 
</dt> <dd>

TBD

</dd> <dt>

*origin\_datatype* 
</dt> <dd>

TBD

</dd> <dt>

*target\_rank* 
</dt> <dd>

TBD

</dd> <dt>

*target\_disp* 
</dt> <dd>

TBD

</dd> <dt>

*target\_count* 
</dt> <dd>

TBD

</dd> <dt>

*datatype* 
</dt> <dd>

TBD

</dd> <dt>

*win* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_GET(ORIGIN_ADDR, ORIGIN_COUNT, ORIGIN_DATATYPE, TARGET_RANK,
            TARGET_DISP, TARGET_COUNT, TARGET_DATATYPE, WIN, IERROR)
    <type> ORIGIN_ADDR(*)
    INTEGER(KIND=MPI_ADDRESS_KIND) TARGET_DISP
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

[MPI One-Sided Communications Functions](mpi-one-sided-communications-functions.md)
</dt> </dl>

 

 




