---
Description: 'Retrieves or sets the user data associated with the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2e5f7b59-6ea6-4cfe-b756-96c17f194d1d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::UserBlob property'
---

# ISchedulerTask::UserBlob property

Retrieves or sets the user data associated with the task.

This property is read/write.

## Syntax


```C++
HRESULT put_UserBlob(
  [in]  BSTR data
);

HRESULT get_UserBlob(
  [out] BSTR *pData
);
```



## Property value

The user data associated with the task. The resulting encrypted data is limited to 8,000 bytes.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

HPC encrypts the user data when the job is added or submitted to the scheduler. Only the user that added or submitted the job can get the user data. Note that if the user specifies a different RunAs user when the job is submitted, the RunAs user will not be able to access the user data.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




