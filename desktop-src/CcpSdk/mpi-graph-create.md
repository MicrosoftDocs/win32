---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e77ff296-4803-41a6-8c53-d758022cab5b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Graph\_create function'
---

# MPI\_Graph\_create function

TBD

## Syntax


```C++
int MPIAPI MPI_Graph_create(
        MPI_Comm               comm_old,
        int                    nnodes,
        _In_count_(nnodes) int *index,
  _In_  int                    *edges,
        int                    reorder,
  _Out_ MPI_Comm               *comm_cart
);
```



## Parameters

<dl> <dt>

*comm\_old* 
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

*reorder* 
</dt> <dd>

TBD

</dd> <dt>

*comm\_cart* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_GRAPH_CREATE(COMM_OLD, NNODES, INDEX, EDGES, REORDER, COMM_GRAPH, IERROR)
    INTEGER COMM_OLD, NNODES, INDEX(*), EDGES(*), COMM_GRAPH, IERROR
    LOGICAL REORDER
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

 

 




