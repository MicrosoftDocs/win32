---
Description: 'MPI\_Grequest\_cancel\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '185973fe-26d2-4271-a581-df43908eb227'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Grequest\_cancel\_function callback function'
---

# MPI\_Grequest\_cancel\_function callback function

**MPI\_Grequest\_cancel\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Grequest_cancel_function(
  _In_opt_ void *extra_state,
           int  complete
);
```



## Parameters

<dl> <dt>

*extra\_state* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*complete* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
SUBROUTINE GREQUEST_CANCEL_FUNCTION(EXTRA_STATE, COMPLETE, IERROR)
    INTEGER IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) EXTRA_STATE
    LOGICAL COMPLETE
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

 

 




