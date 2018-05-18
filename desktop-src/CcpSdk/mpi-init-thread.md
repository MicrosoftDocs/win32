---
Description: 'Initializes the calling MPI process’s execution environment for threaded execution.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8042dcc8-8099-446f-85a0-9fbffa8f487e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Init\_thread function'
---

# MPI\_Init\_thread function

Initializes the calling MPI process’s execution environment for threaded execution.

## Syntax


```C++
int MPIAPI MPI_Init_thread(
  _In_opt_ int                        *argc,
           _In_opt_count_(*argc) char ***argv,
  _In_     int                        required,
  _Out_    int                        *provided
);
```



## Parameters

<dl> <dt>

*argc* \[in, optional\]
</dt> <dd>

A pointer to the number of arguments for the program. This value can be NULL.

</dd> <dt>

*argv* \[optional\]
</dt> <dd>

A pointer to the argument list for the program. This value can be NULL.

</dd> <dt>

*required* \[in\]
</dt> <dd>

The level of desired thread support. Multiple MPI processes in the same job may use different values.



|                         |                                                                                                                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MPI\_THREAD\_SINGLE     | Only a single thread in the program will execute.                                                                                                                                                                 |
| MPI\_THREAD\_FUNNELED   | The process may contain multiple threads, but the thread that called **MPI\_Init\_thread** is the only one that makes MPI function calls.                                                                         |
| MPI\_THREAD\_SERIALIZED | The process may contain multiple threads, and all of those threads may make MPI function calls, but only one at a time.                                                                                           |
| MPI\_THREAD\_MULTIPLE   | Multiple application threads may call MPI functions with no restrictions. This value is currently only supported on MS-MPI V6 running on Windows Server 2012, Windows Server 2012 R2, Windows 8, and Windows 8.1. |



 

</dd> <dt>

*provided* \[out\]
</dt> <dd>

The level of provided thread support. The value returned will be from the table above.





 

</dd> </dl>

## Return value

**MPI\_SUCCESS** if the function returns successfully. Other error codes if the call failed for other reasons (such as invalid arguments).

In Fortran the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_INIT_THREAD(REQUIRED, PROVIDED, IERROR)
    INTEGER REQUIRED, PROVIDED, IERROR
```

## Remarks

This function must be called by one thread only. That thread will be known as the “Main Thread” and must be the same thread to call [**MPI\_Finalize**](mpi-finalize.md).

The Fortran binding of **MPI\_Init\_thread** does not accept the ARGC and ARGV parameters.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI External Functions](mpi-external-functions.md)
</dt> <dt>

[**MPI\_Finalize**](mpi-finalize.md)
</dt> <dt>

[**MPI\_Init**](mpi-init.md)
</dt> </dl>

 

 




