---
Description: 'Gathers data from all members of a group to one member in a non-blocking way.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '60C7DA65-D001-4959-AE7C-78D943A981EA'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Igather function'
---

# MPI\_Igather function

Gathers data from all members of a group to one member in a non-blocking way.

## Syntax


```C++
int WINAPI MPI_Igather(
  _In_      void         *sendbuf,
            int          sendcount,
            MPI_Datatype sendtype,
  _Out_opt_ void         *recvbuf,
  _In_      int          recvcount,
  _In_      MPI_Datatype recvtype,
  _In_      int          root,
  _In_      MPI_Comm     comm,
  _Out_     MPI_Request  *request
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

The pointer to a buffer containing the data to be sent to the root. The buffer consists of *sendcount* successive elements of the **MPI\_Datatype** indicated by the *sendtype* handle. The message length is specified in terms of number of elements, not number of bytes.

</dd> <dt>

*sendcount* 
</dt> <dd>

The number of *sendtype* elements in *sendbuf*. If the value is zero, the data part of the message is empty.

</dd> <dt>

*sendtype* 
</dt> <dd>

The **MPI\_Datatype** handle representing the data type of each element in *sendbuf*.

</dd> <dt>

*recvbuf* \[out, optional\]
</dt> <dd>

The pointer to a buffer containing the data received from each process on the root, including data sent by the root process (significant only at root). The receive buffer *recvbuf* is ignored for all non-root processes. On the root process, *recvbuf* consists of *recvcount* successive elements of the **MPI\_Datatype** indicated by the *recvtype* handle. The message length is specified in terms of number of elements, not number of bytes.

</dd> <dt>

*recvcount* \[in\]
</dt> <dd>

The number of *recvtype* elements in *recvbuf*. If the value is zero, the data part of the message is empty (significant only at root).

</dd> <dt>

*recvtype* \[in\]
</dt> <dd>

The **MPI\_Datatype** handle representing the data type of each element in *recvbuf* (significant only at root).

</dd> <dt>

*root* \[in\]
</dt> <dd>

The rank of the receiving process within the [**MPI\_Comm**](mpi-comm.md)*comm.*

</dd> <dt>

*comm* \[in\]
</dt> <dd>

The [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> <dt>

*request* \[out\]
</dt> <dd>

The **MPI\_Request** handle representing the communication operation.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_IGATHER(SENDBUF, SENDCOUNT, SENDTYPE, RECVBUF, RECVCOUNT, RECVTYPE,
ROOT, COMM, REQUEST, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER SENDCOUNT, SENDTYPE, RECVCOUNT, RECVTYPE, ROOT, COMM, REQUEST, IERROR
```

## Remarks

A non-blocking call initiates a collective gather operation which must be completed in a separate completion call. Once initiated, the operation may progress independently of any computation or other communication at participating processes. In this manner, non-blocking gather operations can mitigate possible synchronizing e?ects of gather operations by running them in the “background.”

All completion calls (e.g., [**MPI\_Wait**](mpi-wait.md)) are supported for non-blocking gather operations.

## Requirements



|                    |                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Microsoft MPI v6<br/>                                                                                                                    |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl> |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                           |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                           |



## See also

<dl> <dt>

[MPI Collective Functions](mpi-collective-functions.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> <dt>

[**MPI\_Gather**](mpi-gatherv.md)
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

 

 




