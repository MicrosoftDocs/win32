---
Description: 'Performs a receive operation and does not return until a matching message is received.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3268d295-b055-4960-bee4-6ba9dbe50904'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Recv function'
---

# MPI\_Recv function

Performs a receive operation and does not return until a matching message is received.

## Syntax


```C++
int MPIAPI MPI_Recv(
  _In_opt_ void         *buf,
           int          count,
           MPI_Datatype datatype,
           int          source,
           int          tag,
           MPI_Comm     comm,
  _Out_    MPI_Status   *status
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

The data type of the elements in the buffer array.

</dd> <dt>

*source* 
</dt> <dd>

The rank of the sending process within the specified communicator. Specify the **MPI\_ANY\_SOURCE** constant to specify that any source is acceptable.

</dd> <dt>

*tag* 
</dt> <dd>

The message tag that is used to distinguish different types of messages. Specify the **MPI\_ANY\_TAG** constant to indicate that any tag is acceptable.

</dd> <dt>

*comm* 
</dt> <dd>

The handle to the communicator.

</dd> <dt>

*status* \[out\]
</dt> <dd>

On return, contains a pointer to an [**MPI\_Status**](mpi-status.md) structure where information about the received message is stored.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_RECV(BUF, COUNT, DATATYPE, SOURCE, TAG, COMM, STATUS, IERROR)
    <type> BUF(*)
    INTEGER COUNT, DATATYPE, SOURCE, TAG, COMM, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

The length of the received message must be less than or equal to the length of the receive buffer. This function returns an overflow error if all incoming data does not fit into the receive buffer.

If the received message is shorter than the buffer, only the part of the buffer that corresponds to the message is modified. The remainder of the buffer is not modified.

Processes can send messages to themselves. However, it is unsafe to do so with the blocking send and receive operations, [**MPI\_Send**](mpi-send.md) and **MPI\_Recv**, because these blocking send and receive operations can cause a deadlock.

> [!Note]  
> There is an asymmetry between send and receive operations. A receive operation can accept messages from an arbitrary sender, but a send operation must specify a unique receiver. This implements a push style of communication, where data transfer is effected by the sender, rather than a pull style where data transfer is effected by the receiver.

 

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

[**MPI\_Irecv**](mpi-irecv.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> <dt>

[**MPI\_Comm**](mpi-comm.md)
</dt> <dt>

[**MPI\_Status**](mpi-status.md)
</dt> </dl>

 

 




