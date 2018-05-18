---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6c269257-df91-4101-a042-81bed6f90f7e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Info\_get\_nthkey function'
---

# MPI\_Info\_get\_nthkey function

TBD

## Syntax


```C++
int MPIAPI MPI_Info_get_nthkey(
   MPI_Info                           info,
   int                                n,
   _Out_z_cap_(MPI_MAX_INFO_KEY) char *key
);
```



## Parameters

<dl> <dt>

*info* 
</dt> <dd>

TBD

</dd> <dt>

*n* 
</dt> <dd>

TBD

</dd> <dt>

*key* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_INFO_GET_NTHKEY(INFO, N, KEY, IERROR)
    INTEGER INFO, N, IERROR
    CHARACTER*(*) KEY
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

[MPI Info Object Functions](mpi-info-object-functions.md)
</dt> </dl>

 

 




