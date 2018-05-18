---
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5675B3BF-395B-44B6-9CC0-A6DD9428974A'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Iscatterv function'
---

# MPI\_Iscatterv function

## Syntax


```C++
int MPIAPI MPI_Iscatterv(
  _In_opt_  const void         *sendbuf,
  _In_opt_  const int          sendcounts[],
  _In_opt_  const int          displs[],
  _In_            MPI_Datatype sendtype,
  _Out_opt_        void        *recvbuf,
  _In_            int          recvcount,
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

The pointer to a buffer that contains the data to be sent by the root process.

This parameter is ignored for all non-root processes.

If the *comm* parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in the root process. The *recvcount* and *recvtype* parameters are ignored. The scattered vector is still considered to contain *n* segments, where *n* is the group size; the segment that corresponds to the root process is not moved.

</dd> <dt>

*sendcounts\[\]* \[in, optional\]
</dt> <dd>

The number of elements to send to each process. If *sendcounts*\[*i*\] is zero, the data part of the message for that process is empty.

This parameter is ignored for all non-root processes.

</dd> <dt>

*displs\[\]* \[in, optional\]
</dt> <dd>

The locations of the data to send to each communicator process. Each location in the array is relative to the corresponding element of the *sendbuf* array.

In the *sendbuf*, *sendcounts*, and *displs* parameter arrays, the *n*<sup>th</sup> element of each array refers to the data to be sent to the *n*<sup>th</sup> communicator process.

This parameter is significant only at the root process.

</dd> <dt>

*sendtype* \[in\]
</dt> <dd>

The data type of each element in the buffer.

This parameter is ignored for all non-root processes.

</dd> <dt>

*recvbuf* \[out, optional\]
</dt> <dd>

The pointer to a buffer that contains the data that is received on each process. The number and data type of the elements in the buffer are specified in the *recvcount* and *recvtype* parameters.

</dd> <dt>

*recvcount* \[in\]
</dt> <dd>

The number of elements in the receive buffer. If the count is zero, the data part of the message is empty.

</dd> <dt>

*recvtype* \[in\]
</dt> <dd>

The data type of the elements in the receive buffer.

</dd> <dt>

*root* \[in\]
</dt> <dd>

The rank in the sending process within the specified communicator.

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
MPI_ISCATTERV(SENDBUF, SENDCOUNTS, DISPLS, SENDTYPE, RECVBUF, RECVCOUNT, RECVTYPE, ROOT, COMM, REQUEST, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER SENDCOUNTS(*), DISPLS(*), SENDTYPE, RECVCOUNT, RECVTYPE, ROOT, COMM, REQUEST, IERROR
```

## Remarks

A non-blocking call initiates a collective reduction operation which must be completed in a separate completion call. Once initiated, the operation may progress independently of any computation or other communication at participating processes. In this manner, non-blocking reduction operations can mitigate possible synchronizing e?ects of reduction operations by running them in the “background.”

All completion calls (e.g., [**MPI\_Wait)**](mpi-wait.md) are supported for non-blocking reduction operations.

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

[**MPI\_Scatterv**](mpi-scatterv.md)
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

 

 




