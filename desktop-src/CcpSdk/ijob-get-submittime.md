---
Description: 'Retrieves the time that the job was submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2e8b2b66-e67b-4f84-af8e-507452147387'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_SubmitTime method'
---

# IJob::get\_SubmitTime method

Retrieves the time that the job was submitted.

## Syntax


```C++
HRESULT get_SubmitTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The time the job was submitted.

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
</dt> <dt>

[**IJob::get\_StartTime**](ijob-get-starttime.md)
</dt> </dl>

 

 




