---
Description: 'Performs a global reduce operation (for example sum, maximum, or logical and) across all members of a group in a non-blocking way.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8EE81913-0713-4FF3-8723-0EC6641583E3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Ireduce function'
---

# MPI\_Ireduce function

Performs a global reduce operation (for example sum, maximum, or logical and) across all members of a group in a non-blocking way.

## Syntax


```C++
int MPIAPI MPI_Ireduce(
  _In_      void         *sendbuf,
  _Out_opt_ void         *recvbuf,
  _In_      int          count,
  _In_      MPI_Datatype datatype,
  _In_      MPI_Op       op,
  _In_      int          root,
  _In_      MPI_Comm     comm,
  _Out_     MPI_Request  *request
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in\]
</dt> <dd>

The pointer to a buffer containing the data from this rank to be used in the reduction. The buffer consists of *count* successive elements of the **MPI\_Datatype** indicated by the *datatype* handle. The message length is specified in terms of number of elements, not number of bytes.

</dd> <dt>

*recvbuf* \[out, optional\]
</dt> <dd>

The pointer to a buffer to receive the result of the reduction operation. This parameter is significant only at the root process.

</dd> <dt>

*count* \[in\]
</dt> <dd>

The number of elements to send from this process.

</dd> <dt>

*datatype* \[in\]
</dt> <dd>

The **MPI\_Datatype** handle representing the data type of each element in *sendbuf*.

</dd> <dt>

*op* \[in\]
</dt> <dd>

The **MPI\_Op** handle indicating the global reduction operation to perform. The handle can indicate a built-in or application defined operation. For a list of predefined operations, see the [**MPI\_Op**](mpi-op.md) topic.

</dd> <dt>

*root* \[in\]
</dt> <dd>

The rank of the receiving process within the [**MPI\_Comm**](mpi-comm.md) *comm*.

</dd> <dt>

*comm* \[in\]
</dt> <dd>

The [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> <dt>

*request* \[out\]
</dt> <dd>

The **MPI\_Request** handle representing the communication operation..

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_IREDUCE(SENDBUF, RECVBUF, COUNT, DATATYPE, OP, ROOT, COMM, REQUEST, IERROR) 
    <type> SENDBUF(*), RECVBUF(*) 
    INTEGER COUNT, DATATYPE, OP, ROOT, COMM, REQUEST, IERROR
```

## Remarks

A non-blocking call initiates a collective reduction operation which must be completed in a separate completion call. Once initiated, the operation may progress independently of any computation or other communication at participating processes. In this manner, non-blocking reduction operations can mitigate possible synchronizing e?ects of reduction operations by running them in the “background.”

All completion calls (e.g., [**MPI\_Wait**](mpi-wait.md)) are supported for non-blocking reduction operations.

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

[**MPI\_Op**](mpi-op.md)
</dt> <dt>

[**MPI\_Reduce**](mpi-reduce.md)
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

 

 




