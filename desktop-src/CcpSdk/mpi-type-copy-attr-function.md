---
Description: 'MPI\_Type\_copy\_attr\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'af7f651c-0da6-42e0-b7bc-5d4200f5f11f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_copy\_attr\_function callback function'
---

# MPI\_Type\_copy\_attr\_function callback function

**MPI\_Type\_copy\_attr\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Type_copy_attr_function(
           MPI_Datatype olddatatype,
           int          datatype_keyval,
  _In_opt_ void         *extra_state,
  _In_     void         *attribute_val_in,
  _Out_    void         *attribute_val_out,
  _Out_    int          *flag
);
```



## Parameters

<dl> <dt>

*olddatatype* 
</dt> <dd>

TBD

</dd> <dt>

*datatype\_keyval* 
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
SUBROUTINE TYPE_COPY_ATTR_FUNCTION(OLDTYPE, TYPE_KEYVAL, EXTRA_STATE,
            ATTRIBUTE_VAL_IN, ATTRIBUTE_VAL_OUT, FLAG, IERROR)
    INTEGER OLDTYPE, TYPE_KEYVAL, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) EXTRA_STATE,
        ATTRIBUTE_VAL_IN, ATTRIBUTE_VAL_OUT
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

[**MPI\_Type\_create\_keyval**](mpi-type-create-keyval.md)
</dt> </dl>

 

 




