---
Description: 'Defines a new data type that consists of a specified number of blocks. Each block is the same block length, but each block can have a different block displacement.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c093ef03-d22e-43cb-b5aa-641d53705fc9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_create\_indexed\_block function'
---

# MPI\_Type\_create\_indexed\_block function

Defines a new data type that consists of a specified number of blocks. Each block is the same block length, but each block can have a different block displacement.

## Syntax


```C++
int MPIAPI MPI_Type_create_indexed_block(
        int                   count,
        int                   blocklength,
        _In_count_(count) int array_of_displacements[],
        MPI_Datatype          oldtype,
  _Out_ MPI_Datatype          *newtype
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of blocks and the number of entries in the *array\_of\_displacements* parameter.

</dd> <dt>

*blocklength* 
</dt> <dd>

The number of elements in each block.

</dd> <dt>

*array\_of\_displacements* 
</dt> <dd>

The displacement of each individual block in bytes. All block displacements must be a multiple of the **extent** of the data type as specified in the *oldtype* parameter.

</dd> <dt>

*oldtype* 
</dt> <dd>

The MPI data type of each element.

</dd> <dt>

*newtype* \[out\]
</dt> <dd>

On return, contains an [**MPI\_Datatype**](mpi-datatype.md) handle that represents the new data type.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_TYPE_CREATE_INDEXED_BLOCK(COUNT, BLOCKLENGTH, ARRAY_OF_DISPLACEMENTS, OLDTYPE, NEWTYPE, IERROR)
    COUNT, BLOCKLENGTH, ARRAY_OF_DISPLACEMENTS, OLDTYPE, NEWTYPE, IERROR
```

## Remarks

This function is similar to the function [**MPI\_Type\_indexed**](mpi-type-indexed.md) except that all the blocks have the same length.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Datatype Functions](mpi-datatype-functions.md)
</dt> <dt>

[**MPI\_Type\_indexed**](mpi-type-indexed.md)
</dt> </dl>

 

 




