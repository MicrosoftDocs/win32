---
description: Overview of the Activity Coordinator API.
ms.assetid: 05aa4f50-4365-4707-bed7-8eba2a723d93
title: Activity Coordinator API Overview
ms.topic: article
ms.date: 04/27/2022
---

# Overview of the Activity Coordinator API

The Activity Coordinator API coordinates execution of **deferrable tasks**, called activities, on a system. Activities can defer their execution to a time when the system is in a desired state, where running the task does not interfere with the user's experience or system performance. This allows the total consumption of applications on the system to be more evenly distributed across times when the user is inactive or the system is idle. The API provides centralized coordination of these decisions to help avoid scenarios where applications degrade the user experience by competing for system resources.

## Usage

Developers use the API by defining policies which describe the desired state of the system during which they want to execute their activities. By subscribing to these policies, developers get notified when to start or stop their activity based on the satisfaction of their policy's conditions. The API coordinates these notifications among subscriptions on the system to provide a centralized determination of what is an **appropriate time** to perform deferrable work.

Using the API does not prevent applications from running work as they see fit. It relies on them to be good citizens, choosing appropriate policies and making execution decisions in response to API notifications. Additionally, using the API requires the calling process to be running. Applications should not rely on the Activity Coordinator API for high-priority work that needs to run irrespective of system conditions.

Windows has several APIs available to developers for deferring or scheduling tasks. Use the following guide to determine which API is best for your application.

| API | Intended use |
|-----|-----|
| Activity Coordinator | Use Activity Coordinator to coordinate execution of deferrable tasks based on desired system conditions. |
| [Background Intelligent Transfer Service (BITS)](../Bits/background-intelligent-transfer-service-portal.md) | BITS is used by programmers and system administrators to download files from or upload files to HTTP web servers and SMB file shares. It will take the cost of the transfer into consideration, as well as the network usage so that the user's foreground work has as little impact as possible. |
| [Task Scheduler](../taskschd/task-scheduler-start-page.md) | The Task Scheduler enables you to automatically perform routine tasks on a chosen computer. Use this API to execute tasks such as starting an application, sending an email message, or showing a message box. Tasks can be scheduled to execute in response to events, or triggers. |

## Policies, resources, and conditions

Policies describe the conditions of many system resources. Developers configure policies by associating each resource with a desired “condition” to begin using that resource. Conditions describe the qualitative state of a resource and may be evaluated by factors.

The combination of resources and conditions allows developers to describe the desired state of the system to help ensure that running their workload does not adversely impact the user experience or system performance. As the system state is always changing, subscribing to these policies provides notifications of when to start or stop work based on whether the policy is satisfied (open) or unsatisfied (closed).

## Policy templates

Policy templates are a way for developers to configure their policies with pre-defined resource-conditions designed to meet the needs of most applications. A policy template is required when creating a policy and is used as a starting point to configure policies specific to the developer's needs. An empty policy template is provided for developers wanting full control over their policy.

## Related topics

[Activity Coordinator API and terminology](activity-coordinator-api-and-terminology.md)

[Choosing the right Activity Coordinator policy](choosing-the-right-activity-coordinator-policy.md)

[Activity Coordinator example project](activity-coordinator-example-project.md)
