---
Description: 'This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the MPI\_Type\_create\_struct function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '73fbdd24-782c-41a4-b277-fa3aee6cbb79'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_struct function'
---

# MPI\_Type\_struct function

This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the [**MPI\_Type\_create\_struct**](mpi-type-create-struct.md) function.

## Syntax


```C++
int
MPIAPI MPI_Type_struct(
   int        count,
   _In_count_ newtype
);
```



## Parameters

<dl> <dt>

*count* 
</dt> <dd>

TBD

</dd> <dt>

*newtype* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_TYPE_STRUCT(COUNT, ARRAY_OF_BLOCKLENGTHS,
            ARRAY_OF_DISPLACEMENTS, ARRAY_OF_TYPES, NEWTYPE, IERROR)
    INTEGER COUNT, ARRAY_OF_BLOCKLENGTHS(*), ARRAY_OF_TYPES(*), NEWTYPE,
    IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) ARRAY_OF_DISPLACEMENTS(*)
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

[**MPI\_Type\_create\_struct**](mpi-type-create-struct.md)
</dt> </dl>

 

 




