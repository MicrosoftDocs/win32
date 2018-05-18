---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1e25a15b-cc5a-4584-b130-29b742c84753'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Type\_get\_contents function'
---

# MPI\_Type\_get\_contents function

TBD

## Syntax


```C++
int MPIAPI MPI_Type_get_contents(
   MPI_Datatype                          datatype,
   int                                   max_integers,
   int                                   max_addresses,
   int                                   max_datatypes,
   _Out_cap_(max_integers) int           array_of_integers[],
   _Out_cap_(max_addresses) MPI_Aint     array_of_addresses[],
   _Out_cap_(max_datatypes) MPI_Datatype array_of_datatypes[]
);
```



## Parameters

<dl> <dt>

*datatype* 
</dt> <dd>

TBD

</dd> <dt>

*max\_integers* 
</dt> <dd>

TBD

</dd> <dt>

*max\_addresses* 
</dt> <dd>

TBD

</dd> <dt>

*max\_datatypes* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_integers* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_addresses* 
</dt> <dd>

TBD

</dd> <dt>

*array\_of\_datatypes* 
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_TYPE_GET_CONTENTS(DATATYPE, MAX_INTEGERS, MAX_ADDRESSES, MAX_DATATYPES,
            ARRAY_OF_INTEGERS, ARRAY_OF_ADDRESSES, ARRAY_OF_DATATYPES, IERROR)
    INTEGER DATATYPE, MAX_INTEGERS, MAX_ADDRESSES, MAX_DATATYPES,
    ARRAY_OF_INTEGERS(*), ARRAY_OF_DATATYPES(*), IERROR
    INTEGER(KIND=MPI_ADDRESS_KIND) ARRAY_OF_ADDRESSES(*)
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
</dt> </dl>

 

 




