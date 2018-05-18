---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '59ada82e-1178-4059-bc07-3f0426a62297'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_create\_darray function'
---

# MPI\_Type\_create\_darray function

TBD

## Syntax


```C++
int MPIAPI MPI_Type_create_darray(
        int                   size,
        int                   rank,
        int                   ndims,
        _In_count_(ndims) int array_of_gszies[],
        _In_count_(ndims) int array_of_distribs[],
        _In_count_(ndims) int array_of_dargs[],
        _In_count_(ndims) int array_of_psizes[],
        int                   order,
        MPI_Datatype          oldtype,
  _Out_ MPI_Datatype          *newtype
);
```



## Parameters

<dl> <dt>

*size* 
</dt> <dd>

TBD

</dd> <dt>

*rank* 
</dt> <dd>

TBD

</dd> <dt>

*ndims* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_gszies* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_distribs* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_dargs* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_psizes* 
</dt> <dd>

TBD

</dd> <dt>

*order* 
</dt> <dd>

TBD

</dd> <dt>

*oldtype* 
</dt> <dd>

TBD

</dd> <dt>

*newtype* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_TYPE_CREATE_DARRAY(SIZE, RANK, NDIMS, ARRAY_OF_GSIZES,
        ARRAY_OF_DISTRIBS, ARRAY_OF_DARGS, ARRAY_OF_PSIZES, ORDER,
        OLDTYPE, NEWTYPE, IERROR)
    INTEGER SIZE, RANK, NDIMS, ARRAY_OF_GSIZES(*), ARRAY_OF_DISTRIBS(*),
    ARRAY_OF_DARGS(*), ARRAY_OF_PSIZES(*), ORDER, OLDTYPE, NEWTYPE, IERROR
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

[MPI Datatype Functions](mpi-datatype-functions.md)
</dt> </dl>

 

 




