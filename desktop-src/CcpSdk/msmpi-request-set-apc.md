---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dff831d6-4505-49fe-856e-05b9241682db'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MSMPI\_Request\_set\_apc function'
---

# MSMPI\_Request\_set\_apc function

TBD

## Syntax


```C++
int MPIAPI MSMPI_Request_set_apc(
       MPI_Request            request,
  _In_ MSMPI_Request_callback *callback_fn,
  _In_ MPI_Status             *callback_status
);
```



## Parameters

<dl> <dt>

*request* 
</dt> <dd>

TBD

</dd> <dt>

*callback\_fn* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*callback\_status* \[in\]
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
</dt> <dt>

[**MSMPI\_Request\_callback**](msmpi-request-callback.md)
</dt> </dl>

 

 




