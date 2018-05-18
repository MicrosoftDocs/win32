---
Description: 'A command is a single task that you want to execute on every node in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b6c472f8-ca59-4579-95e0-c2ba6140e4d8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Executing a Command Synchronously
---

# Executing a Command Synchronously

A command is a single task that you want to execute on every node in the cluster. The command is not scheduled like a job but is executed immediately. The task must contain the [command line](itask-put-commandline.md) to execute. To limit the nodes on which the command runs, call the [**ITask::put\_RequiredNodes**](itask-put-requirednodes.md) method. You may also set the following task properties (other task properties are ignored if set):

-   [**ITask::put\_Stdin**](itask-put-stdin.md)
-   [**ITask::put\_WorkDirectory**](itask-put-workdirectory.md)
-   [**ITask::SetEnvironmentVariable**](itask-setenvironmentvariable.md)

To execute the command, call either the [**ICluster::ExecuteCommand**](icluster-executecommand.md) or [**ICluster::ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md) method. If you expect the command to generate a large volume of output and you want to be able to page through the output, consider using **ExecuteCommandWithPaging**.

The [**ExecuteCommand**](icluster-executecommand.md) method waits until the results from all nodes are returned.

The following example shows how to execute a command synchronously.


```C++
  ITask* pTask = NULL;
  IClusterEnumerable* pResultsCollection = NULL;
  long CommandId = 0;

  // Get an instance of the Task object.
  hr = pCluster->CreateTask(&amp;pTask);
  if (SUCCEEDED(hr))
  {
    // Add the command to execute to the task.
    hr = pTask->put_CommandLine(_bstr_t(L"dir %windir%\\system32\\setup"));
    if (SUCCEEDED(hr))
    {
      hr = pCluster->GetNewCommandId(&amp;CommandId);
      if (SUCCEEDED(hr))
      {
        hr = pCluster->ExecuteCommand(CommandId, 
                                  pTask, 
                                  _bstr_t(L"domain\\username"), 
                                  NULL, 
                                  VARIANT_TRUE, 
                                  0, 
                                  &amp;pResultsCollection);

        if (SUCCEEDED(hr))
        {
          ListCommandResults(pResultsCollection);
          pResultsCollection->Release();
        }
        else
        {
          BSTR bstrMessage = NULL;
 
          wprintf(L"pCluster->ExecuteCommand failed.\n");
          hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
          wprintf(L"%s\n", bstrMessage);
          SysFreeString(bstrMessage);
        }
      }
    }
  
    pTask->Release();
  }

// List the results of executing the command from each node.
void ListCommandResults(IClusterEnumerable* pCollection)
{
  HRESULT hr = S_OK;
  IEnumVARIANT* pResults = NULL;   
  IExecutionResult* pResult = NULL; 
  VARIANT var;
  long ExitCode = 0;
  BSTR bstrNodeName = NULL;
  BSTR bstrOutput = NULL;

  // Get the collection's enumerator used to enumerate
  // the items of the collection.
  hr = pCollection->GetEnumerator(&amp;pResults);
  if (FAILED(hr))
  {
    wprintf(L"pCollection->GetEnumerator failed.\n");
    goto cleanup;
  }

  VariantInit(&amp;var);

  // Enumerate each item in the collection
  while (hr = pResults->Next(1, &amp;var, NULL) == S_OK)
  {
    // The variant contains the IDispatch pointer to the result.
    // Query the IDispatch interface for the IExecutionResult interface.
    var.pdispVal->QueryInterface(IID_IExecutionResult, reinterpret_cast<void **> (&amp;pResult));

    // Retrieve the node name, exit code and output from the result.
    hr = pResult->get_NodeName(&amp;bstrNodeName);
    if (SUCCEEDED(hr))
    {
      wprintf(L"Node: %s\n", bstrNodeName);
      SysFreeString(bstrNodeName);

      hr = pResult->get_ExitCode(&amp;ExitCode);
      if (SUCCEEDED(hr))
      {
        wprintf(L"Exit code: %d\n", ExitCode);
      }

      hr = pResult->get_Output(&amp;bstrOutput);
      if (SUCCEEDED(hr))
      {
        wprintf(L"Output: %s\n", bstrOutput);
        SysFreeString(bstrOutput);
      }
      else
      {
        wprintf(L"Output: Unable to retrieve output.\n");
      }
    }
    else
    {
      wprintf(L"Node: Unable to retrieve node name from result.\n");
    }

    pResult->Release();
    pResult = NULL;

    VariantClear(&amp;var);
  }

cleanup:

  if (pResults)
    pResults->Release();

  return;
}
```




```CSharp
ITask task;
IClusterEnumerable executionResults;

task = cluster.CreateTask();
task.CommandLine = @"dir %windir%\system32\setup";

try
{
    executionResults = cluster.ExecuteCommandWithPaging(cluster.GetNewCommandId(),
        task,
        null,
        null,
        true,
        0,
        2048);

        Console.WriteLine("\nCommand: " + task.CommandLine);

        foreach (IExecutionResult result in executionResults)
        {
            string output;

            Console.WriteLine("\nOutput from " + result.NodeName + "\n");
            while ((output = cluster.ReadExecutionResult(result)) != string.Empty)
            {
                Console.Write(output);
            }
        }
}
catch (Exception e)
{
    Console.WriteLine("\nExecuteCommandWithPaging failed.\n" + e.Message);
}
```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



