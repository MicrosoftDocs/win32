---
Description: 'Obtains adjacency information of the calling process in a distributed graph topology.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1016274C-C079-4770-962E-8036FF696B71'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Dist\_graph\_neighbors\_count function'
---

# MPI\_Dist\_graph\_neighbors\_count function

Obtains adjacency information of the calling process in a distributed graph topology. The information that is obtained by this function, on the number of incoming edges, outgoing edges, and a flag indicating if the distributed graph is weighted, matches the information provided in the call to [**MPI\_Dist\_graph\_create\_adjacent**](mpi-dist-graph-create-adjacent.md) or [**MPI\_Dist\_graph\_create**](mpi-dist-graph-create.md) (by the calling process in the case of **MPI\_Dist\_graph\_create\_adjacent**, or potentially by processes other than the calling process in the case of **MPI\_Dist\_graph\_create**).

## Syntax


```C++
int WINAPI MPI_Dist_graph_neighbors_count(
  _In_  MPI_Comm comm,
  _Out_ int      indegree,
  _Out_ int      outdegree,
  _Out_ int      weighted
);
```



## Parameters

<dl> <dt>

*comm* \[in\]
</dt> <dd>

The handle of the communicator with the distributed graph topology.

</dd> <dt>

*indegree* \[out\]
</dt> <dd>

Number of edges into this process (non-negative integer).

</dd> <dt>

*outdegree* \[out\]
</dt> <dd>

Number of edges out of this process (non-negative integer).

</dd> <dt>

*weighted* \[out\]
</dt> <dd>

Is false if **MPI\_UNWEIGHTED** was supplied during creation, true otherwise.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_DIST_GRAPH_NEIGHBORS_COUNT (COMM, INDEGREE, OUTDEGREE, WEIGHTED, IERROR)
    INTEGER COMM, INDEGREE, OUTDEGREE, IERROR
    LOGICAL WEIGHTED
```

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

[**MPI\_Dist\_graph\_neighbors**](mpi-dist-graph-neighbors-count.md)
</dt> <dt>

[**MPI\_Dist\_graph\_create**](mpi-dist-graph-create.md)
</dt> <dt>

[**MPI\_Dist\_graph\_create\_adjacent**](mpi-dist-graph-create-adjacent.md)
</dt> </dl>

 

 




