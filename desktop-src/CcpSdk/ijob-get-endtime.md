---
Description: 'Retrieves the job end time.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c7834154-771d-4008-bae0-1253d09490cf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_EndTime method'
---

# IJob::get\_EndTime method

Retrieves the job end time.

## Syntax


```C++
HRESULT get_EndTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The job end time.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The end time indicates when the job finished, failed, or was canceled. The value is MaxValue if the job has not finished, failed, or been canceled. The time is reset if you requeue a failed or canceled job.

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

[**IJob::get\_StartTime**](ijob-get-starttime.md)
</dt> </dl>

 

 




