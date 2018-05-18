---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8575ee33-58a8-45dd-84c7-968f3ffe3fa5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Unpack function'
---

# MPI\_Unpack function

TBD

## Syntax


```C++
int MPIAPI MPI_Unpack(
        _In_bytecount_(insize) void *inbuf,
        int                         insize,
        _Inout_ int                 *position,
  _Out_ void                        *outbuf,
        int                         outcount,
        MPI_Datatype                datatype,
        MPI_Comm                    comm
);
```



## Parameters

<dl> <dt>

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

</dd> <dt>

*comm* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_UNPACK(INBUF, INSIZE, POSITION, OUTBUF, OUTCOUNT, DATATYPE, COMM, IERROR)
    <type> INBUF(*), OUTBUF(*)
    INTEGER INSIZE, POSITION, OUTCOUNT, DATATYPE, COMM, IERROR
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

 

 




