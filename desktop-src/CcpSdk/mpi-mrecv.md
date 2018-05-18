---
Description: 'Performs a blocking receive for a message matched by MPI\_Mprobe or MPI\_Improbe.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'C31BC7F5-80CD-42FE-9BF9-E6D81A1231C4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Mrecv function'
---

# MPI\_Mrecv function

Performs a blocking receive for a message matched by [**MPI\_Mprobe**](mpi-mprobe.md) or [**MPI\_Improbe**](mpi-improbe.md).

## Syntax


```C++
int MPIAPI MPI_Mrecv(
  _Out_   void         *buf,
  _In_    int          count,
  _In_    MPI_Datatype datatype,
  _Inout_ MPI_Message  *message,
  _Out_   MPI_Status   *status
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

The MPI data type of the elements in the buffer array.

</dd> <dt>

*message* \[in, out\]
</dt> <dd>

Contains a pointer to the message.

</dd> <dt>

*status* \[out\]
</dt> <dd>

On return, contains a pointer to an [**MPI\_Status**](mpi-status.md) structure where information about the message is stored.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_MRECV(BUF, COUNT, DATATYPE, MESSAGE, STATUS, IERROR)
    <type> BUF(*)
    INTEGER COUNT, DATATYPE, MESSAGE, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

This function receives a message matched by a matching probe operation. The receive bu?er consists of the storage containing *count* consecutive elements of the type speci?ed by *datatype*, starting at address *buf*. The length of the received message must be less than or equal to the length of the receive bu?er. An over?ow error occurs if all incoming data does not ?t, without truncation, into the receive bu?er.

If the message is shorter than the receive bu?er, then only those locations corresponding to the (shorter) message are modi?ed.

On return from this function, the message handle is set to **MPI\_MESSAGE\_NULL**. All errors that occur during the execution of this operation are handled according to the error handler set for the communicator used in the matching probe call that produced the message handle

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

[**MPI\_Mprobe**](mpi-mprobe.md)
</dt> <dt>

[**MPI\_Improbe**](mpi-improbe.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> <dt>

[**MPI\_Imrecv**](mpi-imrecv.md)
</dt> </dl>

 

 




