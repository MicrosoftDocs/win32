---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd3982ec6-a490-4c6b-b1ff-01fb9b458e12'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPIR\_Dup\_fn function'
---

# MPIR\_Dup\_fn function

TBD

## Syntax


```C++
int MPIAPI MPIR_Dup_fn(
           MPI_Comm oldcomm,
           int      keyval,
  _In_opt_ void     *extra_state,
  _In_     void     *attribute_val_in,
  _Out_    void     *attribute_val_out,
  _Out_    int      *flag
);
```



## Parameters

<dl> <dt>

*oldcomm* 
</dt> <dd>

TBD

</dd> <dt>

*keyval* 
</dt> <dd>

TBD

</dd> <dt>

*extra\_state* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*attribute\_val\_in* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*attribute\_val\_out* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*flag* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Miscellaneous Functions](mpi-miscellaneous-functions.md)
</dt> </dl>

 

 




