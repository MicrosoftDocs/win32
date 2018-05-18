---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a79b2c21-bbab-4aeb-b612-8f11796d1512'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Sendrecv function'
---

# MPI\_Sendrecv function

TBD

## Syntax


```C++
int MPIAPI MPI_Sendrecv(
  _In_  void         *sendbuf,
        int          sendcount,
        MPI_Datatype sendtype,
        int          dest,
        int          sendtag,
  _Out_ void         *recvbuf,
        int          recvcount,
        MPI_Datatype recvtype,
        int          source,
        int          recvtag,
        MPI_Comm     comm,
  _Out_ MPI_Status   *status
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*sendcount* 
</dt> <dd>

TBD

</dd> <dt>

*sendtype* 
</dt> <dd>

TBD

</dd> <dt>

*dest* 
</dt> <dd>

TBD

</dd> <dt>

*sendtag* 
</dt> <dd>

TBD

</dd> <dt>

*recvbuf* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*recvcount* 
</dt> <dd>

TBD

</dd> <dt>

*recvtype* 
</dt> <dd>

TBD

</dd> <dt>

*source* 
</dt> <dd>

TBD

</dd> <dt>

*recvtag* 
</dt> <dd>

TBD

</dd> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*status* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_SENDRECV(SENDBUF, SENDCOUNT, SENDTYPE, DEST, SENDTAG, RECVBUF,
        RECVCOUNT, RECVTYPE, SOURCE, RECVTAG, COMM, STATUS, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, DEST, SENDTAG, RECVCOUNT, RECVTYPE,
    SOURCE, RECVTAG, COMM, STATUS(MPI_STATUS_SIZE), IERROR
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

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> </dl>

 

 




