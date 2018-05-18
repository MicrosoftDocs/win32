---
Description: 'MPI\_Type\_delete\_attr\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '51e6cd99-404f-4ede-9b92-e87ff9469053'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_delete\_attr\_function callback function'
---

# MPI\_Type\_delete\_attr\_function callback function

**MPI\_Type\_delete\_attr\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
int MPI_Type_delete_attr_function(
           MPI_Datatype datatype,
           int          datatype_keyval,
  _In_     void         *attribute_val,
  _In_opt_ void         *extra_state
);
```



## Parameters

<dl> <dt>

*datatype* 
</dt> <dd>

TBD

</dd> <dt>

*datatype\_keyval* 
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
SUBROUTINE TYPE_DELETE_ATTR_FUNCTION(DATATYPE, TYPE_KEYVAL, ATTRIBUTE_VAL,
            EXTRA_STATE, IERROR)
    INTEGER DATATYPE, TYPE_KEYVAL, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) ATTRIBUTE_VAL, EXTRA_STATE
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

 

 




