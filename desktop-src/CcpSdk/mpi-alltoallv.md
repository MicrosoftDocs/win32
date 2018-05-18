---
Description: 'Gathers data from and scatters data to all members of a group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '14a47f9e-b476-4397-9b70-d8d2428b33bd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Alltoallv function'
---

# MPI\_Alltoallv function

Gathers data from and scatters data to all members of a group. The **MPI\_Alltoallv** function adds flexibility to the [**MPI\_Alltoall**](mpi-alltoall.md) function by allowing a varying count of data from each process.

## Syntax


```C++
int MPIAPI MPI_Alltoallv(
  _In_  void         *sendbuf,
  _In_  int          *sendcounts,
  _In_  int          *sdispls,
        MPI_Datatype sendtype,
  _Out_ void         *recvbuf,
  _In_  int          *recvcounts,
  _In_  int          *rdispls,
        MPI_Datatype recvtype,
        MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

The pointer to the data to be sent to all processes in the group. The number and data type of the elements in the buffer are specified in the *sendcount* and *sendtype* parameters. Each element in the buffer corresponds to a process in the group.

If the comm parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in all processes. The *sendcount*, *sdispls* and *sendtype* parameters are ignored. Each process enters data in the corresponding receive buffer element.

Data that are sent and received must have the same type map as specified by the *recvcounts* array and the *recvtype* parameter. Data is read from the locations of the receive buffer that is specified by the *rdispls* parameter.

</dd> <dt>

*sendcounts* \[in\]
</dt> <dd>

The number of data elements that this process sends in the buffer that is specified in the *sendbuf* parameter. If an element in*sendcount* is zero, the data part of the message from that process is empty.

</dd> <dt>

*sdispls* \[in\]
</dt> <dd>

The location, relative to the *sendbuf* parameter, of the data for each communicator process.

Entry *j* specifies the displacement relative to the *sendbuf* parameter from which to take the outgoing data that is destined for process *j*.

</dd> <dt>

*sendtype* 
</dt> <dd>

The MPI data type of the elements in the send buffer.

</dd> <dt>

*recvbuf* \[out\]
</dt> <dd>

The pointer to a buffer that contains the data that are received from each process. The number and data type of the elements in the buffer are specified in the *recvcount* and *recvtype* parameters.

</dd> <dt>

*recvcounts* \[in\]
</dt> <dd>

The number of data elements from each communicator process in the receive buffer.

</dd> <dt>

*rdispls* \[in\]
</dt> <dd>

The location, relative to the *recvbuf* parameter, of the data from each communicator process.

In the *recvbuf*, *recvcounts*, and *rdispls* parameter arrays, the *n*<sup>th</sup> element of each array refers to the data that is received from the *n*<sup>th</sup> communicator process.

</dd> <dt>

*recvtype* 
</dt> <dd>

The MPI data type of each element in buffer.

</dd> <dt>

*comm* 
</dt> <dd>

Specifies the [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_ALLTOALL(SENDBUF, SENDCOUNT, SENDTYPE, RECVBUF, RECVCOUNT, RECVTYPE,
            COMM, IERROR)
    <type> SENDBUF(*), R.ECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, RECVCOUNT, RECVTYPE, COMM, IERROR
```

## Remarks

The type signature that is specified by the *sendcount*, and *sendtype* parameters for a process must be equal to the type signature that is specified by the *recvcount*, and *recvtype* parameters of the receiving process. Therefore, the amount of data sent must be equal to the amount of data that is received between any pair of processes. Distinct type maps between sender and receiver are still allowed.

All parameters are significant on all processes. The *comm* parameter must be identical on all processes.

If the *comm* parameter references an intracommunicator, then the *j*<sup>th</sup> block that is sent from process *i* is received by process *j* and is placed in the *i*<sup>th</sup> block of the receive buffer. These blocks do not have to all have the same size.

The outcome of calling the **MPI\_Alltoallv** function is as if each process sent a message to every other process with, `MPI_Send(sendbuf + sdispls[i]*extent(sendtype), sendcounts[i], sendtype, I, …)`, and received a message from every other process with a call to `MPI_Recv(recvbuf + rdispls[i]*extent(recvtype), recvcounts[i], recvtype, I, …)`.

Specifying the in-place option indicates that the same amount and type of data is sent and received between any two processes in the group of the communicator. Different pairs of processes can exchange different amounts of data. Users must ensure that *recvcounts\[j\]* and *recvtype* on process *i* match *recvcounts\[i\]* and *recvtype* on process *j*. This symmetric exchange can be useful in applications where the data to be sent is not be used by the sending process after the **MPI\_Alltoallv** function call.

If the *comm* parameter references an intercommunicator, then the outcome is as if each process in group A sends a message to each process in group B, and vice versa. The *j*<sup>th</sup> send buffer of process *i* in group A should be consistent with the *i*<sup>th</sup> receive buffer of process *j* in group B, and vice versa.

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

[**MPI\_Alltoall**](mpi-alltoall.md)
</dt> <dt>

[**MPI\_Gather**](mpi-gather.md)
</dt> <dt>

[**MPI\_Scatter**](mpi-scatter.md)
</dt> <dt>

[**MPI\_Send**](mpi-send.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> </dl>

 

 




