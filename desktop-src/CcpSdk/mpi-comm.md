---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '41201F26-5B85-49AB-A138-46CC9864B180'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Comm enumeration'
---

# MPI\_Comm enumeration

TBD

## Syntax


```C++
typedef enum _MPI_Comm { 
  MPI_COMM_NULL   = 0x04000000,
  MPI_COMM_WORLD  = 0x44000000,
  MPI_COMM_SELF   = 0x44000001
} MPI_Comm;
```



## Constants

<dl> <dt>

<span id="MPI_COMM_NULL"></span><span id="mpi_comm_null"></span>**MPI\_COMM\_NULL**
</dt> <dd>

TBD

</dd> <dt>

<span id="MPI_COMM_WORLD"></span><span id="mpi_comm_world"></span>**MPI\_COMM\_WORLD**
</dt> <dd>

TBD

</dd> <dt>

<span id="MPI_COMM_SELF"></span><span id="mpi_comm_self"></span>**MPI\_COMM\_SELF**
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |



## See also

<dl> <dt>

[MPI Enumerations](mpi-enumerations.md)
</dt> </dl>

 

 




