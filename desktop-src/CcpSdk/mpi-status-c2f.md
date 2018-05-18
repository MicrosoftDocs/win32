---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2bb2d54f-b801-41a7-a1db-4d792858cc2c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Status\_c2f function'
---

# MPI\_Status\_c2f function

TBD

## Syntax


```C++
int MPIAPI MPI_Status_c2f(
  _In_  MPI_Status *status,
  _Out_ MPI_Fint   *f_status
);
```



## Parameters

<dl> <dt>

*status* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*f\_status* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Miscellaneous Functions](mpi-miscellaneous-functions.md)
</dt> </dl>

 

 




