---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3c505756-3c1a-4284-b611-5bdda552819d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Register\_datarep function'
---

# MPI\_Register\_datarep function

TBD

## Syntax


```C++
int MPIAPI MPI_Register_datarep(
  _In_     char                            *datarep,
  _In_opt_ MPI_Datarep_conversion_function *read_conversion_fn,
  _In_opt_ MPI_Datarep_conversion_function *write_conversion_fn,
  _In_     MPI_Datarep_extent_function     *dtype_file_extent_fn,
  _In_opt_ void                            *extra_state
);
```



## Parameters

<dl> <dt>

*datarep* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*read\_conversion\_fn* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*write\_conversion\_fn* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*dtype\_file\_extent\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*extra\_state* \[in, optional\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

TBD

## Fortran

``` syntax
MPI_REGISTER_DATAREP(DATAREP, READ_CONVERSION_FN, WRITE_CONVERSION_FN,
            DTYPE_FILE_EXTENT_FN, EXTRA_STATE, IERROR)
    CHARACTER*(*) DATAREP
    EXTERNAL READ_CONVERSION_FN, WRITE_CONVERSION_FN, DTYPE_FILE_EXTENT_FN
    INTEGER(KIND=MPI_ADDRESS_KIND) EXTRA_STATE
    INTEGER IERROR
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

[MPI File Functions](mpi-file-functions.md)
</dt> <dt>

[**MPI\_Datarep\_conversion\_function**](mpi-datarep-conversion-function.md)
</dt> <dt>

[**MPI\_Datarep\_extent\_function**](mpi-datarep-extent-function.md)
</dt> </dl>

 

 




