---
Description: 'A job contains one or more tasks to run on nodes in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'acca6d4e-f552-4a91-bc65-fdb5a5e12341'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Submitting a Job to the Scheduling Queue
---

# Submitting a Job to the Scheduling Queue

A job contains one or more tasks to run on nodes in the cluster. To create a job, call the [**ICluster::CreateJob**](icluster-createjob.md), [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md), or [**ICluster::CreateJobFromXmlFile**](icluster-createjobfromxmlfile.md) method.

After creating an [**IJob**](ijob.md) instance, specify the terms of the job. The terms specify the required resources for your job (for example, computers with a minimum of two processors).

If you create the job from XML, the XML will typically specify the required resources and contain all the tasks to run. If the XML does not specify the necessary resources or tasks, use the [**IJob**](ijob.md) instance to update the terms or add new tasks.

To create a task that you add to the job, call the [**ICluster::CreateTask**](icluster-createtask.md), [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md), or [**ICluster::CreateTaskFromXmlFile**](icluster-createtaskfromxmlfile.md) method. At a minimum, you must specify the command to run. If the task requires specific resources or is dependent on other tasks, set those terms, too. To add the task to the job, call the [**IJob::AddTask**](ijob-addtask.md) method.

After you have defined the job and added all the tasks to the job, call the [**ICluster::QueueJob**](icluster-addjob.md) method to add the job to the scheduling queue. The scheduler will then schedule your job to run based on the required resources and job priority. To add multiple jobs at one time to the scheduling queue, you can call the [**ICluster::QueueJobs**](icluster-queuejobs.md) method.

The following example shows how to use the **AddJob** and **SubmitJob** methods to add a job to the queue.


```CSharp
            IJob job = cluster.CreateJob();
            ITask task = cluster.CreateTask();

            // Set the appropriate job terms for your use. If the default
            // terms are appropriate and you do not want to set a display
            // name for your job, you only need to create the job instance.
            job.Name = "My Job";
            job.Priority = JobPriority.BelowNormal;

            // Add the job to the cluster. You can define and add the tasks 
            // to the job before or after you add the job to the cluster.
            // In this example, the tasks are added after the job is added
            // to the cluster.
            int jobId = cluster.AddJob(job);

            // Specify the command to run. Also specify paths for stdout and
            // stderr if you want to capture the output.
            task.CommandLine = "<COMMANDGOESHERE>";
            task.Stdout = "<STDOUTFILEGOESHERE>";
            task.Stderr = "<STDERRFILEGOESHERE>";

            // Add the task to the job.
            int taskId = cluster.AddTask(jobId, task);

            // Add the job to the scheduling queue.
            cluster.SubmitJob(jobId, null, null, true, 0);
```



The following example shows how to create a job, specify its terms, add a task to the job, and add the job to the scheduling queue.


```C++
HRESULT hr = S_OK;
IJob* pJob = NULL;
ITask* pTask = NULL;
long JobId = 0;

// Get an instance of the Job object.
hr = pCluster->CreateJob(&amp;pJob);
if (SUCCEEDED(hr))
{
  // Name the job. If you do not specify a name, the service generates a 
  // name by concatenating the name of the user that submitted the job
  // with the time that the job was submitted.
  hr = pJob->put_Name(_bstr_t(L"Job 1"));

  // Change any default job term values that are not appropriate for 
  // your job.
  hr = pJob->put_Priority(JobPriority_BelowNormal);

  // Get an instance of the Task object.
  hr = pCluster->CreateTask(&amp;pTask);
  if (SUCCEEDED(hr))
  {
    // You must specify a command (including arguments) to run. If the 
    // path contains long names, use quotation marks around the path. If you do 
    // not set IJob->put_AskedNodes or ITask->put_RequiredNodes, the 
    // command to run must exist on all nodes in the cluster.
    hr = pTask->put_CommandLine(_bstr_t(L"dir %windir%\\system32\\setup"));

    // If the command generates output that you want to capture, you must
    // specify the path for standard output and standard error. The path
    // to the file must exist on the node on which the task runs.
    hr = pTask->put_Stdout(_bstr_t(L"c:\\tmp\\myoutput.txt"));

    // Add the task to the job.
    hr = pJob->AddTask(pTask);

    // Add the job to the scheduling queue.
    hr = pCluster->QueueJob(pJob, _bstr_t(L"domain\\username"), NULL, VARIANT_TRUE, 0, &amp;JobId); 
    if (FAILED(hr))
    {
      BSTR bstrMessage;

      wprintf(L"pCluster->QueueJob failed.\n");
      hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
      wprintf(L"%s\n", bstrMessage);
      SysFreeString(bstrMessage);
    }
    else
    {
      wprintf(L"Added job %d to the scheduling queue.\n", JobId);
    }

    pTask->Release();
  }
  else
  {
    wprintf(L"pCluster->CreateJob failed.\n");
  }

  pJob->Release();
}
else
{
  wprintf(L"pCluster->CreateJob failed.\n");
}
```



The following example shows how to build the job collection that you pass to [**QueueJobs**](icluster-queuejobs.md). The example assumes that the `pCluster` variable points to a valid [**ICluster**](icluster.md) instance and that the `pJob1` and `pJob2` variables point to valid [**IJob**](ijob.md) instances that contain one or more tasks.


```C++
  HRESULT hr = S_OK;
  IClusterEnumerable* pJobs = NULL;
  IClusterEnumerable* pJobIds = NULL;

  hr = pCluster->CreateClusterEnumerable(&amp;pJobs);
  if (FAILED(hr))
  {
    wprintf(L"pCluster->CreateClusterEnumerable failed.\n");
    return NULL;
  }

  if (AddJobToCollection(pJobs, pJob1))
  {
    if (AddJobToCollection(pJobs, pJob2))
    {
      // Add the jobs to the scheduling queue. If the service fails to 
      // add one of the jobs, none of the jobs are added to the queue.
      hr = pCluster->QueueJobs(pJobs, _bstr_t(L"domain\\username"), NULL, VARIANT_TRUE, 0, &amp;pJobIds); 
      if (FAILED(hr))
      {
        BSTR bstrMessage;

        wprintf(L"pCluster->QueueJobs failed.\n");
        hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
        wprintf(L"%s\n", bstrMessage);
        SysFreeString(bstrMessage);
      }
      else
      {
        // Do something with the job IDs.

        pJobIds->Release();
      }
    }
  }

  pJobs->Release();
  pJob1->Release();
  pJob2->Release();


BOOL AddJobToCollection(IClusterEnumerable* pJobs, IJob* pJob)
{
  IDispatch* pdisp = NULL;
  VARIANT vJob;
  BOOL fSuccess = TRUE;

  pJob->QueryInterface(IID_IDispatch, reinterpret_cast<void **> (&amp;pdisp));  

  VariantInit(&amp;vJob);
  vJob.vt = VT_DISPATCH;
  vJob.pdispVal = pdisp;

  hr = pJobs->Add(vJob);
  if (FAILED(hr))
  {
    wprintf(L"pJobs->Add failed.\n");
    fSuccess = FALSE;
  }

  VariantClear(&amp;vJob);
  return fSuccess;
}
```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



