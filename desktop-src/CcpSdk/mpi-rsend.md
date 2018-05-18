---
Description: 'Performs a ready mode send operation and returns when the send buffer can be safely reused.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '28076c76-7ea3-4ac3-996c-b36619565227'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Rsend function'
---

# MPI\_Rsend function

Performs a ready mode send operation and returns when the send buffer can be safely reused.

## Syntax


```C++
int MPIAPI MPI_Rsend(
  _In_opt_ void         *buf,
           int          count,
           MPI_Datatype datatype,
           int          dest,
           int          tag,
           MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*buf* \[in, optional\]
</dt> <dd>

A pointer to the buffer that contains the data to be sent.

</dd> <dt>

*count* 
</dt> <dd>

The number of elements in the buffer. If the data part of the message is empty, set the *count* parameter to 0.

</dd> <dt>

*datatype* 
</dt> <dd>

The data type of the elements in the buffer.

</dd> <dt>

*dest* 
</dt> <dd>

The rank of the destination process within the communicator that is specified by the *comm* parameter.

</dd> <dt>

*tag* 
</dt> <dd>

The message tag that can be used to distinguish different types of messages.

</dd> <dt>

*comm* 
</dt> <dd>

The handle to the communicator.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_RSEND(BUF, COUNT, DATATYPE, DEST, TAG, COMM, IERROR)
    <type> BUF(*)
    INTEGER COUNT, DATATYPE, DEST, TAG, COMM, IERROR
```

## Remarks

This function is non-local. This function returns as soon as the send buffer can be reused and does not depend on the status of a matching receive operation. However, the successful completion of the overall send operation depends on the existence of a matching receive operation.

This function can only be called if the matching receive operation is already posted. Otherwise, the function returns an error and its result is undefined. On some systems, this requirement eliminates some of the handshaking that is used in other modes, and can improve performance compared to the standard or synchronous send operations.

The **MPI\_Rsend** function has the same semantics as the [**MPI\_Send**](mpi-send.md) and [**MPI\_Ssend**](mpi-ssend.md) functions, but it notifies the system that a matching receive is already posted. That information can save some overhead. Therefore, in a correct program, a ready send could be replaced by a standard send with no effect on the behavior of the program other than performance.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> <dt>

[**MPI\_Send**](mpi-send.md)
</dt> <dt>

[**MPI\_Bsend**](mpi-bsend.md)
</dt> <dt>

[**MPI\_Ssend**](mpi-ssend.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> </dl>

 

 




