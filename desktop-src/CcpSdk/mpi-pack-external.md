---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c2051da8-9986-49f7-b19b-feb1d45d9a56'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Pack\_external function'
---

# MPI\_Pack\_external function

TBD

## Syntax


```C++
int MPIAPI MPI_Pack_external(
       _In_z_ char                 *datarep,
  _In_ void                        *inbuf,
       int                         incount,
       MPI_Datatype                datatype,
       _Out_bytecap_(outsize) void *outbuf,
       MPI_Aint                    outsize,
       _Inout_ MPI_Aint            *position
);
```



## Parameters

<dl> <dt>

*datarep* 
</dt> <dd>

TBD

</dd> <dt>

*inbuf* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*incount* 
</dt> <dd>

TBD

</dd> <dt>

*datatype* 
</dt> <dd>

TBD

</dd> <dt>

*outbuf* 
</dt> <dd>

TBD

</dd> <dt>

*outsize* 
</dt> <dd>

TBD

</dd> <dt>

*position* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_PACK_EXTERNAL(DATAREP, INBUF, INCOUNT, DATATYPE, OUTBUF, OUTSIZE,
            POSITION, IERROR)
    INTEGER INCOUNT, DATATYPE, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) OUTSIZE, POSITION
    CHARACTER*(*) DATAREP
    <type> INBUF(*), OUTBUF(*)
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

 

 




