---
Description: 'MPI\_File\_errhandler\_fn is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ae5f7495-3285-4d2a-9c67-9f186c35babf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_File\_errhandler\_fn callback function'
---

# MPI\_File\_errhandler\_fn callback function

*MPI\_File\_errhandler\_fn* is a placeholder for the application-defined function name.

## Syntax


```C++
void MPI_File_errhandler_fn(
  _In_    MPI_File *file,
  _Inout_  int     *errcode,
                   ...
);
```



## Parameters

<dl> <dt>

*file* \[in\]
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
SUBROUTINE FILE_ERRHANDLER_FUNCTION(FILE, ERROR_CODE)
INTEGER FILE, ERROR_CODE
```

## Remarks

The placeholder name of this function, *MPI\_File\_errhandler\_fn*, is deprecated in the MPI-2.2 standard and replaced by *MPI\_File\_errhandler\_function*. The function prototype is unchanged.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |



## See also

<dl> <dt>

[MPI Management Functions](mpi-management-functions.md)
</dt> <dt>

[**MPI\_File\_create\_errhandler**](mpi-file-create-errhandler.md)
</dt> </dl>

 

 




