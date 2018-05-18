---
Description: 'Gathers data from and scatters data to all members of a group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6cb4cd3b-f69e-448b-bb46-b0f1fa794b09'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Alltoallw function'
---

# MPI\_Alltoallw function

Gathers data from and scatters data to all members of a group. The **MPI\_Alltoallw** function is the most general form of complete data exchange in this API. **MPI\_Alltoallw** enables separate specification of the count, displacement, and data type.

## Syntax


```C++
int MPIAPI MPI_Alltoallw(
  _In_  void         *sendbuf,
  _In_  int          *sendcounts[],
  _In_  int          *sdispls[],
  _In_  MPI_Datatype sendtypes[],
  _Out_ void         *recvbuf,
  _In_  int          *recvcounts[],
  _In_  int          *rdispls[],
  _In_  MPI_Datatype recvtypes[],
        MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

The pointer to the data to be sent to all processes in the group. The number and data type of the elements in the buffer are specified in the *sendcount* and *sendtype* parameters. Each element in the buffer corresponds to a process in the group.

If the comm parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in all processes. The *sendcount*, *sdispls* and *sendtype* parameters are ignored. Each process enters data in the corresponding receive buffer element.

Data that is sent and received must have the same type map, as specified by the *recvcounts* array and the *recvtype* parameter, and is read from the locations of the receive buffer as specified by the *rdispls* parameter.

</dd> <dt>

*sendcounts* \[in\]
</dt> <dd>

The number of data elements that this process sends in the buffer as specified in the *sendbuf* parameter. If an element in *sendcount* is zero, the data part of the message from that process is empty.

</dd> <dt>

*sdispls* \[in\]
</dt> <dd>

The location, in bytes, relative to the *sendbuf* parameter, of the data for each communicator process.

Entry *j* specifies the displacement relative to the *sendbuf* parameter from which to take the outgoing data that is destined for process *j*.

</dd> <dt>

*sendtypes* \[in\]
</dt> <dd>

The data type for each of the elements in the send buffer. Entry *j* specifies the type of data that is sent to process *j* in the group.

</dd> <dt>

*recvbuf* \[out\]
</dt> <dd>

The pointer to a buffer that contains the data that is received from each process. The number and data type of the elements in the buffer are specified in the *recvcount* and *recvtype* parameters.

</dd> <dt>

*recvcounts* \[in\]
</dt> <dd>

The number of data elements from each communicator process in the receive buffer.

</dd> <dt>

*rdispls* \[in\]
</dt> <dd>

The location, in bytes, relative to the *recvbuf* parameter, of the data from each communicator process. Entry *i* specifies the displacement relative to the *recvbuf* parameter at which to place the incoming data from process *i*.

In the *recvbuf*, *recvcounts*, and *rdispls* parameter arrays, the *n*<sup>th</sup> element of each array refers to the data that is received from the *n*<sup>th</sup> communicator process.

</dd> <dt>

*recvtypes* \[in\]
</dt> <dd>

The data type of each element in buffer. Entry *i* specifies the type of data that is received from process *i*.

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
MPI_ALLTOALLW(SENDBUF, SENDCOUNT, SDISPLS, SENDTYPE, RECVBUF, RECVCOUNTS, RDISPLS, RECVTYPE,COMM, IERROR)
    <type> SENDBUF(*), R.ECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPES(*), SDISPLS(*), RECVCOUNTS(*), RDISPLS(*), RECVTYPE, COMM, IERROR
```

## Remarks

> \[!Important\]  
> To allow maximum flexibility, the displacement of blocks within the send and receive buffers is specified in bytes.

 

All parameters are significant on all processes. The *comm* parameter must be identical on all processes.

If the *comm* parameter references an intracommunicator, then the *j*<sup>th</sup> block that is sent from process *i* is received by process *j* and is placed in the *i*<sup>th</sup> block of the receive buffer. These blocks do not all have to have the same size.

The type signature that is specified by the *sendcounts\[j\]* and *sendtypes\[j\]* parameters for process *i* must be equal to the type signature that is associated with the *recvcounts\[i\]* and *recvtypes\[i\]* at process *j*. Therefore, the amount of data sent must be equal to the amount of data that is received between any pair of processes. Distinct type maps between sender and receiver are still allowed.

The result of a call to the **MPI\_Alltoallw** function is as if each process sent a message to every other process with `MPI_Send(sendbuf+sdispls[i],sendcounts[i],sendtypes[i] ,i,...)`, and received a message from every other process with a call to `MPI_Recv(recvbuf+rdispls[i],recvcounts[i],recvtypes[i] ,i,...)`.

Specifying the in-place option indicates that the same amount and type of data is sent and received between any two processes in the group of the communicator. Different pairs of processes can exchange different amounts of data. Users must ensure that *recvcounts\[j\]* and *recvtype* on process *i* match *recvcounts\[i\]* and *recvtype* on process *j*.

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

[**MPI\_Alltoallv**](mpi-alltoallv.md)
</dt> <dt>

[**MPI\_Gather**](mpi-gather.md)
</dt> <dt>

[**MPI\_Scatter**](mpi-scatter.md)
</dt> <dt>

[**MPI\_Send**](mpi-send.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> </dl>

 

 




