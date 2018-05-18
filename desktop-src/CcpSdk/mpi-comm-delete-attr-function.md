---
Description: 'MPI\_Comm\_delete\_attr\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd8b778cb-c354-4361-8d7a-0dc0f3209cdf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_delete\_attr\_function function'
---

# MPI\_Comm\_delete\_attr\_function function

**MPI\_Comm\_delete\_attr\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Comm_delete_attr_function(
           MPI_Comm comm,
           int      comm_keyval,
  _In_     void     *attribute_val,
  _In_opt_ void     *extra_state
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*comm\_keyval* 
</dt> <dd>

TBD

</dd> <dt>

*attribute\_val* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*extra\_state* \[in, optional\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
SUBROUTINE COMM_DELETE_ATTR_FUNCTION(COMM, COMM_KEYVAL, ATTRIBUTE_VAL,
            EXTRA_STATE, IERROR)
    INTEGER COMM, COMM_KEYVAL, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) ATTRIBUTE_VAL, EXTRA_STATE
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

[MPI Caching Functions](mpi-caching-functions.md)
</dt> <dt>

[**MPI\_Comm\_create\_keyval**](mpi-comm-create-keyval.md)
</dt> </dl>

 

 




