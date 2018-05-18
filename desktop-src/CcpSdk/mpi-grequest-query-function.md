---
Description: 'MPI\_Grequest\_query\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5b15fa89-832a-428d-87b7-efd393a20ea1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Grequest\_query\_function callback function'
---

# MPI\_Grequest\_query\_function callback function

**MPI\_Grequest\_query\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Grequest_query_function(
  _In_opt_ void       *extra_state,
  _Out_    MPI_Status *status
);
```



## Parameters

<dl> <dt>

*extra\_state* \[in, optional\]
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
SUBROUTINE GREQUEST_QUERY_FUNCTION(EXTRA_STATE, STATUS, IERROR)
    INTEGER STATUS(MPI_STATUS_SIZE), IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) EXTRA_STATE
```

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |



## See also

<dl> <dt>

[MPI External Functions](mpi-external-functions.md)
</dt> <dt>

[**MPI\_Grequest\_start**](mpi-grequest-start.md)
</dt> </dl>

 

 




