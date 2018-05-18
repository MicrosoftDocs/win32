---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bd2e9269-a2cf-44e8-b2e8-b86cc5702479'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_create\_keyval function'
---

# MPI\_Type\_create\_keyval function

TBD

## Syntax


```C++
int MPIAPI MPI_Type_create_keyval(
  _In_     MPI_Type_copy_attr_function   *type_copy_attr_fn,
  _In_     MPI_Type_delete_attr_function *type_delete_attr_fn,
  _Out_    int                           *type_keyval,
  _In_opt_ void                          *extra_state
);
```



## Parameters

<dl> <dt>

*type\_copy\_attr\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*type\_delete\_attr\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*type\_keyval* \[out\]
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
MPI_TYPE_CREATE_KEYVAL(TYPE_COPY_ATTR_FN, TYPE_DELETE_ATTR_FN, TYPE_KEYVAL,
            EXTRA_STATE, IERROR)
    EXTERNAL TYPE_COPY_ATTR_FN, TYPE_DELETE_ATTR_FN
    INTEGER TYPE_KEYVAL, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) EXTRA_STATE
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

[*MPI\_Type\_copy\_attr\_function*](mpi-type-copy-attr-function.md)
</dt> <dt>

[*MPI\_Type\_delete\_attr\_function*](mpi-type-delete-attr-function.md)
</dt> </dl>

 

 




