---
Description: 'MPI\_Win\_copy\_attr\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4866238c-2fd2-43ee-938f-c36ca0ca0806'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Win\_copy\_attr\_function callback function'
---

# MPI\_Win\_copy\_attr\_function callback function

**MPI\_Win\_copy\_attr\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Win_copy_attr_function(
           MPI_Win oldwin,
           int     win_keyval,
  _In_opt_ void    *extra_state,
  _In_     void    *attribute_val_in,
  _Out_    void    *attribute_val_out,
  _Out_    int     *flag
);
```



## Parameters

<dl> <dt>

*oldwin* 
</dt> <dd>

TBD

</dd> <dt>

*win\_keyval* 
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
SUBROUTINE WIN_COPY_ATTR_FUNCTION(OLDWIN, WIN_KEYVAL, EXTRA_STATE,
            ATTRIBUTE_VAL_IN, ATTRIBUTE_VAL_OUT, FLAG, IERROR)
    INTEGER OLDWIN, WIN_KEYVAL, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) EXTRA_STATE, ATTRIBUTE_VAL_IN,
        ATTRIBUTE_VAL_OUT
    LOGICAL FLAG
```

## Requirements



|                   |                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl> |



## See also

<dl> <dt>

[MPI Caching Functions](mpi-caching-functions.md)
</dt> <dt>

[**MPI\_Win\_create\_keyval**](mpi-win-create-keyval.md)
</dt> </dl>

 

 




