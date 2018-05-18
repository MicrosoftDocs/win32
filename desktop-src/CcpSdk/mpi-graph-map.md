---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '43f34f5d-dd31-4173-b441-4c330fe7f75e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Graph\_map function'
---

# MPI\_Graph\_map function

TBD

## Syntax


```C++
int MPIAPI MPI_Graph_map(
        MPI_Comm               comm,
        int                    nnodes,
        _In_count_(nnodes) int *index,
  _In_  int                    *edges,
  _Out_ int                    *newrank
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*nnodes* 
</dt> <dd>

TBD

</dd> <dt>

*index* 
</dt> <dd>

TBD

</dd> <dt>

*edges* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*newrank* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_GRAPH_MAP(COMM, NNODES, INDEX, EDGES, NEWRANK, IERROR)
    INTEGER COMM, NNODES, INDEX(*), EDGES(*), NEWRANK, IERROR
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

[MPI Process Topology Functions](mpi-process-topology-functions.md)
</dt> </dl>

 

 




