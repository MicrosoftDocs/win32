---
Description: 'Retrieves the job-related error message or job cancellation message.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '81d89d94-d19c-4c60-bcca-becd2d35820b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ErrorMessage property'
---

# ISchedulerJob::ErrorMessage property

Retrieves the job-related error message or job cancellation message.

This property is read-only.

## Syntax


```C++
HRESULT get_ErrorMessage(
  [out] BSTR *pErrorMessage
);
```



## Property value

The message.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The message contains the last message that was set for the job. The message can be a run-time error message or the message passed to the [**IScheduler::CancelJob**](ischeduler-canceljob.md) method.

Check the message if the job state is Failed or Canceled or if a job's method call fails.

For possible HPC-defined errors, see the fields defined for the [ErrorCode](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.errorcode.aspx) class.

## Examples

The following example shows how to access the error message. The SubmitJob method call fails with 80040621 because a task in the job does not specify a command line.


```C++
    _bstr_t message;

    hr = pScheduler->SubmitJob(pJob, NULL, NULL);
    if (FAILED(hr))
    {
        wprintf(L"pScheduler->SubmitJob failed with 0x%x.\n", hr);

        // Have to call Refresh to update the job object with the message.
        hr = pJob->Refresh();
        if (FAILED(hr))
        {
            wprintf(L"pJob->Refresh failed with 0x%x.\n", hr);
            goto cleanup;
        }

        hr = pJob->get_ErrorMessage(&amp;message.GetBSTR());
        if (FAILED(hr))
        {
            wprintf(L"pJob->get_ErrorMessage failed with 0x%x.\n", hr);
        }

        wprintf(L"%s\n", message.GetBSTR());

        goto cleanup;
    }
```



## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerTask.ErrorMessage**](ischedulertask-errormessage.md)
</dt> </dl>

 

 




