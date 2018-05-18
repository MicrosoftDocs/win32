---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0310d14e-ebc8-4131-8467-ee58f04d0020'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Reduce\_local function'
---

# MPI\_Reduce\_local function

TBD

## Syntax


```C++
int MPIAPI MPI_Reduce_local(
  _In_ void         *inbuf,
       _Inout_ void *inoutbuf,
       int          count,
       MPI_Datatype datatype,
       MPI_Op       op
);
```



## Parameters

<dl> <dt>

*inbuf* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*inoutbuf* 
</dt> <dd>

TBD

</dd> <dt>

*count* 
</dt> <dd>

TBD

</dd> <dt>

*datatype* 
</dt> <dd>

TBD

</dd> <dt>

*op* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_REDUCE_LOCAL(INBUF, INOUTBUF, COUNT, DATATYPE, OP, IERROR)
    <type> INBUF(*), INOUTBUF(*)
    INTEGER COUNT, DATATYPE, OP, IERROR
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

[MPI Collective Functions](mpi-collective-functions.md)
</dt> </dl>

 

 




