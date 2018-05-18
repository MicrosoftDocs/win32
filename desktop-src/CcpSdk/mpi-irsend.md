---
Description: 'Initiates a ready mode send operation and returns a request handle that represents the communication operation.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'be8e193d-4341-4f20-aa31-40c9640a8bca'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Irsend function'
---

# MPI\_Irsend function

Initiates a ready mode send operation and returns a request handle that represents the communication operation.

## Syntax


```C++
int MPIAPI MPI_Irsend(
  _In_opt_ void         *buf,
           int          count,
           MPI_Datatype datatype,
           int          dest,
           int          tag,
           MPI_Comm     comm,
  _Out_    MPI_Request  *request
);
```



## Parameters

<dl> <dt>

*buf* \[in, optional\]
</dt> <dd>

A pointer to the buffer that contains the data to be sent. The buffer consists of count successive elements of the MPI\_Datatype object that is indicated by the *datatype* handle. The message length is specified in terms of number of elements, not in number of bytes. The caller should not modify any part of the send buffer until the communication operation is completed.

</dd> <dt>

*count* 
</dt> <dd>

The number of elements in the buffer array. If count is zero, the data part of the message is empty.

</dd> <dt>

*datatype* 
</dt> <dd>

A handle that represents the data type of the elements in the buffer.

</dd> <dt>

*dest* 
</dt> <dd>

The rank of the destination process within the communicator *comm* parameter.

</dd> <dt>

*tag* 
</dt> <dd>

The message tag that is used to distinguish different types of messages.

</dd> <dt>

*comm* 
</dt> <dd>

The handle to the communicator.

</dd> <dt>

*request* \[out\]
</dt> <dd>

On return, a pointer to a handle that represents the communication operation.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_IRSEND(BUF, COUNT, DATATYPE, DEST, TAG, COMM, REQUEST, IERROR)
    <type> BUF(*)
    INTEGER COUNT, DATATYPE, DEST, TAG, COMM, REQUEST, IERROR
```

## Remarks

This function can return before the message was copied out of the send buffer. This function is local, it returns immediately, irrespective of the status of other processes. See the remarks for the [**MPI\_Rsend**](mpi-rsend.md) function for the description of the ready communication mode.

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

[**MPI\_Rsend**](mpi-rsend.md)
</dt> <dt>

[**MPI\_Recv**](mpi-recv.md)
</dt> <dt>

[**MPI\_Irecv**](mpi-irecv.md)
</dt> <dt>

[**MPI\_Wait**](mpi-wait.md)
</dt> <dt>

[**MPI\_Test**](mpi-test.md)
</dt> <dt>

[**MPI\_Comm**](mpi-comm.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> </dl>

 

 




