---
Description: 'Gathers data from and scatters data to all members of a group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1fde8800-421a-45d3-ba4d-be0237003b61'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Alltoall function'
---

# MPI\_Alltoall function

Gathers data from and scatters data to all members of a group. The **MPI\_Alltoall** is an extension of the [**MPI\_Allgather**](mpi-allgather.md) function. Each process sends distinct data to each of the receivers. The *j*<sup>th</sup> block that is sent from process *i* is received by process *j* and is placed in the *i*<sup>th</sup> block of the receive buffer.

## Syntax


```C++
int MPIAPI MPI_Alltoall(
  _In_  void         *sendbuf,
        int          sendcount,
        MPI_Datatype sendtype,
  _Out_ void         *recvbuf,
        int          recvcount,
        MPI_Datatype recvtype,
        MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

The pointer to the data to be sent to all processes in the group. The number and data type of the elements in the buffer are specified in the *sendcount* and *sendtype* parameters.

If the comm parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in all processes. The *sendcount* and *sendtype* parameters are ignored. Each process enters data in the corresponding receive buffer element. The *n*<sup>th</sup> process sends data to the *n*<sup>th</sup> element of the receive buffer.

</dd> <dt>

*sendcount* 
</dt> <dd>

The number of elements in the buffer that is specified in the *sendbuf* parameter. If *sendcount* is zero, the data part of the message is empty.

</dd> <dt>

*sendtype* 
</dt> <dd>

The MPI data type of the elements in the send buffer.

</dd> <dt>

*recvbuf* \[out\]
</dt> <dd>

The pointer to a buffer that contains the data that is received from each process. The number and data type of the elements in the buffer are specified in the *recvcount* and *recvtype* parameters.

</dd> <dt>

*recvcount* 
</dt> <dd>

The number of elements in the receive buffer. If the count is zero, the data part of the message is empty.

</dd> <dt>

*recvtype* 
</dt> <dd>

The MPI data type of the elements in the receive buffer.

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
MPI_ALLTOALL(SENDBUF, SENDCOUNT, SENDTYPE, RECVBUF, RECVCOUNT, RECVTYPE,
            COMM, IERROR)
    <type> SENDBUF(*), R.ECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, RECVCOUNT, RECVTYPE, COMM, IERROR
```

## Remarks

All parameters are significant on all processes. The *comm* parameter must be identical on all processes.

The type signature that is specified by the *sendcount*, and *sendtype* parameters for a process must be equal to the type signature that is specified by the *recvcount*, and *recvtype* parameters. Therefore, the amount of data sent must be equal to the amount of data that is received between any pair of processes. Distinct type maps between sender and receiver are still allowed.

If the *comm* parameter references an intracommunicator, the outcome of a call to `MPI_ALLGATHER(...)` is as if each process executed a send to each process including itself by using `MPI_Send(sendbuf + i*sendcount*extent(sendtype), sendcount, sendtype, I, …)`, and receiving from every other process by using `MPI_Recv(recvbuf + i*recvcount*extent(recvtype), recvcount, recvtype, I, …)`.

If the *comm* parameter references an intercommunicator, then the result is as if each process in group A sends a message to each process in group B, and vice versa. The *j*<sup>th</sup> send buffer of process *i* in group A should be consistent with the *i*<sup>th</sup> receive buffer of process *j* in group B, and vice versa.

The number of items that is sent by processes in group A, do not have to be equal the number of items that is sent by processes in group B. In particular, you can move data in only one direction by specifying *sendcount* == 0 for the communication in the reverse direction.

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

[**MPI\_Allgather**](mpi-allgather.md)
</dt> <dt>

[**MPI\_Send**](mpi-send.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> </dl>

 

 




