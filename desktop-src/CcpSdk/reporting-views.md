---
Description: 'The HPCReporting SQL database that Windows HPC Server 2008 R2 provides contains several views that you can query to obtain data for custom reports. This section provides reference information about those SQL views.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b1d01e3e-791d-41b5-b21f-80b56563b1de'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Reporting Views
---

# Reporting Views

The HPCReporting SQL database that Windows HPC Server 2008 R2 provides contains several views that you can query to obtain data for custom reports. This section provides reference information about those SQL views.



| View name                                                             | Description                                                                                                                                                                                            |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocationHistoryView**](allocationhistoryview.md)<br/>     | Lists the allocations of tasks or subtasks in high-performance computing (HPC) jobs to cores on the nodes in the HPC cluster.<br/>                                                               |
| [**DailyNodeStatView**](dailynodestatview.md)<br/>             | Provides statistics about the availability and use of nodes to run jobs on a daily basis. Contains one row per combination of node and date.<br/>                                                |
| [**JobHistoryView**](jobhistoryview.md)<br/>                   | Lists each queued instance of a job on an HPC cluster that finished, failed, or was canceled. Includes statistics and information about the properties and results, and tasks for the jobs.<br/> |
| [**NodeEventHistoryView**](nodeeventhistoryview.md)<br/>       | Lists the events that occurred on the nodes of an HPC cluster. Events include the addition or removal of nodes and changes to the node state.<br/>                                               |
| [**NodeGroupMembershipView**](nodegroupmembershipview.md)<br/> | Indicates the node groups to which the nodes in an HPC cluster belong. Contains one row for each combination of node and node group for which the node is a member of the node group.<br/>       |
| [**NodeGroupView**](nodegroupview.md)<br/>                     | Lists the node groups for the HPC cluster.<br/>                                                                                                                                                  |
| [**NodeView**](nodeview.md)<br/>                               | Lists the nodes in an HPC cluster.<br/>                                                                                                                                                          |



 

 

 




