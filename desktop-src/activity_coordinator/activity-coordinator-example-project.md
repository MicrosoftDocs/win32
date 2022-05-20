---
description: A simple example project for the Activity Coordinator API.
ms.assetid: 722acf59-ee17-4033-b191-cb0bf53e22ae
title: Activity Coordinator example project
ms.topic: article
ms.date: 04/28/2022
---

# Activity Coordinator example project

## Example project overview

Let's consider the case of a music editing app. This app has high-priority background tasks that service user requests, like publishing content to cloud storage. There are also low-priority background tasks that support user interaction, like providing automatic recommendations to improve a composition while editing. Lastly, there are a set of deferred tasks that do not need to happen at any specific time without the user’s request, which our focus in this example. In particular, we want to periodically re-index the media catalog to improve search times. We can use the Activity Coordinator API to coordinate when this re-indexing occurs.

For this scenario, we would like to re-index the catalog when the user isn’t present and when it's a good time to use the system-disk. We can specify these requirements using Activity Coordinator policies. A given machine, at a given point in time, may not necessarily meet all the requirements and may have different factors contributing to the satisfaction of these requirements. The Activity Coordinator API will use our policy to determine if the requirements have been met and send notifications for when to Start or Stop running our work.

In this case, the **GOOD** policy template meets our needs as it tracks CPU, memory, system disk, power, and user-idle. The work itself has been broken down to happen in small chunks, so that we can adequately respond to notifications.

## Download the example project

Download the example project from the [Windows classic samples](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/ActivityCoordinator) GitHub repository.

## Related topics

[Activity Coordinator API overview](activity-coordinator-api-overview.md)

[Activity Coordinator API and terminology](activity-coordinator-api-and-terminology.md)

[Choosing the right Activity Coordinator policy](choosing-the-right-activity-coordinator-policy.md)
