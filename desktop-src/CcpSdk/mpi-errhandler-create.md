---
Description: 'This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the MPI\_Comm\_create\_errhandler function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9e79d6df-6c94-44a8-aadd-e97a42dd1b6a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Errhandler\_create function'
---

# MPI\_Errhandler\_create function

This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the [**MPI\_Comm\_create\_errhandler**](mpi-comm-create-errhandler.md) function.

## Syntax


```C++
int MPIAPI MPI_Errhandler_create(
  _In_  MPI_Handler_function *function,
  _Out_ MPI_Errhandler       *errhandler
);
```



## Parameters

<dl> <dt>

*function* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*errhandler* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
```

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Management Functions](mpi-management-functions.md)
</dt> <dt>

[**MPI\_Comm\_create\_errhandler**](mpi-comm-create-errhandler.md)
</dt> </dl>

 

 




