---
Description: 'This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the MPI\_Type\_get\_extent function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8efc0ccd-3056-46f0-8327-514b9be41d84'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_ub function'
---

# MPI\_Type\_ub function

This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the [**MPI\_Type\_get\_extent**](mpi-type-get-extent.md) function.

## Syntax


```C++
int
MPIAPI MPI_Type_ub(
        MPI_Datatype datatype,
  _Out_ MPI_Aint     *displacement
);
```



## Parameters

<dl> <dt>

*datatype* 
</dt> <dd>

TBD

</dd> <dt>

*displacement* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
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

[MPI Miscellaneous Functions](mpi-miscellaneous-functions.md)
</dt> <dt>

[**MPI\_Type\_get\_extent**](mpi-type-get-extent.md)
</dt> </dl>

 

 




