---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e87295c3-6e39-4b47-aa6b-2398b6d3508a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Grequest\_start function'
---

# MPI\_Grequest\_start function

TBD

## Syntax


```C++
int MPIAPI MPI_Grequest_start(
  _In_     MPI_Grequest_query_function  *query_fn,
  _In_     MPI_Grequest_free_function   *free_fn,
  _In_     MPI_Grequest_cancel_function *cancel_fn,
  _In_opt_ void                         *extra_state,
  _Out_    MPI_Request                  *request
);
```



## Parameters

<dl> <dt>

*query\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*free\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*cancel\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*extra\_state* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*request* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_GREQUEST_START(QUERY_FN, FREE_FN, CANCEL_FN, EXTRA_STATE, REQUEST, IERROR)
    INTEGER REQUEST, IERROR
    EXTERNAL QUERY_FN, FREE_FN, CANCEL_FN
    INTEGER (KIND=MPI_ADDRESS_KIND) EXTRA_STATE
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

[MPI External Functions](mpi-external-functions.md)
</dt> <dt>

[*MPI\_Grequest\_query\_function*](mpi-grequest-query-function.md)
</dt> <dt>

[*MPI\_Grequest\_free\_function*](mpi-grequest-free-function.md)
</dt> <dt>

[*MPI\_Grequest\_cancel\_function*](mpi-grequest-cancel-function.md)
</dt> </dl>

 

 




