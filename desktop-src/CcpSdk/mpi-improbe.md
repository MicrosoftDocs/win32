---
Description: 'Probes for a message in a non-blocking way.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5761A549-EA87-4A8F-BE00-FFE5E8535BB7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Improbe function'
---

# MPI\_Improbe function

Probes for a message in a non-blocking way. Provides a mechanism to receive the specific message that was matched regardless of intervening probe/receive operations. The matched message is de-queued off the receive queue, giving the application an opportunity to decide how to receive the message based on the information returned by the non-blocking matching probe operation. The matched message is then received using the [**MPI\_Mrecv**](mpi-mrecv.md) or [**MPI\_Imrecv**](mpi-imrecv.md) function.

## Syntax


```C++
int MPIAPI MPI_Improbe(
  _In_  int         source,
  _In_  int         tag,
  _In_  MPI_Comm    comm,
  _Out_ Int         *flag,
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

*flag* \[out\]
</dt> <dd>

On return, contains a pointer to an integer that indicates whether the specified *source*, *tag*, and *comm* are matched. A non-zero value indicates that the parameters are matched.

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
MPI_IMPROBE(SOURCE, TAG, COMM, FLAG, MESSAGE, STATUS, IERROR)
      INTEGER SOURCE, TAG, COMM, FLAG, MESSAGE, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

This function returns *?ag* = **true** if there is a message that can be received and that matches the pattern speci?ed by the arguments *source*, *tag*, and *comm*. The call matches the same message that would have been received by a call to [**MPI\_Recv**](mpi-recv.md) executed at the same point in the program and returns in status the same value that would have been returned by **MPI\_Recv**. In addition, it returns in *message* a handle to the matched message. Otherwise, the call returns *?ag* = **false** and leaves *status* and *message* unde?ned.

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

[**MPI\_Recv**](mpi-recv.md)
</dt> <dt>

[**MPI\_Imrecv**](mpi-imrecv.md)
</dt> </dl>

 

 




