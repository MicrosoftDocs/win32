---
Description: 'Gathers a variable amount of data from each member of a group and sends the data to all members of the group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6f44ceb1-8213-4541-a2d8-639a84a38be2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Allgatherv function'
---

# MPI\_Allgatherv function

Gathers a variable amount of data from each member of a group and sends the data to all members of the group. The **MPI\_Allgatherv** function is like the [**MPI\_Gatherv**](mpi-gatherv.md), except that all processes receive the result, instead of just the root. The block of data that is sent from the *j*<sup>th</sup> process is received by every process and placed in the *j*<sup>th</sup> block of the buffer *recvbuf*. These blocks do not all have to be the same size.

## Syntax


```C++
int MPIAPI MPI_Allgatherv(
  _In_  void         *sendbuf,
        int          sendcount,
        MPI_Datatype sendtype,
  _Out_ void         *recvbuf,
  _In_  int          *recvcounts,
  _In_  int          *displs,
        MPI_Datatype recvtype,
        MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

The pointer to the data to be sent to all processes in the group. The number and data type of the elements in the buffer are specified in the *sendcount* and *sendtype* parameters. Each element in the buffer corresponds to a process in the group.

If the comm parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in all processes. The *sendcount* and *sendtype* parameters are ignored. Each process enters data in the corresponding receive buffer element. The *n*<sup>th</sup> process sends data to the *n*<sup>th</sup> element of the receive buffer.

</dd> <dt>

*sendcount* 
</dt> <dd>

The number of data elements that this process sends in the buffer that is specified in the *sendbuf* parameter. If an element in *sendcount* is zero, the data part of the message from that process is empty.

</dd> <dt>

*sendtype* 
</dt> <dd>

The MPI data type of the elements in the send buffer.

</dd> <dt>

*recvbuf* \[out\]
</dt> <dd>

The pointer to a buffer that contains the data that is received from each process. The number and data type of the elements in the buffer are specified in the *recvcount* and *recvtype* parameters.

</dd> <dt>

*recvcounts* \[in\]
</dt> <dd>

The number of data elements from each communicator process in the receive buffer.

</dd> <dt>

*displs* \[in\]
</dt> <dd>

The location, relative to the *recvbuf* parameter, of the data from each communicator process.

In the *recvbuf*, *recvcounts*, and *displs* parameter arrays, the *n*<sup>th</sup> element of each array refers to the data that is received from the *n*<sup>th</sup> communicator process.

</dd> <dt>

*recvtype* 
</dt> <dd>

The MPI data type of each element in buffer.

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
MPI_ALLGATHERV(SENDBUF, SENDCOUNT, SENDTYPE, RECVBUF, RECVCOUNTS,DISPLS, RECVTYPE,COMM, IERROR)
    <type> SENDBUF(*), R.ECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, RECVCOUNTS(*), DISPLS(*), RECVTYPE, COMM, IERROR
```

## Remarks

The usage rules for **MPI\_Allgatherv** correspond to the rules for [**MPI\_Gatherv**](mpi-gatherv.md).

The type signature that is associated with the *sendtype* parameter on a process must be equal to the type signature that is associated with the *recvtype* parameter on any other process.

If the *comm* parameter references an intracommunicator, the outcome of a call to `MPI_Allgatherv(...)`is as if all processes executed calls to `MPI_GatherV(sendbuf,sendcount,sendtype,recvbuf,recvcounts,displs,recvtype,root,comm)`, for `root = 0 , ..., n-1`.

If the *comm* parameter references an intercommunicator, then each process of one group, for example, group A, contributes the number of data items that are specified in the *sendcount* parameter. This data is concatenated, and the result is stored at each process in the other group, group B. Conversely, the concatenation of the data of the processes in group B is stored at each process in group A. The send buffer parameters in group A must be consistent with the receive buffer parameters in group B, and vice versa.

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

[**MPI\_Gatherv**](mpi-gatherv.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> </dl>

 

 




