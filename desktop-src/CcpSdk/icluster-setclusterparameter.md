---
Description: 'Sets a configuration parameter for the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f7b54741-cf49-468e-9002-52afa987f1f7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::SetClusterParameter method'
---

# ICluster::SetClusterParameter method

Sets a configuration parameter for the cluster.

## Syntax


```C++
HRESULT SetClusterParameter(
  [in] BSTR Name,
  [in] BSTR Value
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the parameter. The names are case-insensitive.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The value of the parameter.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Only a user with administrator privileges can set the cluster's configuration parameters. The following are the supported configuration parameters.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ActivationFilterProgram</td>
<td>The absolute path to an application that determines whether a job should be run. This application is run for each job before the job is started. This application returns 0 if the job should be started and a nonzero value otherwise. It must accept a single command-line argument, which is an absolute path to an XML file that specifies the terms of the job. The job terms are an attribute of the [<strong>Job</strong>](schema-job-element.md) element. The [<strong>ExtendedTerms</strong>](schema-extendedterms-job-element.md) element contains the name/value pairs for application-defined extended job terms. For more information, see [Job Schema](schema-job-schema.md).</td>
</tr>
<tr class="even">
<td>ActivationFilterTimeout</td>
<td>Time-out value for the activation filter, in seconds. By default, the filter must complete in 15 seconds.</td>
</tr>
<tr class="odd">
<td>BackfillLookahead</td>
<td>Number of jobs that the scheduler searches to find jobs that can [backfill](ijob-get-isbackfill.md) the jobs at the top of the queue. The following lists the possible values.<br/>
<ul>
<li>If less than zero, search the entire job queue.</li>
<li>If zero, do not backfill jobs.</li>
<li>If greater than zero, the value is the number of jobs to search.</li>
</ul>
The default is –1.<br/></td>
</tr>
<tr class="even">
<td>EventLogLevel</td>
<td>Sets the error log level. The log level can be one of the following values:<br/>
<ul>
<li>Off</li>
<li>Critical</li>
<li>Error</li>
<li>Warning</li>
<li>Information</li>
<li>Verbose</li>
<li>ActivityTracing</li>
<li>All</li>
</ul>
For a description of these values see the [SourceLevels](https://msdn.microsoft.com/library/system.diagnostics.sourcelevels.aspx) enumeration in the [System.Diagnostics](https://msdn.microsoft.com/library/system.diagnostics.aspx) namespace.<br/></td>
</tr>
<tr class="odd">
<td>HeartbeatInterval</td>
<td>Interval for the scheduler to attempt to contact the node. The default interval is 60 seconds.</td>
</tr>
<tr class="even">
<td>InactivityCount</td>
<td>Number of times the scheduler must attempt to contact a node before it can declare the node unreachable. The default number is 3.</td>
</tr>
<tr class="odd">
<td>JobRetryCount</td>
<td>Maximum number of times the system will rerun a job when a system error occurs (not when a job error occurs). The default number is 3. The job's status is set to Failed when the count is reached.</td>
</tr>
<tr class="even">
<td>JobRuntime</td>
<td>Default run time for any job if not specified on the job. If not set on the job, the default is Infinite. The format is dd:hh:mm or &quot;Infinite&quot;. If the run time of the job exceeds this limit, the job is terminated and its status is set to failed.</td>
</tr>
<tr class="odd">
<td>SpoolDir</td>
<td>An absolute path to the folder that will spool the output from the task run by [<strong>ICluster::ExecuteCommand</strong>](icluster-executecommand.md).</td>
</tr>
<tr class="even">
<td>SubmissionFilterProgram</td>
<td>The absolute path to an application that determines whether a job should be submitted to the queue. This application is run for each job before the job is added to the scheduling queue. This application returns 0 if the job should be submitted and a nonzero value otherwise. It must accept a single command-line argument, which is an absolute path to an XML file that specifies the terms of the job. The job terms are an attribute of the Job element. The ExtendedTerms element contains the name/value pairs for application-defined extended job terms. For more information, see [Job Schema](schema-job-schema.md).</td>
</tr>
<tr class="odd">
<td>SubmissionFilterTimeout</td>
<td>Time-out value for the submission filter, in seconds. By default, the filter must complete in 15 seconds.</td>
</tr>
<tr class="even">
<td>TaskRetryCount</td>
<td>Maximum number of times the system will rerun a task when a system error occurs (not when a task error occurs). The default number is 3. The task's status is set to Failed when the count is reached.</td>
</tr>
<tr class="odd">
<td>TTLCompletedJobs</td>
<td>The minimum number of days that a completed job will be kept. A completed job is a job whose status is finished, canceled, or failed. The default interval is five days; this is the recommended minimum.</td>
</tr>
</tbody>
</table>



 

You can update CCP configuration parameters only; you cannot delete CCP parameters. The method validates the value for CCP parameters and fails if the value is out-of-range.

If you specify a parameter name that is not in the list, the method adds the parameter to the cluster. The cluster does not use the user-defined parameter but it is available for others to use. You can delete or update user-defined parameters. To delete user-defined parameters, set the *Value* parameter to **NULL** or an empty string. (Note that setting a CCP-defined parameter to an empty string will not delete the parameter.)

To retrieve the current configuration values, call the [**ICluster::get\_Parameters**](icluster-get-parameters.md) method.

The filter programs can be configured alternatively using the following registry keys:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CCPSchedSvc\Enum
   ActivationFilterProgram
   ActivationFilterTimeout
```

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CCPSchedSvc\Enum
   SubmissionFilterProgram
   SubmissionFilterTimeout
```

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::get\_Parameters**](icluster-get-parameters.md)
</dt> </dl>

 

 




