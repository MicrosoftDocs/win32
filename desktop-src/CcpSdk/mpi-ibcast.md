---
Description: 'Broadcasts a message from the process with rank &\#0034;root&\#0034; to all other processes of the communicator in a non-blocking way.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2DBA6049-967D-41C1-A84C-942AE694A922'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Ibcast function'
---

# MPI\_Ibcast function

Broadcasts a message from the process with rank "root" to all other processes of the communicator in a non-blocking way.

## Syntax


```C++
int MPIAPI MPI_Ibcast(
  _Inout_  void        *buffer,
  _In_    int          count,
  _In_    MPI_Datatype datatype,
  _In_    int          root,
  _In_    MPI_Comm     comm,
  _Out_   MPI_Request  *request
);
```



## Parameters

<dl> <dt>

*buffer* \[in, out\]
</dt> <dd>

The pointer to the data buffer. On the process that is specified by the *root* parameter, the buffer contains the data to be broadcast. On all other processes in the communicator that is specified by the *comm* parameter, the buffer receives the data broadcast by the root process. *buffer* consists of *count* successive elements of the **MPI\_Datatype** indicated by the *datatype* handle. The message length is specified in terms of number of elements, not number of bytes.

</dd> <dt>

*count* \[in\]
</dt> <dd>

The number of data elements in the buffer. If the *count* parameter is zero, the data part of the message is empty.

</dd> <dt>

*datatype* \[in\]
</dt> <dd>

The **MPI\_Datatype** handle representing the data type of each element in *buffer*.

</dd> <dt>

*root* \[in\]
</dt> <dd>

The rank of the process within the **MPI\_Comm** *comm* sending *buffer.*

</dd> <dt>

*comm* \[in\]
</dt> <dd>

The [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> <dt>

*request* \[out\]
</dt> <dd>

**MPI\_Request** handle representing the communication operation..

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_IBCAST(BUFFER, COUNT, DATATYPE, ROOT, COMM, REQUEST, IERROR)
    <type> BUFFER(*)  
    INTEGER COUNT, DATATYPE, ROOT, COMM, REQUEST, IERROR
```

## Remarks

A non-blocking call initiates a collective broadcast operation which must be completed in a separate completion call. Once initiated, the operation may progress independently of any computation or other communication at participating processes. In this manner, non-blocking broadcast operations can mitigate possible synchronizing e?ects of broadcast operations by running them in the “background.”

All completion calls (e.g., [**MPI\_Wait**](mpi-wait.md)) are supported for non-blocking broadcast operations.

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

[**MPI\_Bcast**](mpi-bcast.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
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
</dt> <dt>

[**MPI\_Comm**](mpi-comm.md)
</dt> </dl>

 

 




