---
Description: 'Performs a synchronous mode send operation and returns when the send buffer can be safely reused.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dea32116-1bf7-479a-a5c0-25158844a739'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Ssend function'
---

# MPI\_Ssend function

Performs a synchronous mode send operation and returns when the send buffer can be safely reused.

## Syntax


```C++
int MPIAPI MPI_Ssend(
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
MPI_SSEND(BUF, COUNT, DATATYPE, DEST, TAG, COMM, IERROR)
    <type> BUF(*)
    INTEGER COUNT, DATATYPE, DEST, TAG, COMM, IERROR
```

## Remarks

This function is non-local. Successful completion of the send operation depends on the occurrence of a matching receive function.

This function can be called whether or not a matching receive is posted. However, the send function is completed successfully only if a matching receive is posted, and the receive operation has started to receive the message. Therefore, the completion of a synchronous send not only indicates that the send buffer can be reused, but it also indicates that the receiving process has started to execute the matching receive.

If both send and receive operations are blocking operations, then the synchronous mode provides synchronous communication semantics; a communication is not completed at either end until the send and receive processes have finished.

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

[**MPI\_Rsend**](mpi-rsend.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> </dl>

 

 




