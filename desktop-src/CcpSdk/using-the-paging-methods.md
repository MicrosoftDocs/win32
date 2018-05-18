---
Description: 'The ICluster interface contains several methods that let you page through the output that the method generates.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7a17eafd-daef-4bea-8c47-46907954ecc3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Using the Paging Methods
---

# Using the Paging Methods

The [**ICluster**](icluster.md) interface contains several methods that let you page through the output that the method generates. These methods are useful if the method might generate a large volume of output and you want to present the data in a user interface as it is generated, instead of waiting until all the data is returned.

The following [**ICluster**](icluster.md) methods provide paging:

-   [**ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md)
-   [**ListAllJobsWithPaging**](icluster-listalljobswithpaging.md)
-   [**ListJobsWithPaging**](icluster-listjobswithpaging.md)
-   [**ListTasksWithPaging**](icluster-listtaskswithpaging.md)
-   [**WaitForCommandWithPaging**](icluster-waitforcommandwithpaging.md)

The paging methods are meant to be called in a loop. The first call takes a snapshot of the output and returns the first page of the output. For [**ListAllJobsWithPaging**](icluster-listalljobswithpaging.md), [**ListJobsWithPaging**](icluster-listjobswithpaging.md), and [**ListTasksWithPaging**](icluster-listtaskswithpaging.md), be sure to set the *Timestamp* and *Version* parameters to **NULL** on the first call and do not change their values on subsequent calls. The loop ends when the enumerable object is empty.

To reset the enumerable object to the beginning, set *Timestamp* to **NULL** and leave the *Version* value unchanged.

For the methods that list jobs and tasks, you can set *Version* to **NULL** and leave the *Timestamp* value unchanged to get jobs or tasks that were added or whose state has changed since the last snapshot.

The following example shows how to use the [**ListAllJobsWithPaging**](icluster-listalljobswithpaging.md) method to list all jobs in the cluster.


```C++
#define PAGE_SIZE 500  // Number of jobs to return in each page

long g_JobCount = 0;  // Counts the total number of jobs returned

  ListAllJobsInCluster(pCluster, PAGE_SIZE);
  wprintf(L"Total number of jobs, %d\n", g_JobCount);


// List all jobs in the cluster. Use the specified page size to 
// page through the results.
void ListAllJobsInCluster(ICluster* pCluster, long PageSize)
{
  HRESULT hr = S_OK;
  IClusterEnumerable* pJobsCollection = NULL;
  IEnumVARIANT* pJobs = NULL;
  VARIANT vTimestamp;
  VARIANT vVersion;
  BOOL fMoreJobs = TRUE;

  VariantInit(&amp;vTimestamp);
  VariantInit(&amp;vVersion);

  while (fMoreJobs)
  {
    hr = pCluster->ListAllJobsWithPaging(VARIANT_FALSE, &amp;vTimestamp, &amp;vVersion, PageSize, &amp;pJobsCollection);
    if (FAILED(hr))
    {
      wprintf(L"pCluster->ListAllJobs failed.\n");
      goto cleanup;
    }

    hr = pJobsCollection->GetEnumerator(&amp;pJobs);
    if (SUCCEEDED(hr))
    {
      fMoreJobs = ProcessJobs(pJobs);
      pJobs->Release();
      pJobs = NULL;

      pJobsCollection->Release();
      pJobsCollection = NULL;
    }
    else
    {
      wprintf(L"pJobsCollection->GetEnumerator failed.\n");
      goto cleanup;
    }
  }

cleanup:

  if (pJobsCollection)
    pJobsCollection->Release();

  VariantClear(&amp;vTimestamp);
  VariantClear(&amp;vVersion);

  return;
}


// Process each job in the collection.
BOOL ProcessJobs(IEnumVARIANT* pJobs)
{
  HRESULT hr = S_OK;
  IJob* pJob = NULL;
  VARIANT var;
  long count = 0;

  VariantInit(&amp;var);

  while (hr = pJobs->Next(1, &amp;var, NULL) == S_OK)
  {
    count++;  // Used to determine whether the collection is empty.

    var.pdispVal->QueryInterface(IID_IJob, reinterpret_cast<void **> (&amp;pJob));

    // Do something with the job.

    pJob->Release();
    pJob = NULL;

    VariantClear(&amp;var);
  }

  g_JobCount += count;  // Add to global total job count

  return (count) ? TRUE : FALSE;  // If FALSE, all pages returned
}
```




```CSharp
            // Set pageSize to an appropriate value for your use. The value
            // indicates the number of jobs to return with each page.
            int pageSize = 100; 
            bool hasJobs = true;
            object timestamp = null;
            object version = null;

            while (hasJobs)
            {
                hasJobs = false;

                foreach (IJob job in cluster.ListAllJobsWithPaging(false, ref timestamp, ref version, pageSize))
                {
                    Console.WriteLine(job.Name);

                    foreach (ITask task in job)
                    {
                        if (string.IsNullOrEmpty(task.Name))
                            Console.WriteLine("\t" + task.Id);
                        else
                            Console.WriteLine("\t" + task.Id);
                    }

                    hasJobs = true;
                }

                Console.WriteLine();
            }
```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



