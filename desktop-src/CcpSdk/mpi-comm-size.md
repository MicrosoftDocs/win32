---
Description: 'Retrieves the number of processes involved in a communicator, or the total number of processes available.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'de35aa91-5a27-41a7-9a26-ad0875c43390'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_size function'
---

# MPI\_Comm\_size function

Retrieves the number of processes involved in a communicator, or the total number of processes available.

## Syntax


```C++
int MPIAPI MPI_Comm_size(
        MPI_Comm comm,
  _Out_ int      *size
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

The communicator to evaluate. Specify the **MPI\_COMM\_WORLD** constant to retrieve the total number of processes available.

</dd> <dt>

*size* \[out\]
</dt> <dd>

On return, indicates the number of processes in the group for the communicator.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_COMM_SIZE(COMM,SIZE,IERROR)
    INTEGER COMM, SIZE, IERROR
```

## Remarks

This function enables the user to retrieve the group size with a single function call. Otherwise, it would be necessary to create a temporary group by using the [**MPI\_Comm\_group**](mpi-comm-group.md) function, get the size of the group by using the [**MPI\_Group\_size**](mpi-group-size.md) function, and then free the temporary group by using the [**MPI\_Group\_free**](mpi-group-free.md) function.

This function is often used with the [**MPI\_Comm\_rank**](mpi-comm-rank.md) function to determine the amount of concurrency that is available for a specific library or program. The **MPI\_Comm\_rank** function indicates the rank of the process that calls it in the range from 0 to *size*-1, where *size* is retrieved by using the **MPI\_Comm\_size** function.

> [!Note]  
> There is no standard way to change the number of processes after initialization has taken place.

 

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Communicator Functions](mpi-communicator-functions.md)
</dt> <dt>

[**MPI\_Comm\_rank**](mpi-comm-rank.md)
</dt> </dl>

 

 




