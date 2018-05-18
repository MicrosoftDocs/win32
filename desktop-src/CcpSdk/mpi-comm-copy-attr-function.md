---
Description: 'MPI\_Comm\_copy\_attr\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fc983377-ed92-4f7e-b50d-06283c14eb6d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_copy\_attr\_function function'
---

# MPI\_Comm\_copy\_attr\_function function

**MPI\_Comm\_copy\_attr\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Comm_copy_attr_function(
           MPI_Comm oldcomm,
           int      comm_keyval,
  _In_opt_ void     *extra_state,
  _In_     void     *attribute_val_in,
  _Out_    void     *attribute_val_out,
  _Out_    int      *flag
);
```



## Parameters

<dl> <dt>

*oldcomm* 
</dt> <dd>

TBD

</dd> <dt>

*comm\_keyval* 
</dt> <dd>

TBD

</dd> <dt>

*extra\_state* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*attribute\_val\_in* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*attribute\_val\_out* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*flag* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
SUBROUTINE COMM_COPY_ATTR_FUNCTION(OLDCOMM, COMM_KEYVAL, EXTRA_STATE,
            ATTRIBUTE_VAL_IN, ATTRIBUTE_VAL_OUT, FLAG, IERROR)
    INTEGER OLDCOMM, COMM_KEYVAL, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) EXTRA_STATE, ATTRIBUTE_VAL_IN,
        ATTRIBUTE_VAL_OUT
    LOGICAL FLAG
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

 

 




