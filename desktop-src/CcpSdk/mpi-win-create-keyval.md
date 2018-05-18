---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6c871be1-55e6-4aa9-bd4b-5c9b99ba953c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Win\_create\_keyval function'
---

# MPI\_Win\_create\_keyval function

TBD

## Syntax


```C++
int MPIAPI MPI_Win_create_keyval(
  _In_     MPI_Win_copy_attr_function   *win_copy_attr_fn,
  _In_     MPI_Win_delete_attr_function *win_delete_attr_fn,
  _Out_    int                          *win_keyval,
  _In_opt_ void                         *extra_state
);
```



## Parameters

<dl> <dt>

*win\_copy\_attr\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*win\_delete\_attr\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*win\_keyval* \[out\]
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
MPI_WIN_CREATE_KEYVAL(WIN_COPY_ATTR_FN, WIN_DELETE_ATTR_FN, WIN_KEYVAL,
            EXTRA_STATE, IERROR)
    EXTERNAL WIN_COPY_ATTR_FN, WIN_DELETE_ATTR_FN
    INTEGER WIN_KEYVAL, IERROR
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

[*MPI\_Win\_delete\_attr\_function*](mpi-win-delete-attr-function.md)
</dt> <dt>

[*MPI\_Win\_copy\_attr\_function*](mpi-win-copy-attr-function.md)
</dt> </dl>

 

 




