---
Description: 'Allows replication of an old datatype into a sequence of blocks (each block is a concatenation of the old datatype), where all blocks have the same block length but can have different block displacements in bytes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ED5D334D-FE5E-4259-A679-82B38C750873'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_create\_hindexed\_block function'
---

# MPI\_Type\_create\_hindexed\_block function

Allows replication of an old datatype into a sequence of blocks (each block is a concatenation of the old datatype), where all blocks have the same block length but can have different block displacements in bytes.

## Syntax


```C++
int MPIAPI MPI_Type_create_hindexed_block(
  _In_  int          count,
  _In_  int          blocklength,
  _In_  MPI_Aint     array_of_displacements[],
  _In_  MPI_Datatype oldtype,
  _Out_ MPI_Datatype *newtype
);
```



## Parameters

<dl> <dt>

*count* \[in\]
</dt> <dd>

The number of blocks and the number of entries in the *array\_of\_displacements* parameter.

</dd> <dt>

*blocklength* \[in\]
</dt> <dd>

The number of elements in each block.

</dd> <dt>

*array\_of\_displacements* \[in\]
</dt> <dd>

The array containing the displacement of each block, in bytes.

</dd> <dt>

*oldtype* \[in\]
</dt> <dd>

The [**MPI\_Datatype**](mpi-datatype.md) handle representing the data type of each element.

</dd> <dt>

*newtype* \[out\]
</dt> <dd>

On return, contains the [**MPI\_Datatype**](mpi-datatype.md) handle representing a data type containing *count* copies of element blocks. Each block has *blocklength* elements. The displacement of each block is specified in *array\_of\_displacements*.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_TYPE_CREATE_HINDEXED_BLOCK(COUNT, BLOCKLENGTH, ARRAY_OF_DISPLACEMENTS, OLDTYPE, NEWTYPE, IERROR)
    INTEGER COUNT, BLOCKLENGTH, OLDTYPE, NEWTYPE, IERROR
INTEGER(KIND=MPI_ADDRESS_KIND) ARRAY_OF_DISPLACEMENTS(*)
```

## Remarks

This function is similar to the function [**MPI\_Type\_create\_indexed\_block**](mpi-type-create-indexed-block.md) except that the array of displacements contains the displacement of each block in bytes.

## Requirements



|                    |                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Microsoft MPI v6<br/>                                                                                                                    |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl> |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                           |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                           |



## See also

<dl> <dt>

[MPI Datatype Functions](mpi-datatype-functions.md)
</dt> <dt>

[**MPI\_Type\_create\_indexed\_block**](mpi-type-create-indexed-block.md)
</dt> </dl>

 

 




