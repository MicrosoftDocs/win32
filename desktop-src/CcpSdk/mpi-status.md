---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'E7F73B45-7A00-4210-AAAC-0A3A4EE186B6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Status structure'
---

# MPI\_Status structure

TBD

## Syntax


```C++
typedef struct _MPI_Status {
  int count;
  int cancelled;
  int MPI_SOURCE;
  int MPI_TAG;
  int MPI_ERROR;
} MPI_Status, *PMPI_Status;
```



## Members

<dl> <dt>

**count**
</dt> <dd>

TBD

</dd> <dt>

**cancelled**
</dt> <dd></dd> <dt>

**MPI\_SOURCE**
</dt> <dd></dd> <dt>

**MPI\_TAG**
</dt> <dd></dd> <dt>

**MPI\_ERROR**
</dt> <dd></dd> </dl>

## Remarks

There are two defined **MPI\_Status** pointers that can be used in place of this structure, **MPI\_STATUS\_IGNORE** and **MPI\_STATUSES\_IGNORE**.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h</dt> </dl>                                                                                                         |



## See also

<dl> <dt>

[MPI Structs](mpi-structs.md)
</dt> </dl>

 

 




