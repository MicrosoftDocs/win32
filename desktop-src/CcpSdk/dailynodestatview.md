---
Description: 'Provides statistics about the availability and use of nodes to run jobs on a daily basis. Contains one row per combination of node and date.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '48b398e6-b4bb-4c34-ae1b-dddb27a5dc53'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: DailyNodeStatView
---

# DailyNodeStatView

Provides statistics about the availability and use of nodes to run jobs on a daily basis. Contains one row per combination of node and date.



| Column name                  | Data type                | Can be null   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------|--------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NodeName<br/>          | nvarchar(64)<br/>  | No<br/> | The name of the node for which the statistics apply.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Date<br/>              | smalldatetime<br/> | No<br/> | The day for which the statistics apply. The time portion of this datetime value is set to midnight, but the statistics apply to the whole day. The day extends from midnight of the specified date through midnight of the next date, in the local time of the head node of the cluster.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| UtilizedTime<br/>      | int<br/>           | No<br/> | The amount of time during the day in seconds that the cores of the node were used to run jobs, summed across all of the cores for the node.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CoreAvailableTime<br/> | int<br/>           | No<br/> | The amount of time in seconds that the cores of the node were available to run jobs, summed across all of the cores for the node. The cores on the node are available to run a job if the node had a management state of Online and a node connectivity of OK (Reachable). Thus, this value is equal to the amount of time the node had a management state of Online and a node connectivity of OK (Reachable) multiplied by the number of cores. <br/> The value of the CoreAvailableTime column can be less than the value of the CoreTotalTime column if the node was rebooted, turned off, taken offline, or became unreachable.<br/> |
| CoreTotalTime<br/>     | int<br/>           | No<br/> | The amount of time in seconds that the node was a member of the HPC cluster multiplied by the number of cores for the node. <br/> This value is generally 86,400 times the number of cores for the node unless the node was added to or removed from the cluster on the day to which the row corresponds, because 86,400 is the number of seconds in a day. The value is not affected when the node is rebooted, turned off, taken offline, or becomes unreachable.<br/>                                                                                                                                                                  |



 

## Requirements



|                    |                                       |
|--------------------|---------------------------------------|
| Product<br/> | Windows HPC Server 2008 R2<br/> |



## See also

<dl> <dt>

[**NodeView**](nodeview.md)
</dt> </dl>

 

 




