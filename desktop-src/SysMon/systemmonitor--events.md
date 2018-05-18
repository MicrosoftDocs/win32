---
title: SystemMonitor Events
description: The SystemMonitor class has the following events
ms.assetid: '64d9befd-5ea0-4888-b0fb-cff889f1d188'
---

# SystemMonitor Events

The [**SystemMonitor**](systemmonitor.md) class has the following events:

-   [**OnCounterAdded**](systemmonitor-oncounteradded.md)
-   [**OnCounterDeleted**](-systemmonitor-oncounterdeleted.md)
-   [**OnCounterSelected**](-systemmonitor-oncounterselected.md)
-   [**OnDblClick**](-systemmonitor-ondblclick.md)
-   [**OnSampleCollected**](-systemmonitor-onsamplecollected.md)

> [!Note]  
> You must return from the event handler before the [**update interval**](systemmonitor-updateinterval.md) expires; otherwise, SYSMON displays a message box indicating to the user that it was unable to sample counter values for the previous update interval.

 

 

 




