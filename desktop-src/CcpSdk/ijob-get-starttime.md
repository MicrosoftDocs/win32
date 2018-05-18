---
Description: 'Retrieves the time that the job started running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fed57b9e-8aad-4fe8-b42f-15bb664882df'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_StartTime method'
---

# IJob::get\_StartTime method

Retrieves the time that the job started running.

## Syntax


```C++
HRESULT get_StartTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The time that the job started running.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example that shows how to print a date, see [Listing Jobs](listing-jobs.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_CreateTime**](ijob-get-createtime.md)
</dt> <dt>

[**IJob::get\_EndTime**](ijob-get-endtime.md)
</dt> </dl>

 

 




