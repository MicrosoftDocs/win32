---
Description: 'Terminates the calling MPI process’s execution environment.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e93c2023-9526-466a-892d-f11d18bb9bfe'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Finalize function'
---

# MPI\_Finalize function

Terminates the calling MPI process’s execution environment.

## Syntax


```C++
int MPIAPI MPI_Finalize(void);
```



## Parameters

This function has no parameters.

## Return value

**MPI\_SUCCESS** if the function returns successfully. Other error codes if the call failed for other reasons (such as invalid arguments). In Fortran the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_FINALIZE(IERROR)
    INTEGER IERROR
```

## Remarks

All MPI Processes must call this routine before exiting on the thread that called [**MPI\_Init**](mpi-init.md) or [**MPI\_Init\_thread**](mpi-init-thread.md).

The **MPI\_Finalize** function cleans up all state related to MPI. Once it is called, no other MPI functions may be called, including [**MPI\_Init**](mpi-init.md) and [**MPI\_Init\_thread**](mpi-init-thread.md). The application must ensure that all pending communications are completed or canceled before calling **MPI\_Finalize**.

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

[**MPI\_Init**](mpi-init.md)
</dt> <dt>

[**MPI\_Init\_thread**](mpi-init-thread.md)
</dt> </dl>

 

 




