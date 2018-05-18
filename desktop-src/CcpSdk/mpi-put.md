---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3a25a0d7-eb69-4377-a9ea-4dd89939b798'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Put function'
---

# MPI\_Put function

TBD

## Syntax


```C++
int MPIAPI MPI_Put(
  _In_ void         *origin_addr,
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

*origin\_addr* \[in\]
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
MPI_PUT(ORIGIN_ADDR, ORIGIN_COUNT, ORIGIN_DATATYPE, TARGET_RANK,
            TARGET_DISP, TARGET_COUNT, TARGET_DATATYPE, WIN, IERROR)
    <type> ORIGIN_ADDR(*)
    INTEGER(KIND=MPI_ADDRESS_KIND) TARGET_DISP
    INTEGER ORIGIN_COUNT, ORIGIN_DATATYPE, TARGET_RANK, TARGET_COUNT,
    TARGET_DATATYPE, WIN, IERROR
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

 

 




