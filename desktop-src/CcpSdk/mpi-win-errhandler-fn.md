---
Description: 'MPI\_Win\_errhandler\_fn is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cad5be1d-5e89-41d1-9548-f6eb09c14e34'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Win\_errhandler\_fn callback function'
---

# MPI\_Win\_errhandler\_fn callback function

*MPI\_Win\_errhandler\_fn* is a placeholder for the application-defined function name.

## Syntax


```C++
void MPI_Win_errhandler_fn(
  _In_    MPI_Win *win,
  _Inout_  int    *errcode,
                  ...
);
```



## Parameters

<dl> <dt>

*win* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*errcode* \[in, out\]
</dt> <dd>

TBD

</dd> <dt>

*...* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
SUBROUTINE WIN_ERRHANDLER_FUNCTION(WIN, ERROR_CODE)
    INTEGER WIN, ERROR_CODE
```

## Remarks

The placeholder name of this function, *MPI\_Win\_errhandler\_fn*, is deprecated in the MPI-2.2 standard and replaced by *MPI\_Win\_errhandler\_function*. The function prototype is unchanged.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |



## See also

<dl> <dt>

[MPI Management Functions](mpi-management-functions.md)
</dt> <dt>

[**MPI\_Win\_create\_errhandler**](mpi-win-create-errhandler.md)
</dt> </dl>

 

 




