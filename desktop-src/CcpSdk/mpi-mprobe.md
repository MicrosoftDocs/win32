---
Description: 'Blocking probes for a message.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'A54B0A78-045E-4D90-AC91-761893AD8DB5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Mprobe function'
---

# MPI\_Mprobe function

Blocking probes for a message. Provides a mechanism to receive the specific message that was matched regardless of intervening probe/receive operations. The matched message is de-queued off the receive queue, giving the application an opportunity to decide how to receive the message based on the information returned by the matching probe operation. The matched message is then received using the [**MPI\_Mrecv**](mpi-mrecv.md) or [**MPI\_Imrecv**](mpi-imrecv.md) function.

## Syntax


```C++
int MPIAPI MPI_Mprobe(
  _In_  int         source,
  _In_  int         tag,
  _In_  MPI_Comm    comm,
  _Out_ MPI_Message *message,
  _Out_ MPI_Status  *status
);
```



## Parameters

<dl> <dt>

*source* \[in\]
</dt> <dd>

Source rank or **MPI\_ANY\_SOURCE**.

</dd> <dt>

*tag* \[in\]
</dt> <dd>

Message tag or **MPI\_ANY\_TAG**.

</dd> <dt>

*comm* \[in\]
</dt> <dd>

MPI communicator handle.

</dd> <dt>

*message* \[out\]
</dt> <dd>

On return, contains a pointer to the matched message.

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
MPI_MPROBE(SOURCE, TAG, COMM, MESSAGE, STATUS, IERROR)
      INTEGER SOURCE, TAG, COMM, MESSAGE, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

This function behaves like [**MPI\_Improbe**](mpi-improbe.md) except that it is a blocking call that returns only after a matching message has been found.

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

[**MPI\_Improbe**](mpi-improbe.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> <dt>

[**MPI\_Imrecv**](mpi-imrecv.md)
</dt> </dl>

 

 




