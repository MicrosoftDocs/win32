---
Description: 'This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the MPI\_Comm\_get\_attr function.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f428b242-2f49-4d01-abf5-12af7e5a487c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Attr\_get function'
---

# MPI\_Attr\_get function

This function is deprecated in MPI-2 and removed from MPI-3. It is replaced by the [**MPI\_Comm\_get\_attr**](mpi-comm-get-attr.md) function.

## Syntax


```C++
int
MPIAPI MPI_Attr_get(
        MPI_Comm comm,
        int      keyval,
  _Out_ void     *attribute_val,
  _Out_ int      *flag
);
```



## Parameters

<dl> <dt>

*comm* 
</dt> <dd>

TBD

</dd> <dt>

*keyval* 
</dt> <dd>

TBD

</dd> <dt>

*attribute\_val* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*flag* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_ATTR_GET(COMM, KEYVAL, ATTRIBUTE_VAL, FLAG, IERROR)
    INTEGER COMM, KEYVAL, ATTRIBUTE_VAL, IERROR
    LOGICAL FLAG
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

[**MPI\_Comm\_get\_attr**](mpi-comm-get-attr.md)
</dt> </dl>

 

 




