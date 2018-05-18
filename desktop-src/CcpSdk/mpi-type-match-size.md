---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2c06213e-42da-4e6f-b8b0-2ac39fcbe3b8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_match\_size function'
---

# MPI\_Type\_match\_size function

TBD

## Syntax


```C++
int MPIAPI MPI_Type_match_size(
        int          typeclass,
        int          size,
  _Out_ MPI_Datatype *type
);
```



## Parameters

<dl> <dt>

*typeclass* 
</dt> <dd>

TBD

</dd> <dt>

*size* 
</dt> <dd>

TBD

</dd> <dt>

*type* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_TYPE_MATCH_SIZE(TYPECLASS, SIZE, DATATYPE, IERROR)
    INTEGER TYPECLASS, SIZE, DATATYPE, IERROR
```

## Requirements



|                    |                                                                                                                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilitiese<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                            |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                      |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                      |



## See also

<dl> <dt>

[MPI Miscellaneous Functions](mpi-miscellaneous-functions.md)
</dt> </dl>

 

 




