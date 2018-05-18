---
Description: 'MPI\_Comm\_errhandler\_fn is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '07417db4-d087-42bf-a11c-ae1a3181c382'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_errhandler\_fn callback function'
---

# MPI\_Comm\_errhandler\_fn callback function

*MPI\_Comm\_errhandler\_fn* is a placeholder for the application-defined function name.

## Syntax


```C++
void MPI_Comm_errhandler_fn(
  _In_    MPI_Comm *comm,
  _Inout_ int      *errcode,
                   ...
);
```



## Parameters

<dl> <dt>

*comm* \[in\]
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
SUBROUTINE COMM_ERRHANDLER_FUNCTION(COMM, ERROR_CODE)
    INTEGER COMM, ERROR_CODE
```

## Remarks

The placeholder name of this function, *MPI\_Comm\_errhandler\_fn*, is deprecated in the MPI-2.2 standard and replaced by *MPI\_Comm\_errhandler\_function*. The function prototype is unchanged.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |



## See also

<dl> <dt>

[MPI Management Functions](mpi-management-functions.md)
</dt> <dt>

[**MPI\_Comm\_create\_errhandler**](mpi-comm-create-errhandler.md)
</dt> </dl>

 

 




