---
Description: 'Defines a new data type that consists of a specified number of blocks of a specified size.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1bb8716f-8dc1-4b3a-8f2b-5177c63db715'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_vector function'
---

# MPI\_Type\_vector function

Defines a new data type that consists of a specified number of blocks of a specified size. Each block is a concatenation of the same number of elements of an existing data type.

## Syntax


```C++
int MPIAPI MPI_Type_vector(
        int          count,
        int          blocklength,
        int          stride,
        MPI_Datatype oldtype,
  _Out_ MPI_Datatype *newtype
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of blocks in the created vector.

</dd> <dt>

*blocklength* 
</dt> <dd>

The number of elements in each block.

</dd> <dt>

*stride* 
</dt> <dd>

The number of elements between the start of one block and the start of the next block.

</dd> <dt>

*oldtype* 
</dt> <dd>

The data type of each element.

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
MPI_TYPE_VECTOR(COUNT, BLOCKLENGTH, STRIDE, OLDTYPE, NEWTYPE, IERROR)
    INTEGER COUNT, BLOCKLENGTH, STRIDE, OLDTYPE, NEWTYPE, IERROR
```

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

[**MPI\_Type\_create\_hvector**](mpi-type-create-hvector.md)
</dt> </dl>

 

 




