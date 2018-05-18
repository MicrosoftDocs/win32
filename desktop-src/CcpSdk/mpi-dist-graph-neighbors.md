---
Description: 'Returns the list of neighbors having edges into and out of the calling process, as well as the corresponding weights on the incoming and outgoing edges in a distributed graph topology.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2C012D74-85CD-407F-B0B9-3B16D3FE6E0C'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Dist\_graph\_neighbors function'
---

# MPI\_Dist\_graph\_neighbors function

Returns the list of neighbors having edges into and out of the calling process, as well as the corresponding weights on the incoming and outgoing edges in a distributed graph topology.

## Syntax


```C++
int WINAPI MPI_Dist_graph_neighbors(
  _In_ MPI_Comm              comm,
       _In_range_(>=,0)  int maxindegree,
       _Out_writes_opt int   sources[],
       _Out_writes_opt int   sourceweights[],
       _In_range_(>=,0)  int maxoutdegree,
       _Out_writes_opt int   destinations[],
       _Out_writes_opt int   destweights[]
);
```



## Parameters

<dl> <dt>

*comm* \[in\]
</dt> <dd>

The handle of the communicator with the distributed graph topology.

</dd> <dt>

*maxindegree* 
</dt> <dd>

Size of the *sources* and *sourceweights* arrays (non-negative integer).

</dd> <dt>

*sources\[\]* 
</dt> <dd>

Ranks of processes in the communicator for which, the calling process is the destination in the distributed graph topology (array of non-negative integers).

</dd> <dt>

*sourceweights\[\]* 
</dt> <dd>

Weights of the corresponding edges into the calling process (array of non-negative integers).

</dd> <dt>

*maxoutdegree* 
</dt> <dd>

Size of the *destinations* and *destweights* arrays (non-negative integer).

</dd> <dt>

*destinations\[\]* 
</dt> <dd>

Ranks of processes in the communicator for which the calling process is the source in the distributed graph topology (array of non-negative integers).

</dd> <dt>

*destweights\[\]* 
</dt> <dd>

Weights of the corresponding edges out of the calling process (array of non-negative integers).

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_DIST_GRAPH_NEIGHBORS (COMM, MAXINDEGREE, SOURCES, SOURCEWEIGHTS,
MAXOUTDEGREE, DESTINATIONS, DESTWEIGHTS, IERROR)
    INTEGER COMM, MAXINDEGREE, SOURCES (*), SOURCEWEIGHTS (*), MAXOUTDEGREE,
DESTINATIONS (*), DESTWEIGHTS (*), IERROR
```

## Remarks

The incoming and outgoing edge count and the weight information can be obtained by calling [**MPI\_Dist\_graph\_neighbors\_count**](mpi-dist-graph-neighbors-count.md) prior to calling this method. If *maxindegree* and *maxoutdegree* are less than the number of incoming and outgoing edges returned by **MPI\_Dist\_graph\_neighbors\_count**, then only the first part of the full list is returned.

The incoming and outgoing edge weights are returned only if the graph was created as a weighted distributed graph by the [**MPI\_Dist\_graph\_create\_adjacent**](mpi-dist-graph-create-adjacent.md) or the [**MPI\_Dist\_graph\_create**](mpi-dist-graph-create.md) methods and if **MPI\_UNWEIGHTED** is not supplied as an argument in place of *sourceweights* or *destweights*.

## Requirements



|                    |                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Microsoft MPI v6<br/>                                                                                                                    |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl> |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                           |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                           |



## See also

<dl> <dt>

[MPI Process Topology Functions](mpi-process-topology-functions.md)
</dt> <dt>

[**MPI\_Dist\_graph\_create**](mpi-dist-graph-create.md)
</dt> <dt>

[**MPI\_Dist\_graph\_neighbors\_count**](mpi-dist-graph-neighbors-count.md)
</dt> <dt>

[**MPI\_Dist\_graph\_create\_adjacent**](mpi-dist-graph-create-adjacent.md)
</dt> </dl>

 

 




