---
Description: 'This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the MPI\_Get\_address function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '068bd9d3-206d-4246-9b6f-144a1fcdbf26'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Address function'
---

# MPI\_Address function

This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the [**MPI\_Get\_address**](mpi-get-address.md) function.

## Syntax


```C++
int
MPIAPI MPI_Address(
  _In_  void     *location,
  _Out_ MPI_Aint *address
);
```



## Parameters

<dl> <dt>

*location* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*address* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_ADDRESS(LOCATION, ADDRESS, IERROR)
    <type> LOCATION(*)
    INTEGER IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) ADDRESS
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

[**MPI\_Get\_address**](mpi-get-address.md)
</dt> </dl>

 

 




