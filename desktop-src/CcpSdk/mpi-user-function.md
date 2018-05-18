---
Description: 'MPI\_User\_function is a placeholder for the application-defined function name.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '81f4f323-be56-4546-b589-9f1a0aae1515'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_User\_function function'
---

# MPI\_User\_function function

**MPI\_User\_function** is a placeholder for the application-defined function name.

## Syntax


```C++
void MPI_User_function(
       _In_count_   invec,
       _Inout_ void *inoutvec,
  _In_ int          *len,
  _In_ MPI_Datatype *datatype
);
```



## Parameters

<dl> <dt>

*invec* 
</dt> <dd>

TBD

</dd> <dt>

*inoutvec* 
</dt> <dd>

TBD

</dd> <dt>

*len* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*datatype* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
SUBROUTINE USER_FUNCTION(INVEC, INOUTVEC, LEN, DATATYPE)
    <type> INVEC(LEN), INOUTVEC(LEN)
    INTEGER LEN, DATATYPE
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

[MPI Collective Functions](mpi-collective-functions.md)
</dt> <dt>

[**MPI\_Op\_create**](mpi-op-create.md)
</dt> </dl>

 

 




