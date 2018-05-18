---
Description: 'The Windows operating system accumulates a set of operating statistics for workstations and servers from the time that the workstation or server service is started.'
ms.assetid: '4e0217bf-7550-40a2-b47c-8e898a586005'
title: Statistics Functions
---

# Statistics Functions

The Windows operating system accumulates a set of operating statistics for workstations and servers from the time that the workstation or server service is started. To retrieve these statistics, you can call the following network management statistics function.



| Function                                     | Description                                                                                 |
|----------------------------------------------|---------------------------------------------------------------------------------------------|
| [**NetStatisticsGet**](netstatisticsget.md) | Retrieves operating statistics for a service; supports the workstation and server services. |



 

The **NetStatisticsGet** function returns a [**STAT\_WORKSTATION\_0**](stat-workstation-0-str.md) structure when workstation statistics are requested; the function returns a [**STAT\_SERVER\_0**](stat-server-0-str.md) structure when server statistics are requested.

 

 



