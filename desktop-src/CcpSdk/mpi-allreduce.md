---
Description: 'Combines values from all processes and distributes the result back to all processes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4ff26760-0a3f-4927-8c8d-ac7d7f662039'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Allreduce function'
---

# MPI\_Allreduce function

Combines values from all processes and distributes the result back to all processes.

## Syntax


```C++
int MPIAPI MPI_Allreduce(
  _In_opt_  const void         *sendbuf,
  _Out_opt_       void         *recvbuf,
  _In_            int          count,
  _In_            MPI_Datatype datatype,
  _In_            MPI_Op       op,
  _In_            MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*sendbuf* \[in, optional\]
</dt> <dd>

The pointer to the data to be sent to all processes in the group. The number and data type of the elements in the buffer are specified in the count and datatype parameters.

If the *comm* parameter references an intracommunicator, you can specify an in place option by specifying **MPI\_IN\_PLACE** in all processes. In this case, the input data is taken at each process from the receive buffer, where it will be replaced by the output data.

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

The **MPI\_Datatype** of each element in the buffer. This parameter must be compatible with the operation as specified in the *op* parameter.

</dd> <dt>

*op* \[in\]
</dt> <dd>

The **MPI\_Op** handle indicating the global reduction operation to perform. The handle can indicate a built-in or application-defined operation. For a list of predefined operations, see [**MPI\_Op**](mpi-op.md).

</dd> <dt>

*comm* \[in\]
</dt> <dd>

The [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_ALLREDUCE(SENDBUF, RECVBUF, COUNT, DATATYPE, OP, COMM, IERROR)
    <type> SENDBUF(*), RECVBUF(*)
    INTEGER COUNT, DATATYPE, OP, COMM, IERROR
```

## Remarks

If *comm* is an intercommunicator, the result of the reduction of the data provided by processes in group A is stored at each process in group B, and vice versa. Both groups should provide *count* and *datatype* arguments that specify the same type signature.

All completion calls (e.g., [**MPI\_Wait**](mpi-wait.md)) are supported for non-blocking reduction operations.

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

[**MPI\_Reduce**](mpi-reduce.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> <dt>

[**MPI\_Op**](mpi-op.md)
</dt> </dl>

 

 




