---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f2d8fdf3-1487-4301-9519-191f21af68c2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Graph\_neighbors\_count function'
---

# MPI\_Graph\_neighbors\_count function

TBD

## Syntax


```C++
int MPIAPI MPI_Graph_neighbors_count(
        MPI_Comm comm,
        int      rank,
  _Out_ int      *nneighbors
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*rank* 
</dt> <dd>

TBD

</dd> <dt>

*nneighbors* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_GRAPH_NEIGHBORS_COUNT(COMM, RANK, NNEIGHBORS, IERROR)
    INTEGER COMM, RANK, NNEIGHBORS, IERROR
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

 

 




