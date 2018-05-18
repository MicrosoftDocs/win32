---
Description: 'Scatters data from one member across all members of a group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '057f380a-db02-4197-a4e8-e0e0e8fd2dea'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Scatterv function'
---

# MPI\_Scatterv function

Scatters data from one member across all members of a group. The **MPI\_Scatterv** function performs the inverse of the operation that is performed by the [**MPI\_Gatherv**](mpi-gatherv.md) function.

## Syntax


```C++
int MPIAPI MPI_Scatterv(
  _In_  void         *sendbuf,
  _In_  int          *sendcounts,
  _In_  int          *displs,
        MPI_Datatype sendtype,
  _Out_ void         *recvbuf,
        int          recvcount,
        MPI_Datatype recvtype,
        int          root,
        MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

The pointer to a buffer that contains the data to be sent by the root process.

The *sendbuf* parameter is ignored for all non-root processes.

If the *comm* parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in the root process. The *recvcount* and *recvtype* parameters are ignored. The scattered vector is still considered to contain *n* segments, where *n* is the group size; the segment that corresponds to the root process is not moved.

</dd> <dt>

*sendcounts* \[in\]
</dt> <dd>

The number of elements to send to each process. If *sendcount\[i\]* is zero, the data part of the message for that process is empty.

The *sendcount* parameter is ignored for all non-root processes.

</dd> <dt>

*displs* \[in\]
</dt> <dd>

The locations of the data to send to each communicator process. Each location in the array is relative to the corresponding element of the *sendbuf* array.

In the *sendbuf*, *sendcounts*, and *displs* parameter arrays, the *n*<sup>th</sup> element of each array refers to the data to be sent to the *n*<sup>th</sup> communicator process.

This parameter is significant only at the root process.

</dd> <dt>

*sendtype* 
</dt> <dd>

The MPI data type of each element in the buffer.

The *sendcount* parameter is ignored for all non-root processes.

</dd> <dt>

*recvbuf* \[out\]
</dt> <dd>

The pointer to a buffer that contains the data that is received on each process. The number and data type of the elements in the buffer are specified in the *recvcount* and *recvtype* parameters.

</dd> <dt>

*recvcount* 
</dt> <dd>

The number of elements in the receive buffer. If the count is zero, the data part of the message is empty.

</dd> <dt>

*recvtype* 
</dt> <dd>

The data type of the elements in the receive buffer.

</dd> <dt>

*root* 
</dt> <dd>

The rank in the sending process within the specified communicator.

</dd> <dt>

*comm* 
</dt> <dd>

The [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_SCATTERV(SENDBUF, SENDCOUNT, DISPLS, SENDTYPE, RECVBUF, RECVCOUNT, RECVTYPE, ROOT, COMM, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, DISPLS(*), RECVCOUNT(*), RECVTYPE, ROOT, COMM, IERROR
```

## Remarks

The **MPI\_Scatterv** function extends the functionality of the [**MPI\_Scatter**](mpi-scatter.md) function by allowing a varying count of data, as specified in the *sendcounts* array, to be sent to each process.

The specification of counts, types, and displacements should not cause any location on the root to be read more than one time.

All the function parameters are significant on the root process, only the *recvbuf*, *recvcount*, *recvtype*, *root*, and *comm* parameters are significant on the other processes. The *root* and *comm* parameters must be identical on all processes.

The type signature as specified by the *sendcount*, and *sendtype* parameters for the root process must be equal to the type signature as specified by the *recvcount*, and *recvtype* parameters for all processes. Therefore, the amount of data sent must be equal to the amount of data that is received between any pair of processes. Distinct type maps between sender and receiver are still allowed.

If comm is an intracommunicator, the result is as if the root executed *n* send operations `MPI_Send(sendbuf + displs[i]*extent(sendtype), sendcounts[i], sendtype, I, …)`; and each process executed a receive, `MPI_Recv(recvbuf, recvcount, recvtype, i,…)`.

If the *comm* parameter references an intercommunicator, then the call involves all processes in the intercommunicator, but with one group, group A, that defines the root process. All processes in the other group, group B, set the same value in *root* parameter, that is, the rank of the root process in group A. The root process sets the value **MPI\_ROOT** in the *root* parameter. All other processes in group A set the value **MPI\_PROC\_NULL** in the *root* parameter. Data is broadcast from the root process to all processes in group B. The *buffer* parameters of the processes in group B must be consistent with the *buffer* parameter of the root process.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Collective Functions](mpi-collective-functions.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> <dt>

[**MPI\_Gather**](mpi-gather.md)
</dt> <dt>

[**MPI\_Gatherv**](mpi-gatherv.md)
</dt> <dt>

[**MPI\_Scatter**](mpi-scatter.md)
</dt> </dl>

 

 




