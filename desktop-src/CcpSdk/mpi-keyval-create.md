---
Description: 'This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the MPI\_Comm\_create\_keyval function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '427928ee-84a3-4bbb-9c03-f1b32f5c9b42'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Keyval\_create function'
---

# MPI\_Keyval\_create function

This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the [**MPI\_Comm\_create\_keyval**](mpi-comm-create-keyval.md) function.

## Syntax


```C++
int
MPIAPI MPI_Keyval_create(
  _In_     MPI_Copy_function   *copy_fn,
  _In_     MPI_Delete_function *delete_fn,
  _Out_    int                 *keyval,
  _In_opt_ void                *extra_state
);
```



## Parameters

<dl> <dt>

*copy\_fn* \[in\]
</dt> <dd>

MPI\_Copy\_function

</dd> <dt>

*delete\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*keyval* \[out\]
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
MPI_KEYVAL_CREATE(COPY_FN, DELETE_FN, KEYVAL, EXTRA_STATE, IERROR)
    EXTERNAL COPY_FN, DELETE_FN
    INTEGER KEYVAL, EXTRA_STATE, IERROR
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

[MPI Miscellaneous Functions](mpi-miscellaneous-functions.md)
</dt> <dt>

[**MPI\_Comm\_create\_keyval**](mpi-comm-create-keyval.md)
</dt> </dl>

 

 




