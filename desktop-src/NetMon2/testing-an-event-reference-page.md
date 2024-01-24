---
description: The final step of creating an event reference page (ERP) is to test it.
ms.assetid: 12690317-1cd2-496c-8a0d-ba6caca58b86
title: Testing an Event Reference Page
ms.topic: article
ms.date: 05/31/2018
---

# Testing an Event Reference Page

The final step of creating an event reference page (ERP) is to test it. You can test an ERP by viewing the file in an HTML browser such as Microsoft Internet Explorer. Or, you can install the ERP and its expert DLL to test it for event invocation and display it in the Network Monitor Event Viewer.

## Viewing ERPs that Have No DLL

To view the completed ERP without an installed expert DLL, open the file with an HTML viewer that supports your embedded sources. The following illustration shows the sample ERP file described in [Writing an ERP](writing-an-event-reference-page.md) as it is displayed using Microsoft Internet Explorer Version 4.01.

![sample erp file](images/ie-erp.png)

Testing ERPs that Have a DLL

After the ERP files and the [**expert**](experts.md) DLL is created, you can test the complete functionality of your ERPs with Network Monitor. It is assumed that the DLL is debugged and can generate valid events.

**To test ERPs that have a DLL**

1.  Verify that the correct expert DLL is installed in the appropriate directory. For more information, see [Installing an Expert to Network Monitor 2.1](installing-an-expert-to-network-monitor-2-1.md).
2.  Verify the [correct name](naming-an-event-reference-page.md) of the ERP file.
3.  Verify the [correct location](installing-existing-erps-to-network-monitor-2-1.md) of the ERPs in the Network Monitor directory.
4.  Test expert ERPs in the Network Monitor UI.
5.  Generate a test event.
6.  Verify that the ERP appears in the Network Monitor Event Viewer.

For more information about creating an ERP, see:

-   [Creating Expert and Monitor Event Reference Pages](creating-expert-and-monitor-event-reference-pages.md)
-   [Writing an Event Reference Page](writing-an-event-reference-page.md)
-   [Naming an Event Reference Page](naming-an-event-reference-page.md)

 

 



