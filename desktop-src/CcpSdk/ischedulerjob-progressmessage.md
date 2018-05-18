---
Description: 'Gets or sets a custom status message for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '09A70A44-4E88-4FCA-96FC-32D02B6B2F91'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ProgressMessage property'
---

# ISchedulerJob::ProgressMessage property

Gets or sets a custom status message for the job.

This property is read/write.

## Syntax


```C++
HRESULT put_ProgressMessage(
  [in]          BSTR pRetVal
);

HRESULT get_ProgressMessage(
  [out, retval] BSTR *pRetVal
);
```



## Property value

A string that specifies the custom status message. The maximum length of the message is 80 characters.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

You can set the value of this property for jobs in any state.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::Progress**](ischedulerjob-progress.md)
</dt> </dl>

 

 




