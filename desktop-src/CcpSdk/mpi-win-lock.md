---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e5bd3a8b-264f-4156-958f-e325db1c129c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Win\_lock function'
---

# MPI\_Win\_lock function

TBD

## Syntax


```C++
int MPIAPI MPI_Win_lock(
   int     lock_type,
   int     rank,
   int     assert,
   MPI_Win win
);
```



## Parameters

<dl> <dt>

*lock\_type* 
</dt> <dd>

TBD

</dd> <dt>

*rank* 
</dt> <dd>

TBD

</dd> <dt>

*assert* 
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
MPI_WIN_LOCK(LOCK_TYPE, RANK, ASSERT, WIN, IERROR)
    INTEGER LOCK_TYPE, RANK, ASSERT, WIN, IERROR
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

 

 




