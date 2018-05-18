---
Description: 'Defines a new data type that consists of an n-dimensional subarray of an n-dimensional array.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '27B8E756-94C6-43A9-ACDD-A583419C40A5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_create\_subarray function'
---

# MPI\_Type\_create\_subarray function

Defines a new data type that consists of an n-dimensional subarray of an n-dimensional array. The subarray can be located anywhere within the full array. It can be any nonzero size as long as it is fully contained within the array.

## Syntax


```C++
int MPIAPI MPI_Type_create_subarray(
        int                   ndims,
        _In_count_(ndims) int array_of_sizes[],
        _In_count_(ndims) int array_of_subsizes[],
        _In_count_(ndims) int array_of_starts[],
        int                   order,
        MPI_Datatype          oldtype,
  _Out_ MPI_Datatype          *newtype
);
```



## Parameters

<dl> <dt>

*ndims* 
</dt> <dd>

The number of array dimensions and the number of elements in the *array\_of\_sizes*, *array\_of\_subsizes* and *array\_of\_starts* parameters.

</dd> <dt>

*array\_of\_sizes* 
</dt> <dd>

The number of elements in each dimension of the full array.

</dd> <dt>

*array\_of\_subsizes* 
</dt> <dd>

The number of elements in each dimension of the subarray.

</dd> <dt>

*array\_of\_starts* 
</dt> <dd>

The starting index of the subarray in each dimension.

</dd> <dt>

*order* 
</dt> <dd>

The order of the dimensions.

<dt>

<span id="MPI_ORDER_C"></span><span id="mpi_order_c"></span>

<span id="MPI_ORDER_C"></span><span id="mpi_order_c"></span>**MPI\_ORDER\_C**


</dt> <dd>

The row-major order in which all the elements for a given row are stored contiguously.

</dd> <dt>

<span id="MPI_ORDER_FORTRAN"></span><span id="mpi_order_fortran"></span>

<span id="MPI_ORDER_FORTRAN"></span><span id="mpi_order_fortran"></span>**MPI\_ORDER\_FORTRAN**


</dt> <dd>

The column-major order in which all the elements for a given column are stored contiguously.

</dd> </dl>

> [!Note]  
> Both C and Fortran programs can use either order. The defined values reflect typical usage.

 

</dd> <dt>

*oldtype* 
</dt> <dd>

Specifies the data type of each element.

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
MPI_TYPE_CREATE_SUBARRAY(NDIMS, ARRAY_OF_SIZES, ARRAY_OF_SUBSIZES, ARRAY_OF_STARTS, ORDER, OLDTYPE, NEWTYPE, IERROR)
    NDIMS, ARRAY_OF_SIZES, ARRAY_OF_SUBSIZES, ARRAY_OF_STARTS, ORDER, OLDTYPE, NEWTYPE, IERROR
```

## Remarks

The function returns an error if the size of the subarray exceeds the size of the array. For each dimension *i*, the value of *array\_of\_subsizes\[i\]* parameter must be greater than or equal to one and less than or equal to the *array\_of\_sizes\[i\]* parameter.

The function returns an error if the subarray starts or ends outside the bounds of the array. For any dimension *i*, the value of parameter must be zero and the sum of the *array\_of\_starts\[i\]* and *array\_of\_subsizes\[i\]* parameters must be less than or equal to the value of the *array\_of\_sizes\[i\]* parameter. For example, if the subarray is the same size as the array, then the subarray must start at index zero. Arrays are assumed to be indexed starting from zero.

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
</dt> </dl>

 

 




