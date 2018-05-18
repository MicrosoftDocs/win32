---
Description: 'Gathers data from all members of a group and sends the data to all members of the group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '85205349-5573-404a-b8c0-1273f3a442e5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Allgather function'
---

# MPI\_Allgather function

Gathers data from all members of a group and sends the data to all members of the group. The **MPI\_Allgather** function is similar to the [**MPI\_Gather**](mpi-gather.md) function, except that it sends the data to all processes instead of only to the root. The usage rules for **MPI\_Allgather** correspond to the rules for **MPI\_Gather**.

## Syntax


```C++
int MPIAPI MPI_Allgather(
  _In_  void         *sendbuf,
  _In_  int          sendcount,
  _In_  MPI_Datatype sendtype,
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

The pointer to the data to be sent to all processes in the group. The number and data type of the elements in the buffer are specified in the *sendcount* and *sendtype* parameters. Each element in the buffer corresponds to a process in the group.

If the *comm* parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in all processes. The *sendcount* and *sendtype* parameters are ignored. Each process enters data in the corresponding receive buffer element. The *n*<sup>th</sup> process sends data to the *n*<sup>th</sup> element of the receive buffer.

</dd> <dt>

*sendcount* \[in\]
</dt> <dd>

The number of elements in the buffer that is specified in the *sendbuf* parameter. If *sendcount* is zero, the data part of the message is empty.

</dd> <dt>

*sendtype* \[in\]
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
MPI_ALLGATHER(SENDBUF, SENDCOUNT, SENDTYPE, RECVBUF, RECVCOUNT, RECVTYPE, COMM, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, RECVCOUNT, RECVTYPE, COMM, IERROR
```

## Remarks

The type signature that is associated with the *sendtype* parameter on a process must be equal to the type signature that is associated with the *recvtype* parameter on any other process.

If the *comm* parameter references an intracommunicator, the outcome of a call to `MPI_ALLGATHER(...)` is as if all processes executed n calls to `MPI_Gather(sendbuf,sendcount,sendtype,recvbuf,recvcount,recvtype,root,comm)` for `root = 0 , ..., n-1`.

If the *comm* parameter references an intercommunicator, then each process of one group, for example, group A, contributes the number of data items that are specified in the *sendcount* parameter. This data is concatenated, and the result is stored at each process in the other group, group B. Conversely, the concatenation of the data of the processes in group B is stored at each process in group A. The send buffer parameters in group A must be consistent with the receive buffer parameters in group B, and vice versa.

The number of items, which are sent by processes in group A, do not have to equal the number of items that are sent by processes in group B. In particular, you can move data in only one direction by specifying *sendcount* == 0 for the communication in the reverse direction.

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
</dt> </dl>

 

 




