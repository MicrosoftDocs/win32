---
description: Clicking Run Experts from the Experts window of the Network Monitor UI starts the experts selected for the capture file and calls the Run function. When started, the expert analyzes the capture file by using several expert frame functions.
ms.assetid: 6b8a66cb-d1d6-4e19-b668-049a03a40804
title: Starting and Running Experts
ms.topic: article
ms.date: 05/31/2018
---

# Starting and Running Experts

Clicking **Run Experts** from the Experts window of the Network Monitor UI starts the experts selected for the capture file and calls the [**Run**](run.md) function. When started, the expert analyzes the capture file by using several expert frame functions.

The [**ExpertIndicateStatus**](expertindicatestatus.md) function provides status information from the expert. When you run an expert with Network Monitor, the Expert Status View window displays periodically updated status information (from 0 to 100 percent completion).

![expert status view window](images/exview.png)

The expert is active until the data completes its pass though the capture file. When the pass is complete, an Event Viewer window appears. The information in this window depends on the type of expert that analyzed the data. The following illustration shows a Property Distribution Expert view, which summarizes the frame data that the expert analyzed.

![property distribution expert view](images/exview1.png)

A second report (not shown), summarizes the results of the Transmission Control Protocol (TCP) Retransmit expert.

You can also:

-   Create an entry for an event reference page (ERP) that advises the user of detected conditions or problems (as shown in the Analysis window).
-   Create entries for suggested fixes or explanatory data that provide additional information (as shown in the Resolution window).

After the expert completes its task, Network Monitor removes the expert from active memory. Experts should use the protected memory functions included in the Platform Software Development Kit (SDK); these functions clean up memory if the experts fail during run time.

 

 



