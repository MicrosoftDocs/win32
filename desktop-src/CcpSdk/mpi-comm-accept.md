---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '12ede4b0-e249-4e21-a469-b72bef0f3c55'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_accept function'
---

# MPI\_Comm\_accept function

TBD

## Syntax


```C++
int MPIAPI MPI_Comm_accept(
  _In_  char     *port_name,
        MPI_Info info,
        int      root,
        MPI_Comm comm,
  _Out_ MPI_Comm *newcomm
);
```



## Parameters

<dl> <dt>

*port\_name* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*info* 
</dt> <dd>

TBD

</dd> <dt>

*root* 
</dt> <dd>

TBD

</dd> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*newcomm* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_COMM_ACCEPT(PORT_NAME, INFO, ROOT, COMM, NEWCOMM, IERROR)
    CHARACTER*(*) PORT_NAME
    INTEGER INFO, ROOT, COMM, NEWCOMM, IERROR
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

[MPI Process Management Functions](mpi-process-management-functions.md)
</dt> </dl>

 

 




