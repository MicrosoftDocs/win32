---
Description: 'Tests an outstanding operation for completion.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a0f641d4-3764-43fe-969e-354a8857e5b5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'MPI\_Test function'
---

# MPI\_Test function

Tests an outstanding operation for completion.

## Syntax


```C++
int MPIAPI MPI_Test(
  _Inout_  MPI_Request *request,
  _Out_   int          *flag,
  _Out_   MPI_Status   *status
);
```



## Parameters

<dl> <dt>

*request* \[in, out\]
</dt> <dd>

A pointer to the **MPI\_Request** handle of an outstanding operation.

</dd> <dt>

*flag* \[out\]
</dt> <dd>

On return, contains a pointer to an integer that indicates whether the request is completed. A non-zero value indicates that the request is complete.

</dd> <dt>

*status* \[out\]
</dt> <dd>

On return, contains a pointer to an [**MPI\_Status**](mpi-status.md) object that describes the specified operation if it is complete.

</dd> </dl>

## Return value

Returns **MPI\_SUCCESS** on success. Otherwise, the return value is an error code.

In Fortran, the return value is stored in the *IERROR* parameter.

## Fortran

``` syntax
MPI_WAIT(REQUEST, FLAG, STATUS, IERROR)
    LOGICAL FLAG
    INTEGER REQUEST, STATUS(MPI_STATUS_SIZE), IERROR
```

## Remarks

This function is a local operation. Successful completion does not depend on any operations at other processes.

If the operation that is associated with this request was a persistent communication operation, the persistent request is marked as inactive. Other operations are deallocated, and the request handle is set to **MPI\_REQUEST\_NULL**.

If the *request* parameter points to a value of **MPI\_REQUEST\_NULL** or to an inactive persistent request, then the function returns with the *flag* parameter set to a non-zero value and with the *status* parameter empty.

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

[**MPI\_Wait**](mpi-wait.md)
</dt> <dt>

[**MPI\_Status**](mpi-status.md)
</dt> <dt>

[**MPI\_Testany**](mpi-testany.md)
</dt> <dt>

[**MPI\_Testall**](mpi-testall.md)
</dt> <dt>

[**MPI\_Testsome**](mpi-testsome.md)
</dt> </dl>

 

 




