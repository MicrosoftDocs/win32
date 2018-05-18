---
Description: 'Retrieves the job creation time.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'aea3d0ff-f9c7-4222-9b84-cf16ba281dfc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_CreateTime method'
---

# IJob::get\_CreateTime method

Retrieves the job creation time.

## Syntax


```C++
HRESULT get_CreateTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The job creation time.

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

[**IJob::get\_EndTime**](ijob-get-endtime.md)
</dt> <dt>

[**IJob::get\_StartTime**](ijob-get-starttime.md)
</dt> </dl>

 

 




