---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f7909375-f67e-4339-9cce-7373813ab4bf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Info\_get function'
---

# MPI\_Info\_get function

TBD

## Syntax


```C++
int MPIAPI MPI_Info_get(
        MPI_Info                   info,
  _In_  char                       *key,
        int                        valuelen,
        _Out_z_cap_(valuelen) char *value,
  _Out_ int                        *flag
);
```



## Parameters

<dl> <dt>

*info* 
</dt> <dd>

TBD

</dd> <dt>

*key* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*valuelen* 
</dt> <dd>

TBD

</dd> <dt>

*value* 
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
MPI_INFO_GET(INFO, KEY, VALUELEN, VALUE, FLAG, IERROR)
    INTEGER INFO, VALUELEN, IERROR
    CHARACTER*(*) KEY, VALUE
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

[MPI Info Object Functions](mpi-info-object-functions.md)
</dt> </dl>

 

 




