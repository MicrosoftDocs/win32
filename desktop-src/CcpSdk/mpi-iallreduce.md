---
Description: 'Combines values from all processes and distributes the result back to all processes in a non-blocking way.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0E94E7ED-8194-4AFE-B287-765914559DEA'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Iallreduce function'
---

# MPI\_Iallreduce function

Combines values from all processes and distributes the result back to all processes in a non-blocking way.

## Syntax


```C++
int MPIAPI MPI_Iallreduce(
  _In_opt_  const void         *sendbuf,
  _Out_opt_       void         *recvbuf,
  _In_            int          count,
  _In_            MPI_Datatype datatype,
  _In_            MPI_Op       op,
  _In_            MPI_Comm     comm,
  _Out_           MPI_Request  *request
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in, optional\]
</dt> <dd>

The pointer to the data to be sent to all processes in the group. The number and data type of the elements in the buffer are specified in the *count* and *datatype* parameters.

If the *comm* parameter references an intracommunicator, you can specify an in-place option by specifying **MPI\_IN\_PLACE** in all processes. In this case, the input data is taken at each process from the receive buffer, where it will be replaced by the output data.

</dd> <dt>

*recvbuf* \[out, optional\]
</dt> <dd>

The pointer to a buffer to receive the result of the reduction operation.

</dd> <dt>

*count* \[in\]
</dt> <dd>

The number of elements to send from this process.

</dd> <dt>

*datatype* \[in\]
</dt> <dd>

The data type of each element in the buffer. This parameter must be compatible with the operation as specified in the *op* parameter.

</dd> <dt>

*op* \[in\]
</dt> <dd>

The global reduction operation to perform. The handle can indicate a built-in or application-defined operation. For a list of predefined operations, see [**MPI\_Op**](mpi-op.md).

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
MPI_IALLREDUCE(SENDBUF, RECVBUF, COUNT, DATATYPE, OP, COMM, REQUEST, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER COUNT, DATATYPE, OP, COMM, REQUEST, IERROR
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

[**MPI\_Op**](mpi-op.md)
</dt> <dt>

[**MPI\_Allreduce**](mpi-allreduce.md)
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

 

 




