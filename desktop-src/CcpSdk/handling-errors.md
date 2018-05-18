---
Description: 'If you are writing a C++ application, the COM interoperability layer translates the exceptions thrown by the Compute Cluster Pack (CCP) to HRESULT values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bd6cdcb0-a727-4f2b-951f-37f66c5b2e49'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Handling Errors
---

# Handling Errors

If you are writing a C++ application, the COM interoperability layer translates the exceptions thrown by the Compute Cluster Pack (CCP) to HRESULT values. The CCP-specific HRESULT values are not documented. Instead of testing for specific HRESULT values, test only for success or failure.

If an error occurs, you can use the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md), [**IJob::get\_ErrorMessage**](ijob-get-errormessage.md), and [**ITask::get\_ErrorMessage**](itask-get-errormessage.md) methods to get a description of the error. When the status of a job or task is Failed, the error message contains the description of the run-time error that occurred.

The following C++ example shows how to get the description when an error occurs.


```C++
hr = pCluster->SubmitJobs(pJobIds, 
                          _bstr_t(L"domain\\username"), 
                          NULL, 
                          VARIANT_TRUE, 
                          0); 
if (FAILED(hr))
{
  BSTR bstrMessage = NULL;
 
  wprintf(L"pCluster->SubmitJobs failed.\n");
  hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
  wprintf(L"%s\n", bstrMessage);
  SysFreeString(bstrMessage);
}
```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



