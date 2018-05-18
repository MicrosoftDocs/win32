---
Description: 'Defines a new data type with a specified data type, displacement, and size for each block of data.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a6c7a1fd-66e2-4dc0-a306-966b6c04cc86'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_create\_struct function'
---

# MPI\_Type\_create\_struct function

Defines a new data type with a specified data type, displacement, and size for each block of data.

## Syntax


```C++
int MPIAPI MPI_Type_create_struct(
        int                            count,
        _In_count_(count) int          array_of_blocklengths[],
        _In_count_(count) MPI_Aint     array_of_displacements[],
        _In_count_(count) MPI_Datatype array_of_types[],
  _Out_ MPI_Datatype                   *newtype
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of blocks and the number of entries in the *array\_of\_blocklengths*, *array\_of\_displacements* and *array\_of\_types* parameters.

</dd> <dt>

*array\_of\_blocklengths* 
</dt> <dd>

The number of elements of each block.

</dd> <dt>

*array\_of\_displacements* 
</dt> <dd>

The displacement of each individual block in bytes.

</dd> <dt>

*array\_of\_types* 
</dt> <dd>

The data type of each individual block.

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
MPI_TYPE_CREATE_STRUCT(COUNT, ARRAY_OF_BLOCKLENGTHS, ARRAY_OF_DISPLACEMENTS, ARRAY_OF_TYPES, NEWTYPE, IERROR)
    COUNT, ARRAY_OF_BLOCKLENGTHS, ARRAY_OF_DISPLACEMENTS, ARRAY_OF_TYPES, NEWTYPE, IERROR
```

## Remarks

This function replaces the [**MPI\_Type\_struct**](mpi-type-struct.md) function, which is deprecated.

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
</dt> <dt>

[**MPI\_Type\_create\_hindexed**](mpi-type-create-hindexed.md)
</dt> <dt>

[**MPI\_Type\_create\_indexed\_block**](mpi-type-create-indexed-block.md)
</dt> </dl>

 

 




