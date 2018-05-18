---
Description: 'You can use the following methods to get a list of jobs that have been added to the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '45df11b3-dd90-4cfb-902d-28a8ebf9211f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Listing Jobs
---

# Listing Jobs

You can use the following methods to get a list of jobs that have been added to the cluster.



| Method                                                      | Description                                                                                                                                                                                              |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICluster::ListAllJobs**](icluster-listalljobs.md)       | Lists all jobs that have been added to the cluster.                                                                                                                                                      |
| [**ICluster::ListJobs**](icluster-listjobs.md)             | Lists all jobs for a specified user and status. For example, this method can list all failed jobs submitted by Joe. If you do not specify a user, the method returns all jobs with the specified status. |
| [**ICluster::ListJobsOnNode**](icluster-listjobsonnode.md) | Lists all jobs that are running on the specified node.                                                                                                                                                   |



 

The following C++ example shows how to call the [**ListJobs**](icluster-listjobs.md) method.


```C++
WCHAR *JobStatusStrings[] = { L"NotSubmitted", L"Queued", 
                              L"Running", L"Finished",
                              L"Failed", L"Canceled"
                            };

WCHAR *JobPriorityStrings[] = { L"Lowest", L"BelowNormal", 
                                L"Normal", L"AboveNormal",
                                L"Highest"
                              };


// List the jobs for the specified user and job status. To list all jobs 
// with a specified status, set pUserName to NULL.
void ListJobsForUser(ICluster* pCluster, LPWSTR pUserName, JobStatus QueryJobStatus)
{
  HRESULT hr = S_OK;
  IClusterEnumerable* pJobCollection = NULL;
  IEnumVARIANT* pJobs = NULL;
  IJob* pJob = NULL;
  VARIANT var;


  // Get the list of jobs based on the input.
  hr = pCluster->ListJobs(_bstr_t(pUserName), QueryJobStatus, &amp;pJobCollection);
  if (FAILED(hr))
  {
    BSTR bstrMessage;
    wprintf(L"pCluster->ListJobs failed.\n");
    hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
    wprintf(L"%s\n", bstrMessage);
    SysFreeString(bstrMessage);
    return;
  }

  // Get the enumerator used to loop through the collection.
  hr = pJobCollection->GetEnumerator(&amp;pJobs);
  if (SUCCEEDED(hr))
  {
    VariantInit(&amp;var);

    while (hr = pJobs->Next(1, &amp;var, NULL) == S_OK)
    {
      // The variant contains the IDispatch pointer to the job.
      // Query the IDispatch interface for the IJob interface.
       var.pdispVal->QueryInterface(IID_IJob, reinterpret_cast<void **> (&amp;pJob));

      PrintJobProperties(pJob);

      pJob->Release();
      pJob = NULL;

      VariantClear(&amp;var);
    }

    pJobs->Release();
  }
  else
  {
    wprintf(L"pJobCollection->GetEnumerator failed.\n");
  }

  pJobCollection->Release();

  return;
}


// Print some of the properties of the job.
void PrintJobProperties(IJob* pJob)
{
  HRESULT hr = S_OK;
  BSTR bstrJobName = NULL;
  VARIANT_BOOL fUntilCanceled = VARIANT_FALSE;
  JobStatus Status;
  JobPriority Priority;
  DATE EndDate;
  long id = 0;
  SYSTEMTIME SystemTime;
  WCHAR szDateString[30+1];
  WCHAR szTimeString[30+1];


  hr = pJob->get_Name(&amp;bstrJobName);
  if (FAILED(hr))
  {
    wprintf(L"pJob->get_Name failed.\n");
    goto cleanup;
  }

  hr = pJob->get_Id(&amp;id);
  if (FAILED(hr))
  {
    wprintf(L"pJob->get_Id failed.\n");
    goto cleanup;
  }

  hr = pJob->get_Status(&amp;Status);
  if (FAILED(hr))
  {
    wprintf(L"pJob->get_Status failed.\n");
    goto cleanup;
  }

  hr = pJob->get_RunUntilCanceled(&amp;fUntilCanceled);
  if (FAILED(hr))
  {
    wprintf(L"pJob->get_RunUntilCanceled failed.\n");
    goto cleanup;
  }

  hr = pJob->get_EndTime(&amp;EndDate);
  if (FAILED(hr))
  {
    wprintf(L"pJob->get_EndTime failed.\n");
    goto cleanup;
  }

  hr = pJob->get_Priority(&amp;Priority);
  if (FAILED(hr))
  {
    wprintf(L"pJob->get_EndTime failed.\n");
    goto cleanup;
  }

  wprintf(L"\nName: %s\n", bstrJobName);
  wprintf(L"ID: %ld\n", id);
  wprintf(L"Status: %s\n", JobStatusStrings[Status]);
  wprintf(L"Priority: %s\n", JobPriorityStrings[Priority]);
  wprintf(L"RunUntilCanceled: %s\n", (fUntilCanceled) ? L"TRUE" : L"FALSE");

  if (VariantTimeToSystemTime(EndDate, &amp;SystemTime))
  {
    GetDateFormat(NULL, 0, &amp;SystemTime, NULL, &amp;(szDateString[0]), sizeof(szDateString));
    GetTimeFormat(NULL, 0, &amp;SystemTime, NULL, &amp;(szTimeString[0]), sizeof(szTimeString));
    wprintf(L"End date: %s %s\n", szDateString, szTimeString);
  }

  wprintf(L"Extended terms:\n");
  PrintExtendedJobTerms(pJob);

cleanup:

  SysFreeString(bstrJobName);
}


// Print the extended job terms, if specified.
void PrintExtendedJobTerms(IJob* pJob)
{
  HRESULT hr = S_OK;
  INameValueCollection* pTermsCollection = NULL;
  IEnumVARIANT* pTerms = NULL;
  INameValue* pTerm = NULL;
  VARIANT var;
  BSTR bstrName = NULL;
  BSTR bstrValue = NULL;


  // Get the collection of extended job terms.
  hr = pJob->get_ExtendedJobTerms(&amp;pTermsCollection);
  if (FAILED(hr))
  {
    wprintf(L"pJob->get_ExtendedJobTerms failed.\n");
    return;
  }

  // Get the enumerator used to loop through the collection.
  hr = pTermsCollection->GetEnumerator(&amp;pTerms);
  if (SUCCEEDED(hr))
  {
    VariantInit(&amp;var);

    while (hr = pTerms->Next(1, &amp;var, NULL) == S_OK)
    {
      // The variant contains the IDispatch pointer to the term.
      // Query the IDispatch interface for the INameValue interface.
      var.pdispVal->QueryInterface(IID_INameValue, reinterpret_cast<void **> (&amp;pTerm));

      hr = pTerm->get_Name(&amp;bstrName);  // Term name
      if (SUCCEEDED(hr))
      {
        wprintf(L"\tName: %s\n", bstrName);
        SysFreeString(bstrName);

        hr = pTerm->get_Value(&amp;bstrValue);  // Term Value
        if (SUCCEEDED(hr))
        {
          wprintf(L"\tValue: %s\n\n", bstrValue);
          SysFreeString(bstrName);
        }
        else
        {
          wprintf(L"pTerm->get_Value failed.\n");
        }
      }
      else
      {
        wprintf(L"pTerm->get_Name failed.\n");
      }

      pTerm->Release();
      pTerm = NULL;

      VariantClear(&amp;var);
    }

    pTerms->Release();
  }
  else
  {
    wprintf(L"pTermsCollection->GetEnumerator failed.\n");
  }

  pTermsCollection->Release();

  return;
}
```



The following C# example shows how to call the [**ListAllJobs**](icluster-listalljobs.md) method.


```CSharp
            // List each job in the cluster.
            foreach (IJob job in cluster.ListAllJobs())
            {
                Console.WriteLine(job.Name);

                // Uses the job object to enumerate the tasks in the job.
                Console.WriteLine("\tUsing job object to enumerate tasks...");
                foreach (ITask task in job)
                {
                    if (string.IsNullOrEmpty(task.Name))
                        Console.WriteLine("\t" + task.Id);
                    else
                        Console.WriteLine("\t" + task.Id);
                }

                // Uses the Cluster.ListTasks method to enumerate the tasks in the job.
                Console.WriteLine("\n\tUsing cluster object to enumerate tasks...");
                foreach (ITask task in cluster.ListTasks(job.Id))
                {
                    if (string.IsNullOrEmpty(task.Name))
                        Console.WriteLine("\t" + task.Id);
                    else
                        Console.WriteLine("\t" + task.Id);
                }

                Console.WriteLine();
            }
```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



