---
description: Overview of the Activity Coordinator API.
ms.assetid: 05aa4f50-4365-4707-bed7-8eba2a723d93
title: Activity Coordinator API Overview
ms.topic: article
ms.date: 04/27/2022
---

# Overview of the Activity Coordinator API

The Activity Coordinator API coordinates execution of deferrable tasks on a system. Deferrable tasks are tasks that can defer their execution to a time when the system is in a desired state where running the task does not interfere with other ongoing work. This allows the total consumption of applications on the system to be more evenly distributed across times when the system is otherwise idle, or the user is inactive. The API helps avoid scenarios where applications cause contention for system resources and negatively impact the user’s experience.

## Usage

Developers use the API by defining policies which describe the desired state of the system during which they want to execute their activities. By subscribing to these policies, developers get notified when to start or stop their activity based on the satisfaction of their policy’s conditions. The API coordinates these notifications among subscriptions on the system to provide a centralized determination of what is an “appropriate time” to perform deferrable work.
Opting into the API does not prevent applications from running work at bad times. It relies on them to be good citizens. Additionally, using the API requires the calling process to be running. Applications should not rely on the Activity Coordinator API for high-priority work that needs to run irrespective of system conditions.

**Mention other scheduling APIs here (task scheduler, BITS)?**

## Policies, resources, and conditions

Policies describe many attributes of the system. These include power state, battery levels, user presence, CPU usage, system-disk usage, etc. **Link other doc here with terminology.** Developers customize policies by associating resources with a desired “condition” to begin using that resource. **Link to Guidance for Choosing a Policy here.** Conditions describe the state of a resource and may be evaluated by factors such as its utilization or presence.

The combination of resources and conditions allows developers to describe the desired state of the system to help ensure that running their workload does not adversely impact the system or its users. As the system state is always changing, subscribing to these policies provides notifications of when to start or stop work based on whether the policy is satisfied (open) or unsatisfied (closed).
Activity management

The API will stagger the starting and stopping of activities between multiple consumers to avoid the thundering herd problem seen with existing global notification mechanisms, such as those caused by the low memory event.

Additionally, the threshold to transition from a satisfied to unsatisfied resource condition will be offset such that there is a net availability of each resource. This helps prevent policy transitions from open to closed due to the net resources consumed by the activities notified to run and improves the likelihood that many activities can coexist peacefully on the same system without superfluous start/stop notifications that would dissuade interested consumers.

## Policy templates

Policy templates are a way for developers to configure their policies with pre-defined resource-conditions designed to meet the needs of most applications. A policy template is required when creating a policy but does not prevent further customization to meet their needs. An empty policy template is provided for developers wanting full control over their policy.

## Related topics

[Activity Coordinator API and terminology](activity-coordinator-api-and-terminology.md)

[Choosing the right Activity Coordinator policy](choosing-the-right-activity-coordinator-policy.md)

[Activity Coordinator example project](activity-coordinator-example-project.md)
