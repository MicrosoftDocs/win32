---
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c1a39d12-063f-4f1c-b64b-6010fe6d9cc7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Reporting Features in Windows HPC Server 2008 R2
---

# Reporting Features in Windows HPC Server 2008 R2

Windows HPC Server 2008 R2 provides the following items that you can use to get information about jobs, nodes, and metrics for custom reports:

-   SQL Views

-   HPC cmdlets for the Windows PowerShell command-line interface

> [!Note]  
> The data that Windows HPC Server 2008 R2 provides through these two sources is not updated in real time and is subject to some latency. For Windows HPC Server 2008 R2, the HPC Reporting Service collects data every 15 minutes when the service is running, so the latency can be up to 15 minutes.

 

## SQL Views

The main source of data that Windows HPC Server 2008 R2 provides for creating custom reports consists of a set of views in the HPCReporting SQL database for the HPC cluster. These views contain information about the jobs that have run on the cluster, the nodes and node groups in the cluster, changes in the state of the nodes, and the allocation of jobs to the nodes.

For reference information about each of the SQL views in the HPCReporting SQL database, see [Reporting Views](reporting-views.md).

## HPC cmdlets

Windows HPC Server 2008 R2 provides cmdlets that you can use to get data for custom reports and to view and set configuration properties for the reporting database.

The following table lists the cmdlets that you can use to get data for custom reports.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Cmdlet</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Get-HpcJobHistory](http://go.microsoft.com/fwlink/p/?linkid=179946)<br/></td>
<td>Gets the job history data for all finished, canceled, and failed jobs for the specified time period. You can export this information to a database, and then create and run reports about the information.<br/> Includes <em>StartDate</em> and <em>EndDate</em> parameters that you can use to specify the period of time for which you want to get job history data. Specifically, [Get-HpcJobHistory](http://go.microsoft.com/fwlink/p/?linkid=179946) gets job history data for jobs where the EventTime value for the job is between <em>StartDate</em> and <em>EndDate</em>.<br/>
<blockquote>
<p>[!Note]</p>
<p>The data that this command retrieves is similar to the data in the [<strong>JobHistoryView</strong>](jobhistoryview.md) in the HPCReporting database.<br/></p>
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[Get-HpcNodeStateHistory](http://go.microsoft.com/fwlink/p/?linkid=179944)<br/></td>
<td>Retrieves the history of changes to the state of the nodes in the HPC cluster for the specified time period. These changes include the addition and removal of nodes, and changes of the node state to Online, Offline, Reachable, or Unreachable.<br/> Includes <em>StartDate</em> and <em>EndDate</em> parameters that you can use to specify the period of time for which you want to get node state data.<br/>
<blockquote>
<p>[!Note]</p>
<p>The data that this command retrieves is similar to the data in the [<strong>NodeEventHistoryView</strong>](nodeeventhistoryview.md) in the HPCReporting database.<br/></p>
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[Get-HpcMetricValueHistory](http://go.microsoft.com/fwlink/p/?linkid=179947)<br/></td>
<td>Gets the historical values of the specified metrics that HPC Cluster Manager uses in the heat maps for the nodes and the monitoring charts.<br/> Includes <em>StartDate</em> and <em>EndDate</em> parameters that you can use to specify the period of time for which you want to get metric values, a <em>MetricName</em> parameter that you can use to specify the metrics for which you want to get values, a <em>Counter</em> parameter that you can use to specify the counters for which you want to get values, and <em>Node</em> and <em>NodeName</em> parameters that you can use to specify the nodes for which you want to get metric values. A single metric can contain multiple counters. The <em>StartDate</em> and <em>EndDate</em> parameters are required, and the other parameters are optional.<br/>
<blockquote>
<p>[!Note]</p>
<p>This cmdlet does not correspond to a view in the HPCReporting database.<br/></p>
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

> [!Note]
>
> If you run the HPC cmdlets on a computer that only has the Windows HPC Server 2008 R2 client components installed and is not a member of an HPC cluster, include the *Scheduler* parameter in the cmdlet to specific the head node of the HPC cluster for which you want to get information.

 

### Configuration parameters for the reporting database

You can use configuration parameters to view or change if and how long the reporting database stores information about jobs and nodes for reporting. You can view the values of the parameters with the [Get-HPCClusterProperty](http://go.microsoft.com/fwlink/p/?linkid=179948) cmdlet and set the values with the [Set-HpcClusterProperty](http://go.microsoft.com/fwlink/p/?linkid=152322) cmdlet. The following table lists the configuration parameters that are available in Windows HPC Server 2008 R2.



| Parameter                           | Description                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AllocationHistoryTtl<br/>     | Specifies the number of days that the HPCReporting database should store information about the allocation of jobs to nodes. This parameter has a default value of 5.<br/>                                                                                                                                                                                                  |
| DataExtensibilityEnabled<br/> | Specifies whether the cluster stores information for custom reporting about jobs, nodes, and the allocation of jobs to nodes.<br/> True indicates that the cluster stores information for custom reporting about jobs, nodes, and the allocation of jobs to nodes. False indicates that the cluster does not store this information. The default value is True.<br/> |
| DataExtensibilityTtl<br/>     | Specifies the number of days that the HPCReporting database should store all of the information about jobs and nodes except for the allocation of jobs to nodes. This parameter has a default value of 365.<br/>                                                                                                                                                           |
| ReportingDBSize<br/>          | Contains the current size of the reporting database. This value is a string that includes the units of measurement for the size. This parameter is read-only.<br/>                                                                                                                                                                                                         |



 

To view the current value of a configuration parameter, run the following cmdlet:

**Get-HpcClusterProperty -Parameter -Name** *Parameter\_Name*

To change the value of a configuration parameter, run the following cmdlet:

**Set-HpcClusterProperty -***Parameter\_Name* *New\_Value*

> [!Note]
>
> You cannot use the [Set-HpcClusterProperty](http://go.microsoft.com/fwlink/p/?linkid=152322) cmdlet to change the value of the ReportingDBSize configuration parameter.

 

 

 




