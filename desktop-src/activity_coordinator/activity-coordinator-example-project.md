---
description: A simple example project for the Activity Coordinator API.
ms.assetid: 722acf59-ee17-4033-b191-cb0bf53e22ae
title: Activity Coordinator example project
ms.topic: article
ms.date: 04/28/2022
---

# Activity Coordinator example project

## Example project overview

Let's consider the case of a music editing app. This app has high-priority background tasks that service user requests, like publishing content to cloud storage. There are also low-priority background tasks that support user interaction, like providing automatic recommendations to improve a composition while editing. Lastly, there are a set of deferred tasks that do not need to happen at any specific time without the user’s request, which our focus in this example. In particular, we would like to periodically retrain the recommendation model when user impact is minimal. We can use the Activity Coordinator API to achieve this.

For this scenario, we would like to re-train the model when the user isn’t present. The retraining workflow in this scenario is also a GPU consumer, so we also want to run when it's a good time to use the GPU. We can specify these requirements using Activity Coordinator policies. The Activity Coordinator API will use our policy to determine when the requirements are met and send notifications for when to start or stop running our work.

In this case, the **GOOD** policy template meets most our needs as it tracks CPU, memory, system disk, power, and user-idle. We simply need to explicitly set a condition for GPU. It's important to remember that even though our workload will primarily utilize the GPU, the execution of our activity still inherently consumes CPU, memory, disk, and power. Our impact to these resources may also vary greatly between system configurations. For instance, a faster GPU could result in the CPU spending more time feeding the GPU with data, which may then result in more data being read or saved to disk. The speed of this disk may also affect CPU consumption in a similar fashion. By configuring all the resources we affect, we can be sure we don't inadvertently interfere with the user experience or degrade system performance. Additionally, the work itself has been broken down to happen in small chunks, so that we can adequately respond to coordination notifications to avoid running outside of the desired conditions.
To demonstrate how developers can change or downgrade policies, we also add the requirement that we want retraining to complete within 48-hours. The first 24-hours, our soft deadline, we attempt to run with our ideal policy, and the last 24-hours we downgrade to a lesser policy. 
## Download the example project

Download the example project from the [Windows classic samples](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/ActivityCoordinator) GitHub repository.

## Related topics

[Activity Coordinator API overview](activity-coordinator-api-overview.md)

[Activity Coordinator API and terminology](activity-coordinator-api-and-terminology.md)

[Choosing the right Activity Coordinator policy](choosing-the-right-activity-coordinator-policy.md)
