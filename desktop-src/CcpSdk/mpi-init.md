---
Description: 'Initializes the calling MPI process’s execution environment for single threaded execution.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4b88878f-b15c-421e-bad0-21353b516bb5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Init function'
---

# MPI\_Init function

Initializes the calling MPI process’s execution environment for single threaded execution.

## Syntax


```C++
int MPIAPI MPI_Init(
  _In_opt_ int                        *argc,
           _In_opt_count_(*argc) char ***argv
);
```



## Parameters

<dl> <dt>

*argc* \[in, optional\]
</dt> <dd>

A pointer to the number of arguments for the program. This value can be NULL.

</dd> <dt>

*argv* 
</dt> <dd>

A pointer to the argument list for the program. This value can be NULL.

</dd> </dl>

## Return value

**MPI\_SUCCESS** if the function returns successfully. Other error codes if the call failed for other reasons (such as invalid arguments). In Fortran the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_INIT(IERROR)
    INTEGER IERROR
```

## Remarks

This function must be called by one thread only. That thread will be known as the “Main Thread” and must be the same thread to call [**MPI\_Finalize**](mpi-finalize.md).

The Fortran binding of **MPI\_Init** does not accept the ARGC and ARGV parameters.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Management Functions](mpi-management-functions.md)
</dt> <dt>

[**MPI\_Finalize**](mpi-finalize.md)
</dt> <dt>

[**MPI\_Init\_thread**](mpi-init-thread.md)
</dt> </dl>

 

 




