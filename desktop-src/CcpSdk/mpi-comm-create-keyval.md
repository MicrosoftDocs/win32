---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '13d0bf93-f8b8-4f26-bcbf-1b2a0bdab0fe'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_create\_keyval function'
---

# MPI\_Comm\_create\_keyval function

TBD

## Syntax


```C++
int MPIAPI MPI_Comm_create_keyval(
  _In_opt_ MPI_Comm_copy_attr_function   *comm_copy_attr_fn,
  _In_opt_ MPI_Comm_delete_attr_function *comm_delete_attr_fn,
  _Out_    int                           *comm_keyval,
  _In_opt_ void                          *extra_state
);
```



## Parameters

<dl> <dt>

*comm\_copy\_attr\_fn* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*comm\_delete\_attr\_fn* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*comm\_keyval* \[out\]
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
MPI_COMM_CREATE_KEYVAL(COMM_COPY_ATTR_FN, COMM_DELETE_ATTR_FN, COMM_KEYVAL,
        EXTRA_STATE, IERROR)
    EXTERNAL COMM_COPY_ATTR_FN, COMM_DELETE_ATTR_FN
    INTEGER COMM_KEYVAL, IERROR
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

[**MPI\_Comm\_copy\_attr\_function**](mpi-comm-copy-attr-function.md)
</dt> <dt>

[**MPI\_Comm\_delete\_attr\_function**](mpi-comm-delete-attr-function.md)
</dt> </dl>

 

 




