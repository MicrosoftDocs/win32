---
Description: 'Defines a new data type that is a concatenation of a number of elements of an existing data type.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f2fb753c-3f17-4308-a384-8edd8c18bacf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_contiguous function'
---

# MPI\_Type\_contiguous function

Defines a new data type that is a concatenation of a number of elements of an existing data type.

## Syntax


```C++
int MPIAPI MPI_Type_contiguous(
        int          count,
        MPI_Datatype oldtype,
  _Out_ MPI_Datatype *newtype
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

The number of elements in the new data type.

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
MPI_TYPE_CONTIGUOUS(COUNT, OLDTYPE, NEWTYPE, IERROR)
    INTEGER COUNT, OLDTYPE, NEWTYPE, IERROR
```

## Remarks

The concatenation of the new data type is defined by using the extent of the old data type as the size of the concatenated copies.

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

[**MPI\_Type\_vector**](mpi-type-vector.md)
</dt> <dt>

[**MPI\_Type\_create\_hvector**](mpi-type-create-hvector.md)
</dt> </dl>

 

 




