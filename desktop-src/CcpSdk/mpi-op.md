---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3C70A7BA-E67A-434F-BF13-F42F498B8150'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Op enumeration'
---

# MPI\_Op enumeration

TBD

## Syntax


```C++
typedef enum _MPI_Op { 
  MPI_OP_NULL  = 0x18000000,
  MPI_MAX      = 0x58000001,
  MPI_MIN      = 0x58000003,
  MPI_SUM      = 0x58000003,
  MPI_PROD     = 0x58000004,
  MPI_LAND     = 0x58000005,
  MPI_BAND     = 0x58000006,
  MPI_LOR      = 0x58000007,
  MPI_BOR      = 0x58000008,
  MPI_LXOR     = 0x58000009,
  MPI_BXOR     = 0x5800000a,
  MPI_MINLOC   = 0x5800000b,
  MPI_MAXLOC   = 0x5800000c,
  MPI_REPLACE  = 0x5800000d
} MPI_Op;
```



## Constants

<dl> <dt>

<span id="MPI_OP_NULL"></span><span id="mpi_op_null"></span>**MPI\_OP\_NULL**
</dt> <dd></dd> <dt>

<span id="MPI_MAX"></span><span id="mpi_max"></span>**MPI\_MAX**
</dt> <dd></dd> <dt>

<span id="MPI_MIN"></span><span id="mpi_min"></span>**MPI\_MIN**
</dt> <dd></dd> <dt>

<span id="MPI_SUM"></span><span id="mpi_sum"></span>**MPI\_SUM**
</dt> <dd></dd> <dt>

<span id="MPI_PROD"></span><span id="mpi_prod"></span>**MPI\_PROD**
</dt> <dd></dd> <dt>

<span id="MPI_LAND"></span><span id="mpi_land"></span>**MPI\_LAND**
</dt> <dd></dd> <dt>

<span id="MPI_BAND"></span><span id="mpi_band"></span>**MPI\_BAND**
</dt> <dd></dd> <dt>

<span id="MPI_LOR"></span><span id="mpi_lor"></span>**MPI\_LOR**
</dt> <dd></dd> <dt>

<span id="MPI_BOR"></span><span id="mpi_bor"></span>**MPI\_BOR**
</dt> <dd></dd> <dt>

<span id="MPI_LXOR"></span><span id="mpi_lxor"></span>**MPI\_LXOR**
</dt> <dd></dd> <dt>

<span id="MPI_BXOR"></span><span id="mpi_bxor"></span>**MPI\_BXOR**
</dt> <dd></dd> <dt>

<span id="MPI_MINLOC"></span><span id="mpi_minloc"></span>**MPI\_MINLOC**
</dt> <dd></dd> <dt>

<span id="MPI_MAXLOC"></span><span id="mpi_maxloc"></span>**MPI\_MAXLOC**
</dt> <dd></dd> <dt>

<span id="MPI_REPLACE"></span><span id="mpi_replace"></span>**MPI\_REPLACE**
</dt> <dd></dd> </dl>

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |



## See also

<dl> <dt>

[MPI Enumerations](mpi-enumerations.md)
</dt> </dl>

 

 




