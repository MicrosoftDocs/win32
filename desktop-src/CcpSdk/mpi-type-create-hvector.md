---
Description: 'Defines a new data type that consists of a specified number of blocks. Each block is a concatenation of the same number of elements of an existing data type.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '66f3fd82-d20c-4ac0-a5e1-ab54115df59f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_create\_hvector function'
---

# MPI\_Type\_create\_hvector function

Defines a new data type that consists of a specified number of blocks. Each block is a concatenation of the same number of elements of an existing data type. This function is similar to the function [**MPI\_Type\_vector**](mpi-type-vector.md) except that the stride is specified in bytes instead of the number of elements.

## Syntax


```C++
int MPIAPI MPI_Type_create_hvector(
        int          count,
        int          blocklength,
        MPI_Aint     stride,
        MPI_Datatype oldtype,
  _Out_ MPI_Datatype *newtype
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of blocks in the new data type.

</dd> <dt>

*blocklength* 
</dt> <dd>

The number of elements in each block.

</dd> <dt>

*stride* 
</dt> <dd>

The number of bytes between the start of one block and the next. The stride is a multiple of the **extent** of the old data type.

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
MPI_TYPE_CREATE_HVECTOR(COUNT, BLOCKLENGTH, STRIDE, OLDTYPE, NEWTYPE, IERROR)
    INTEGER COUNT, BLOCKLENGTH, STRIDE, OLDTYPE, NEWTYPE, IERROR
```

## Remarks

This function replaces the [**MPI\_Type\_hvector**](mpi-type-hvector.md) function, which is deprecated.

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

[**MPI\_Type\_contiguous**](mpi-type-contiguous.md)
</dt> <dt>

[**MPI\_Type\_vector**](mpi-type-vector.md)
</dt> </dl>

 

 




