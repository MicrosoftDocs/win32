---
Description: 'Scatters data from one member across all members of a group in a non-blocking way. This function performs the inverse of the operation that is performed by the MPI\_Igather function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '17138DD8-9BBF-45F2-A31B-252B90EBD0C8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Iscatter function'
---

# MPI\_Iscatter function

Scatters data from one member across all members of a group in a non-blocking way. This function performs the inverse of the operation that is performed by the [**MPI\_Igather**](mpi-igather.md)function.

## Syntax


```C++
int MPIAPI MPI_Iscatter(
  _In_opt_  const void         *sendbuf,
  _In_             int         sendcount,
  _In_            MPI_Datatype sendtype,
  _Out_opt_       void         *recvbuf,
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

The pointer to a buffer that contains the data to be sent to the root process.

This parameter is ignored for all non-root processes.

If the *comm* parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in the root process. The *recvcount* and *recvtype* parameters are ignored. The scattered vector is still considered to contain *n* segments, where *n* is the group size; the segment that corresponds to the root process is not moved.

</dd> <dt>

*sendcount* \[in\]
</dt> <dd>

The number of elements in the send buffer. If *sendcount* is zero, the data part of the message is empty.

This parameter is ignored for all non-root processes.

</dd> <dt>

*sendtype* \[in\]
</dt> <dd>

The data type of each element in the buffer.

This parameter is ignored for all non-root processes.

</dd> <dt>

*recvbuf* \[out, optional\]
</dt> <dd>

The handle to a buffer that contains the data that is received on each process. The number and data type of the elements in the buffer are specified in the *recvcount* and *recvtype* parameters.

</dd> <dt>

*recvcount* \[in\]
</dt> <dd>

The number of elements in the receive buffer. If the count is zero, the data part of the message is empty.

</dd> <dt>

*recvtype* \[in\]
</dt> <dd>

The MPI data type of the elements in the receive buffer.

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
MPI_ISCATTER(SENDBUF, SENDCOUNT, SENDTYPE, RECVBUF, RECVCOUNT, RECVTYPE, ROOT, COMM, REQUEST, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, RECVCOUNT, RECVTYPE, ROOT, COMM, REQUEST, IERROR
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

[**MPI\_Scatter**](mpi-scatter.md)
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

 

 




