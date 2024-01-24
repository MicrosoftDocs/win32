---
description: After you author an event reference page (ERP) source HTML document, you must name it before Network Monitor can display it in the Event Viewer.
ms.assetid: 0c668a8b-94a5-4996-8214-4629a24a8337
title: Naming an Event Reference Page
ms.topic: article
ms.date: 05/31/2018
---

# Naming an Event Reference Page

After you author an event reference page (ERP) source HTML document, you must name it before Network Monitor can display it in the Event Viewer.

Name monitor and expert ERP files with this format:

``` syntax
<ExpertName><EventIdent>.htm (or <MonitorName><EventIdent>.htm)
```

<dl> <dt>

<span id="ExpertName"></span><span id="expertname"></span><span id="EXPERTNAME"></span>**ExpertName**
</dt> <dd>

DLL file name, excluding the file name extension.

</dd> <dt>

<span id="EventIdent"></span><span id="eventident"></span><span id="EVENTIDENT"></span>**EventIdent**
</dt> <dd>

Event identifier of the expert ERP.

The event identifier is also found in the **EventIdent** member of the **NMEVENTDATA** structure.

</dd> </dl>

For more information about creating an ERP, see the following topics:

-   [Creating Expert and Monitor Event Reference Pages](creating-expert-and-monitor-event-reference-pages.md)
-   [Writing an Event Reference Page](writing-an-event-reference-page.md)
-   [Testing an Event Reference Page](testing-an-event-reference-page.md)

 

 



