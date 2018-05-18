---
Description: 'Performs a non-blocking receive for a message matched by MPI\_Mprobe or MPI\_Improbe.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'E91DF5CA-9A31-4D30-B9CC-44AD4BEFF6C2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Imrecv function'
---

# MPI\_Imrecv function

Performs a non-blocking receive for a message matched by [**MPI\_Mprobe**](mpi-mprobe.md) or [**MPI\_Improbe**](mpi-improbe.md).

## Syntax


```C++
int MPIAPI MPI_Imrecv(
  _Out_   void         *buf,
  _In_    int          count,
  _In_    MPI_Datatype datatype,
  _Inout_ MPI_Message  *message,
  _Out_   MPI_Request  *request
);
```



## Parameters

<dl> <dt>

*buf* \[out\]
</dt> <dd>

A pointer to the address of the receive buffer.

</dd> <dt>

*count* \[in\]
</dt> <dd>

The number of *datatype* elements in *buf*.

</dd> <dt>

*datatype* \[in\]
</dt> <dd>

The MPI data type of the elements in *buf*.

</dd> <dt>

*message* \[in, out\]
</dt> <dd>

Contains a pointer to the message.

</dd> <dt>

*request* \[out\]
</dt> <dd>

On return, contains a pointer to an **MPI\_REQUEST** handle representing the communication operation.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_IMRECV(BUF, COUNT, DATATYPE, MESSAGE, REQUEST, IERROR)
    <type> BUF(*)
    INTEGER COUNT, DATATYPE, MESSAGE, REQUEST, IERROR
```

## Remarks

This function is the non-blocking variant of [**MPI\_Mrecv**](mpi-mrecv.md) and starts a non-blocking receive of a matched message. Completion semantics are similar to [**MPI\_Irecv**](mpi-irecv.md).

On return from this function, the message handle is set to **MPI\_MESSAGE\_NULL**.

If this function is called with **MPI\_MESSAGE\_NO\_PROC** as the message argument, the call returns immediately with a request object which, when completed, will yield a status object set to *source* = **MPI\_PROC\_NULL**, *tag* = **MPI\_ANY\_TAG**, and *count* = 0, as if a receive from **MPI\_PROC\_NULL** was issued. A call to this function with **MPI\_MESSAGE\_NULL** is erroneous.

## Requirements



|                    |                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Microsoft MPI v6<br/>                                                                                                                    |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl> |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                           |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                           |



## See also

<dl> <dt>

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> <dt>

[**MPI\_Irecv**](mpi-irecv.md)
</dt> <dt>

[**MPI\_Mrecv**](mpi-mrecv.md)
</dt> <dt>

[**MPI\_Mprobe**](mpi-mprobe.md)
</dt> <dt>

[**MPI\_Improbe**](mpi-improbe.md)
</dt> </dl>

 

 




