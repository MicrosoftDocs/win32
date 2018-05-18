---
Description: 'Broadcasts data from one member of a group to all members of the group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '92e6be4d-915c-49a4-80fe-5abbc88b57b2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Bcast function'
---

# MPI\_Bcast function

Broadcasts data from one member of a group to all members of the group.

## Syntax


```C++
int MPIAPI MPI_Bcast(
  _Inout_  void        *buffer,
  _In_    int          count,
  _In_    MPI_Datatype datatype,
  _In_    int          root,
  _In_    MPI_Comm     comm
);
```



## Parameters

<dl> <dt>

*buffer* \[in, out\]
</dt> <dd>

The pointer to the data buffer. On the process that is specified by the *root* parameter, the buffer contains the data to be broadcast. On all other processes in the communicator that is specified by the *comm* parameter, the buffer receives the data broadcast by the root process.

</dd> <dt>

*count* \[in\]
</dt> <dd>

The number of data elements in the buffer. If the *count* parameter is zero, the data part of the message is empty.

</dd> <dt>

*datatype* \[in\]
</dt> <dd>

The MPI data type of the elements in the send buffer.

</dd> <dt>

*root* \[in\]
</dt> <dd>

The rank of the process that is sending the data.

</dd> <dt>

*comm* \[in\]
</dt> <dd>

The [**MPI\_Comm**](mpi-comm.md) communicator handle.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_BCAST(BUFFER, COUNT, DATATYPE, ROOT, COMM, IERROR)
    <type> BUFFER(*)  
    INTEGER COUNT, DATATYPE, ROOT, COMM, IERROR
```

## Remarks

The type signature as specified by the *count* and *datatype* parameters on each process must be equal to the type signature at the root. This requirement implies that the amount of data sent must be equal to the amount received, pair-wise between each process and the root. **MPI\_Bcast** and all other data-movement collective routines make this restriction. Distinct type maps between sender and receiver are still allowed.

If the *comm* parameter references an intracommunicator, the **MPI\_Bcast** function broadcasts a message from the specified process to all processes of the group that includes itself. It is called by all members of the group that are using the same parameters. On return, the content of root buffer is copied to all the other processes.

If the *comm* parameter references an intercommunicator, then the call involves all processes in the intercommunicator, but with one group, group A, that defines the root process. All processes in the other group, group B, set the same value in *root* parameter, that is, the rank of the root process in group A. The root process sets the value **MPI\_ROOT** in the *root* parameter. All other processes in group A set the value **MPI\_PROC\_NULL** in the *root* parameter. Data is broadcast from the root process to all processes in group B. The *buffer* parameters of the processes in group B must be consistent with the *buffer* parameter of the root process.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Collective Functions](mpi-collective-functions.md)
</dt> <dt>

[**MPI\_Datatype**](mpi-datatype.md)
</dt> </dl>

 

 




