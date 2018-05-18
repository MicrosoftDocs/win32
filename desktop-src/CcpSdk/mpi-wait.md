---
Description: 'Completes an outstanding operation.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '516ab401-2b6b-45db-9815-34d75b9c4c3b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Wait function'
---

# MPI\_Wait function

Completes an outstanding operation.

## Syntax


```C++
int MPIAPI MPI_Wait(
  _Inout_ MPI_Request *request,
  _Out_   MPI_Status  *status
);
```



## Parameters

<dl> <dt>

*request* \[in, out\]
</dt> <dd>

A pointer to the **MPI\_Request** handle of an outstanding operation.

</dd> <dt>

*status* \[out\]
</dt> <dd>

A pointer to an [**MPI\_Status**](mpi-status.md) object that describes the specified request.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_WAIT(REQUEST, STATUS, IERROR)
    INTEGER REQUEST, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

This function is a non-local operation. Successful completion might depend on matching operations at other processes.

This function returns when the operation that is identified by the *request* parameter is completed.

If the operation that is associated with this request was a persistent communication operation, the persistent request is marked as inactive. Other operations are deallocated, and the request handle is set to **MPI\_REQUEST\_NULL**.

If the *request* parameter points to a value of **MPI\_REQUEST\_NULL** or to an inactive persistent communication request, then the function returns an empty status.

## Requirements



|                    |                                                                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2012 MS-MPI Redistributable Package, HPC Pack 2008 R2 MS-MPI Redistributable Package, HPC Pack 2008 MS-MPI Redistributable Package or HPC Pack 2008 Client Utilities<br/> |
| Header<br/>  | <dl> <dt>Mpi.h; </dt> <dt>Mpif.h</dt> </dl>                                           |
| Library<br/> | <dl> <dt>Msmpi.lib</dt> </dl>                                                                                                     |
| DLL<br/>     | <dl> <dt>Msmpi.dll</dt> </dl>                                                                                                     |



## See also

<dl> <dt>

[MPI Point to Point Functions](mpi-point-to-point-functions.md)
</dt> <dt>

[**MPI\_Isend**](mpi-isend.md)
</dt> <dt>

[**MPI\_Ibsend**](mpi-ibsend.md)
</dt> </dl>

 

 




