---
description: A simple example project for the Activity Coordinator API.
ms.assetid: 722acf59-ee17-4033-b191-cb0bf53e22ae
title: Activity Coordinator Example Project
ms.topic: article
ms.date: 04/28/2022
---

# Activity Coordinator Example Project

## Example project overview

Let's consider the case of a music editing app. This app has high-priority background tasks that service user requests, like publishing content to cloud storage. There are also low-priority background tasks that support user interaction, like providing automatic recommendations to improve a composition while editing. Lastly, there are a set of deferred tasks that do not need to happen at any specific time without the user’s request. In particular, periodically re-indexing the media catalog to improve search times.

Our focus is on the deferred tasks. For this scenario, we would like to re-index the catalog when we are unlikely to compete for system disk access and when the user isn’t present. We can specify the desired requirements using Activity Coordinator policies. A given machine, at a given point in time, may not necessarily meet all the requirements. The Activity Coordinator API will use policies in order to determine if the requirements have been met, so we can accordingly get notifications for when to Start or Stop running our work. In this case, the **GOOD** policy template meets our needs as it tracks CPU, memory, system disk, power, and user-idle. The work itself has been broken down to happen in small chunks, so that we can adequately respond to notifications.

## Download the example project

Download the example project from the [Windows classic samples](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/ActivityCoordinator) GitHub repository.

## Related topics

[Activity Coordinator API overview](activity-coordinator-api-overview.md)

[Activity Coordinator API and terminology](activity-coordinator-api-and-terminology.md)

[Choosing the right Activity Coordinator policy](choosing-the-right-activity-coordinator-policy.md)
