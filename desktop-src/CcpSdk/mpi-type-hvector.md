---
Description: 'This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the MPI\_Type\_create\_hvector function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '25ce3e68-95d3-4d83-ac36-16ed76c914dd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_hvector function'
---

# MPI\_Type\_hvector function

This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the [**MPI\_Type\_create\_hvector**](mpi-type-create-hvector.md) function.

## Syntax


```C++
int
MPIAPI MPI_Type_hvector(
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

TBD

</dd> <dt>

*blocklength* 
</dt> <dd>

TBD

</dd> <dt>

*stride* 
</dt> <dd>

TBD

</dd> <dt>

*oldtype* 
</dt> <dd>

TBD

</dd> <dt>

*newtype* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_TYPE_HVECTOR(COUNT, BLOCKLENGTH, STRIDE, OLDTYPE, NEWTYPE,
    IERROR)
    INTEGER COUNT, BLOCKLENGTH, OLDTYPE, NEWTYPE, IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) STRIDE
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

[MPI Miscellaneous Functions](mpi-miscellaneous-functions.md)
</dt> <dt>

[**MPI\_Type\_create\_hvector**](mpi-type-create-hvector.md)
</dt> </dl>

 

 




