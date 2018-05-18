---
Description: 'Gathers variable data from all members of a group to one member in a non-blocking way.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7857E458-3F26-473E-9A37-F5F604B0EBA5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Igatherv function'
---

# MPI\_Igatherv function

Gathers variable data from all members of a group to one member in a non-blocking way.

## Syntax


```C++
int MPIAPI MPI_Igatherv(
  _In_opt_  const void         *sendbuf,
  _In_            int          sendcount,
  _In_            MPI_Datatype sendtype,
  _Out_opt_       void         *recvbuf,
  _In_opt_  const int          recvcounts[],
  _In_opt_  const int          displs[],
  _In_            MPI_Datatype recvtype,
  _In_            int          root,
  _In_            MPI_Comm     comm,
  _Out_           MPI_Request  *request
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in, optional\]
</dt> <dd>

The handle to a buffer that contains the data to be sent to the root process.

If the *comm* parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in all processes. The *sendcount* and *sendtype* parameters are ignored. Each process enters data in the corresponding receive buffer element. The *n*<sup>th</sup> process sends data to the *n*<sup>th</sup> element of the receive buffer. The data that is sent by the root process is assumed to be in the correct place in the receive buffer.

</dd> <dt>

*sendcount* \[in\]
</dt> <dd>

The number of elements in the send buffer. If *sendcount* is zero, the data part of the message is empty.

</dd> <dt>

*sendtype* \[in\]
</dt> <dd>

The data type of each element in the buffer.

</dd> <dt>

*recvbuf* \[out, optional\]
</dt> <dd>

The handle to a buffer on the root process that contains the data that is received from each process, including data that is sent by the root process. This parameter is significant only at the root process. The *recvbuf* parameter is ignored for all non-root processes.

</dd> <dt>

*recvcounts\[\]* \[in, optional\]
</dt> <dd>

The number of elements that is received from each process. Each element in the array corresponds to the rank of the sending process. If the count is zero, the data part of the message is empty. This parameter is significant only at the root process.

</dd> <dt>

*displs\[\]* \[in, optional\]
</dt> <dd>

The location, relative to the *recvbuf* parameter, of the data from each communicator process. The data that is received from process *j* is placed into the receive buffer of the root process offset *displs\[j\]* elements from the *sendbuf* pointer.

In the *recvbuf*, *recvcounts*, and *displs* parameter arrays, the *n*<sup>th</sup> element of each array refers to the data that is received from the *n*<sup>th</sup> communicator process.

This parameter is significant only at the root process.

</dd> <dt>

*recvtype* \[in\]
</dt> <dd>

The data type of each element in buffer. This parameter is significant only at the root process.

</dd> <dt>

*root* \[in\]
</dt> <dd>

The rank of the receiving process within the specified communicator.

</dd> <dt>

*comm* \[in\]
</dt> <dd>

The [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> <dt>

*request* \[out\]
</dt> <dd>

The [**MPI\_Request**](mpi-comm.md) handle representing the communication operation.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_IGATHERV(SENDBUF, SENDCOUNT, SENDTYPE, RECVBUF, RECVCOUNTS, DISPLS, RECVTYPE,
ROOT, COMM, REQUEST, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, RECVCOUNTS(*), DISPLS(*), RECVTYPE, ROOT, COMM, REQUEST, IERROR
```

## Remarks

A non-blocking call initiates a collective reduction operation which must be completed in a separate completion call. Once initiated, the operation may progress independently of any computation or other communication at participating processes. In this manner, non-blocking reduction operations can mitigate possible synchronizing e?ects of reduction operations by running them in the “background.”

All completion calls (e.g., [**MPI\_Wait**](mpi-wait.md)) are supported for non-blocking reduction operations.

## Requirements



|                    |                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Microsoft MPI v7<br/>                                                                                                                    |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl> |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                           |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                           |



## See also

<dl> <dt>

[MPI Collective Functions](mpi-collective-functions.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> <dt>

[**MPI\_Gatherv**](mpi-gatherv.md)
</dt> <dt>

[**MPI\_Test**](mpi-test.md)
</dt> <dt>

[**MPI\_Testall**](mpi-testall.md)
</dt> <dt>

[**MPI\_Testany**](mpi-testany.md)
</dt> <dt>

[**MPI\_Testsome**](mpi-testsome.md)
</dt> <dt>

[**MPI\_Wait**](mpi-wait.md)
</dt> <dt>

[**MPI\_Waitall**](mpi-waitall.md)
</dt> <dt>

[**MPI\_Waitany**](mpi-waitany.md)
</dt> <dt>

[**MPI\_Waitsome**](mpi-waitsome.md)
</dt> </dl>

 

 




