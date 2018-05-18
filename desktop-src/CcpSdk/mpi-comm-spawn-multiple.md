---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '138dbd80-1330-406f-abcb-6f95fa81135e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_spawn\_multiple function'
---

# MPI\_Comm\_spawn\_multiple function

TBD

## Syntax


```C++
int MPIAPI MPI_Comm_spawn_multiple(
            int                        count,
            _In_count_(count) char     *array_of_commands[],
            _In_opt_count_(count) char **array_of_argv[],
            _In_count_(count) int      array_of_maxprocs[],
            _In_count_(count) MPI_Info array_of_info[],
            int                        root,
            MPI_Comm                   comm,
  _Out_     MPI_Comm                   *intercomm,
  _Out_opt_ int                        array_of_errcodes[]
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_commands* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_argv* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_maxprocs* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_info* 
</dt> <dd>

TBD

</dd> <dt>

*root* 
</dt> <dd>

TBD

</dd> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*intercomm* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_errcodes* \[out, optional\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_COMM_SPAWN_MULTIPLE(COUNT, ARRAY_OF_COMMANDS, ARRAY_OF_ARGV,
            ARRAY_OF_MAXPROCS, ARRAY_OF_INFO, ROOT, COMM, INTERCOMM,
            ARRAY_OF_ERRCODES, IERROR)
    INTEGER COUNT, ARRAY_OF_INFO(*), ARRAY_OF_MAXPROCS(*), ROOT, COMM,
    INTERCOMM, ARRAY_OF_ERRCODES(*), IERROR
    CHARACTER*(*) ARRAY_OF_COMMANDS(*), ARRAY_OF_ARGV(COUNT, *)
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

[MPI Process Management Functions](mpi-process-management-functions.md)
</dt> </dl>

 

 




