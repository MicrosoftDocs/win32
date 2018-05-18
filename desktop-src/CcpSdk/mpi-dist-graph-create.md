---
Description: 'Returns a handle to a new communicator to which the distributed graph topology information is attached.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'AA8B083C-E601-4E64-BAEE-09CB364A005F'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Dist\_graph\_create function'
---

# MPI\_Dist\_graph\_create function

Returns a handle to a new communicator to which the distributed graph topology information is attached.

## Syntax


```C++
int WINAPI MPI_Dist_graph_create(
  _In_  MPI_Comm                comm_old,
        _In_range_(>=,0)  int   n,
        _In_reads_opt const int sources[],
        _In_reads_opt const int degrees[],
        _In_opt const int       destinations[],
        _In_opt const int       weights[],
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

*n* 
</dt> <dd>

Number of sources for which this process specifies outgoing edges (non-negative integer).

</dd> <dt>

*sources\[\]* 
</dt> <dd>

Array containing the *n* sources for which this source specifies the outgoing edges (array of non-negative integers).

</dd> <dt>

*degrees\[\]* 
</dt> <dd>

Array specifying the number of destinations for each source node in the source node array (array of non-negative integers).

</dd> <dt>

*destinations\[\]* 
</dt> <dd>

Destination nodes for the source nodes in the sources array (array of non-negative integers).

</dd> <dt>

*weights\[\]* 
</dt> <dd>

Weights for corresponding edges in the *destinations* array (array of non-negative integers).

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
MPI_DIST_GRAPH_CREATE (COMM_OLD, N, SOURCES, DEGREES, DESTINATIONS, WEIGHTS,
INFO, REORDER, COMM_DIST_GRAPH, IERROR)
    INTEGER COMM_OLD, N, SOURCES (*), DEGREES (*), DESTINATIONS (*),
WEIGHTS (*), INFO, COMM_DIST_GRAPH, IERROR
    LOGICAL REORDER
```

## Remarks

Both the *sources* and *destinations* arrays may contain the same node more than once, and the order in which nodes are listed as destinations or sources is not significant. Similarly, different processes may specify edges with the same source and destination nodes. Source and destination nodes must be process ranks of *comm\_old*. Different processes may specify different numbers of source and destination nodes, as well as different source to destination edges. This allows a fully distributed specification of the communication graph. Isolated processes (processes with no outgoing or incoming edges, that is, processes that do not occur as source or destination node in the graph specification) are allowed.

The number of processes in *comm\_dist\_graph* is identical to the number of processes in *comm\_old*. The call to this function is collective.

In C or FORTRAN, an application can supply **MPI\_UNWEIGHTED** for the *weights* array to indicate that all edges have the same (effectively no) weight. It is erroneous to supply **MPI\_UNWEIGHTED** for some but not all processes of *comm\_old*. The behavior in such a case is not guaranteed. If the graph is weighted, but *n* = 0, then, **MPI\_WEIGHTS\_EMPTY** or any arbitrary array may be passed to *weights*.

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

[**MPI\_Dist\_graph\_create\_adjacent**](mpi-dist-graph-create-adjacent.md)
</dt> <dt>

[**MPI\_Dist\_graph\_neighbors\_count**](mpi-dist-graph-neighbors-count.md)
</dt> <dt>

[**MPI\_Dist\_graph\_neighbors**](mpi-dist-graph-neighbors.md)
</dt> </dl>

 

 




