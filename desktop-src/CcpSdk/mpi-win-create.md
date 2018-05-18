---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fccf3c21-8840-4de4-8d97-e8bb778771e2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Win\_create function'
---

# MPI\_Win\_create function

TBD

## Syntax


```C++
int MPIAPI MPI_Win_create(
  _In_  void     *base,
        MPI_Aint size,
        int      disp_unit,
        MPI_Info info,
        MPI_Comm comm,
  _Out_ MPI_Win  *win
);
```



## Parameters

<dl> <dt>

*base* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*size* 
</dt> <dd>

TBD

</dd> <dt>

*disp\_unit* 
</dt> <dd>

TBD

</dd> <dt>

*info* 
</dt> <dd>

TBD

</dd> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*win* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_WIN_CREATE(BASE, SIZE, DISP_UNIT, INFO, COMM, WIN, IERROR)
    <type> BASE(*)
    INTEGER(KIND=MPI_ADDRESS_KIND) SIZE
    INTEGER DISP_UNIT, INFO, COMM, WIN, IERROR
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

 

 




