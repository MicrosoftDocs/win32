---
Description: 'Returns a handle to a new communicator to which the distributed graph topology information is attached.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1E6FDB8C-6964-4DA4-837A-8DD4D304D48B'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Dist\_graph\_create\_adjacent function'
---

# MPI\_Dist\_graph\_create\_adjacent function

Returns a handle to a new communicator to which the distributed graph topology information is attached.

## Syntax


```C++
int WINAPI MPI_Dist_graph_create_adjacent(
  _In_  MPI_Comm                comm_old,
        _In_range_(>=,0)  int   indegree,
        _In_reads_opt const int sources[],
        _In_reads_opt const int sourceweights[],
        _In_range_(>=,0)  int   outdegree,
        _In_reads_opt const int destinations[],
        _In_reads_opt const int destweights[],
  _In_  MPI_Info                info,
        _In_range_(0,1) int     reorder,
  _Out_ MPI_Comm                *comm_dist_graph
);
```



## Parameters

<dl> <dt>

*comm\_old* \[in\]
</dt> <dd>

The handle of the communicator without the topology information (handle).

</dd> <dt>

*indegree* 
</dt> <dd>

Size of the *sources* and *sourceweights* arrays (non-negative integer).

</dd> <dt>

*sources\[\]* 
</dt> <dd>

Ranks of processes for which the calling process is the destination (array of non-negative integers).

</dd> <dt>

*sourceweights\[\]* 
</dt> <dd>

Weights of the corresponding edges into the calling process (array of non-negative integers).

</dd> <dt>

*outdegree* 
</dt> <dd>

Size of the *destinations* and *destweights* arrays (non-negative integer).

</dd> <dt>

*destinations\[\]* 
</dt> <dd>

Ranks of processes for which the calling process is the source (array of non-negative integers).

</dd> <dt>

*destweights\[\]* 
</dt> <dd>

Weights of the corresponding edges out of the calling process (array of non-negative integers).

</dd> <dt>

*info* \[in\]
</dt> <dd>

Hints on optimization or interpretation of weights (handle). Currently use **MPI\_INFO\_NULL** as this variable is not being used internally.

</dd> <dt>

*reorder* 
</dt> <dd>

Ranks may be reordered (true) or not (false) (logical). Currently this is not used internally.

</dd> <dt>

*comm\_dist\_graph* \[out\]
</dt> <dd>

Handle to the communicator with the distributed graph topology information attached (handle).

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_DIST_GRAPH_CREATE_ADJACENT (COMM_OLD, INDEGREE, SOURCES, SOURCEWEIGHTS,
OUTDEGREE, DESTINATIONS, DESTWEIGHTS, INFO, REORDER,
COMM_DIST_GRAPH, IERROR)
    INTEGER COMM_OLD, INDEGREE, SOURCES (*), SOURCEWEIGHTS (*), OUTDEGREE,
DESTINATIONS (*), DESTWEIGHTS (*), INFO, COMM_DIST_GRAPH, IERROR
    LOGICAL REORDER
```

## Remarks

Each process in the *comm\_old* communicator passes all information about its incoming and outgoing edges in the virtual distributed graph topology. The calling processes must ensure that each edge of the graph is described in the source and in the destination process with the same weight, if the graph is weighted. If there are multiple edges for a given source-destination pair, then the sequence of the weights of these edges does not matter.

The complete communication topology is the combination of all edges shown in the sources array of all processes in *comm\_old*, which must be identical to the combination of all edges shown in the *destinations* array. Source and destination ranks must be process ranks of *comm\_old*. This allows a fully distributed specification of the communication graph. Isolated processes, that is, processes with no incoming or outgoing edges in the distributed topology, and thus have *indegree* or *outdegree* or both, as zero, are allowed.

The number of processes in the newly created communicator, *comm\_dist\_graph*, is identical to the number of processes in *comm\_old*. The call to this function is collective.

Weights are specified as non-negative integers using the *sourceweights* and *destweights* arrays, if the graph is a weighted graph. An application will need to specify **MPI\_UNWEIGHTED** for both the *sourceweights* and *destweights* arrays to indicate that all edges have the same (effectively no) weight. It is erroneous to supply **MPI\_UNWEIGHTED** for some but not all processes of *comm\_old*. The behavior in such a case is not guaranteed. If the graph is weighted, but *indegree* or *outdegree* is zero for a process, then **MPI\_WEIGHTS\_EMPTY** or any arbitrary array may be passed to *sourceweights* or *destweights* by that process.

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

[**MPI\_Dist\_graph\_neighbors**](mpi-dist-graph-neighbors.md)
</dt> </dl>

 

 




