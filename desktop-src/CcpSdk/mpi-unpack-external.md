---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6b96b349-619d-4ebd-b33a-a647c5e179ea'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Unpack\_external function'
---

# MPI\_Unpack\_external function

TBD

## Syntax


```C++
int MPIAPI MPI_Unpack_external(
        _In_z_ char                 *datarep,
        _In_bytecount_(insize) void *inbuf,
        MPI_Aint                    insize,
        _Inout_ MPI_Aint            *position,
  _Out_ void                        *outbuf,
        int                         outcount,
        MPI_Datatype                datatype
);
```



## Parameters

<dl> <dt>

*datarep* 
</dt> <dd>

TBD

</dd> <dt>

*inbuf* 
</dt> <dd>

TBD

</dd> <dt>

*insize* 
</dt> <dd>

TBD

</dd> <dt>

*position* 
</dt> <dd>

TBD

</dd> <dt>

*outbuf* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*outcount* 
</dt> <dd>

TBD

</dd> <dt>

*datatype* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_UNPACK_EXTERNAL(DATAREP, INBUF, INSIZE, POSITION, OUTBUF, OUTCOUNT,
            DATATYPE, IERROR)
    INTEGER OUTCOUNT, DATATYPE, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) INSIZE, POSITION
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

 

 




