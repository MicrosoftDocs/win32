---
Description: 'Initiates a receive operation and returns a handle to the requested communication operation.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '033ac026-a3a4-455f-9f4d-ba64ac7623e7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Irecv function'
---

# MPI\_Irecv function

Initiates a receive operation and returns a handle to the requested communication operation.

## Syntax


```C++
int MPIAPI MPI_Irecv(
  _In_opt_ void         *buf,
           int          count,
           MPI_Datatype datatype,
           int          source,
           int          tag,
           MPI_Comm     comm,
  _Out_    MPI_Request  *request
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

The number of elements in the buffer array. If the data part of the message is empty, set the *count* parameter to 0.

</dd> <dt>

*datatype* 
</dt> <dd>

The data type of the elements in the buffer.

</dd> <dt>

*source* 
</dt> <dd>

The rank of the sending process within the specified communicator. Specify the **MPI\_ANY\_SOURCE** constant to specify that any source is acceptable.

</dd> <dt>

*tag* 
</dt> <dd>

The message tag that can be used to distinguish different types of messages. Specify the **MPI\_ANY\_TAG** constant to indicate that any tag is acceptable.

</dd> <dt>

*comm* 
</dt> <dd>

The handle to the communicator.

</dd> <dt>

*request* \[out\]
</dt> <dd>

On return, contains a handle to the requested communication operation.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_IRECV(BUF, COUNT, DATATYPE, SOURCE, TAG, COMM, REQUEST, IERROR)
    <type> BUF(*)
    INTEGER COUNT, DATATYPE, SOURCE, TAG, COMM, REQUEST, IERROR
```

## Remarks

This function is local, it returns immediately, and does not wait for any other process. This function can return before the message is received into the buffer.

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

[**MPI\_Recv**](mpi-recv.md)
</dt> <dt>

[**MPI\_Wait**](mpi-wait.md)
</dt> <dt>

[**MPI\_Test**](mpi-test.md)
</dt> <dt>

[**MPI\_Comm**](mpi-comm.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> </dl>

 

 




