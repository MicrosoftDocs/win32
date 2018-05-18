---
Description: 'Extracts a subset a group of processes for the purpose of separate Multiple Instruction Multiple Data (MIMD) computation in a separate communicator.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bb028396-e3d5-4e2c-908f-bfe70cd86ca5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm\_create function'
---

# MPI\_Comm\_create function

Extracts a subset a group of processes for the purpose of separate Multiple Instruction Multiple Data (MIMD) computation in a separate communicator.

## Syntax


```C++
int MPIAPI MPI_Comm_create(
        MPI_Comm  comm,
        MPI_Group group,
  _Out_ MPI_Comm  *newcomm
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

The source communicator.

</dd> <dt>

*group* 
</dt> <dd>

The group that defines the requested subset of the processes in the source communicator.

</dd> <dt>

*newcomm* \[out\]
</dt> <dd>

On return, contains a handle to a new communicator.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_COMM_CREATE(COMM,GROUP,NEWCOMM,IERROR)
    INTEGER COMM, GROUP, NEWCOMM, IERROR
```

## Remarks

The communicator that this function creates can be further subdivided into parallel subcomputations by using the **MPI\_Comm\_create** function or other communicator constructors. The [**MPI\_Comm\_split**](mpi-comm-split.md) function is a more general function to create [**MPI\_Comm**](mpi-comm.md) objects.

If the *comm* parameter references an intracommunicator, this function returns a new communicator with a communication group as defined by the *group* parameter. No cached information propagates from the source communicator to the new communicator. Each process must call with a *group* parameter that is a subgroup of the group that is associated with the source communicator. A possible value is **MPI\_GROUP\_EMPTY**. The processes can specify different values for the *group* parameter. If a process calls with a non-empty group, then all processes in that group must call the function with the same values for the *group* parameter, that is, the same members in the same order. Otherwise, the function returns an error. This result implies that the set of groups that are specified across the processes must be disjoint. If the calling process is a member of the group that is specified in the *group* parameter, then the *newcomm* parameter represents a communicator with the specified group as its associated group. If a process specifies a group to which it does not belong, for example, **MPI\_GROUP\_EMPTY**, then the *newcomm* parameter returns **MPI\_COMM\_NULL**.

The interface supports the original mechanism from MPI-1.1, which required the same group in all processes of comm. It was extended in MPI-2.2 to enable the use of disjoint subgroups to enable implementations to eliminate unnecessary communication that the [**MPI\_Comm\_split**](mpi-comm-split.md) function would incur when the user already knows the membership of the disjoint subgroups.

The **MPI\_Comm\_create** function is collective and must be called by all processes in the group of the source communicator. The requirement that the entire group participate in the call comes from the following issues:

-   It allows the implementation to layer the **MPI\_Comm\_create** function on top of regular collective communications.
-   It provides additional safety, in particular in the case where partially overlapping groups are used to create new communicators.
-   It permits implementations to avoid some of the communication that is related to context creation.

If the *comm* parameter references an intercommunicator, then the created communicator is also an intercommunicator where the local group consists only of those processes that are specified in the *group* parameter. Specify only those processes in the local group of the input intercommunicator that are to be a part of the new communicator in the *group* parameter. All processes in the same local group of the communicator must specify the same value for the *group* parameter, that is, the same members in the same order. If either group does not specify at least one process in the local group of the intercommunicator, or if the calling process is not included in the group, an error is returned.

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

[**MPI\_Comm\_split**](mpi-comm-split.md)
</dt> </dl>

 

 




