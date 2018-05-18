---
Description: 'MPI\_Grequest\_free\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b1a96d01-0a0c-4307-9cf2-68b51426e45e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Grequest\_free\_function callback function'
---

# MPI\_Grequest\_free\_function callback function

**MPI\_Grequest\_free\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Grequest_free_function(
  _In_opt_ void *extra_state
);
```



## Parameters

<dl> <dt>

*extra\_state* \[in, optional\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
SUBROUTINE GREQUEST_FREE_FUNCTION(EXTRA_STATE, IERROR)
    INTEGER IERROR
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

 

 




