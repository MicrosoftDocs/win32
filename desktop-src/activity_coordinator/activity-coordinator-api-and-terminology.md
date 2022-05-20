---
description: An overview of the Activity Coordinator API and some of its common terms.
ms.assetid: 483d721a-7543-44c7-bdb2-16848c84cf81
title: Activity Coordinator API and terminology
ms.topic: article
ms.date: 05/12/2022
---

# Activity Coordinator API and terminology

The Activity Coordinator API **coordinates execution of deferrable tasks, called activities, on a system**. Developers can use the API to get notifications of when to start or stop an activity based on a desired system state. This state is defined by a policy, which describes the optimal conditions of system resources while running an activity. Developers subscribe to these policies to have notifications sent to a supplied callback, which they use to coordinate the execution of their activity.

>**Note** These notifications are to coordinate low priority or resource intensive tasks that can be deferred to a later time. If there is a high priority task that needs to happen irrespective of the system conditions, it should not rely on this API.

## API-specific terminology

### Resource

A resource is a physical component or attribute of the system which is consumed or affected by an activity. Simple examples are traditional system resources like CPU, system-disk, and GPU. Less traditional resources include things like power and user-idle.

### Condition

A condition is a qualitative description of a resource’s desired state as either **good**, **medium**, or **not set**. At a basic level, a _good condition_ means it is a _good time_ to use a resource. A given resource-condition pair may be evaluated using a variety of dimensions.

Developers must choose which conditions to use for individual resources, so they will fit the needs of their workload. This allows the API to best coordinate work among its consumers.

### Deferrable

**Deferrable tasks** are those tasks which don’t immediately affect the user experience of an application, though the lack of execution over an extended period may still affect the overall experience. In general, these tasks don’t need to be run immediately and can defer their execution to a time when the system is in a desirable state. These are times when running the task does not interfere with the user's experience or system performance. Such tasks could include:

- Re-indexing a media catalog
- Training or updating a recommendation model
- Installing plugin updates

### Activity

An **activity** is a **deferrable unit of work** as defined by the developer. Activities inherently consume system resources to execute, which may result in impact to the user experience. Developers must understand how their activity consumes these resources so they can appropriately use the API. Then, they can defer activity execution to a more ideal time using the API, rather than immediately executing such work at times which may significantly impact the user experience.

### Policy

Policies define what an **ideal time** time to run means by describing the desired conditions of various resources required to run or impacted by the developer’s activity. A policy is formed by several pairs of resources and conditions, defining individual **resource conditions**.

A policy may specify conditions for resources like Power, Memory, and CPU, but also exclude resources like GPU based on their relevance. A policy is considered **open** when all resource conditions are met and **closed** otherwise. Policies do not describe how much of a given resource an activity is expected to consume. The API uses policy configurations to make coordination decisions among API consumers.

When configuring a policy, it is recommended that the developer starts with the best (**good**) condition for each resource so that the API can help them run at the best times, when execution is least likely to impact the user's experience or system performance. Conditions may be lowered (e.g., from **good** to **medium**) afterwards if the activity is not notified to run frequently enough or long enough to meet the developer's needs.

### Subscription

Subscriptions are the coordination mechanism for activities. Developers subscribe to a policy with a callback, which the API calls with coordination notifications. These notifications inform the developer when they should start/resume or stop/pause their activity. Notifications are based on the resource conditions of the subscribed policy, as configured at time of subscription, and coordination decisions made by the API.

### Policy template

A member of the enum **ACTIVITY_COORDINATOR_POLICY_TEMPLATE**. These can be used when creating a policy to pre-configure it with reasonable conditions designed to meet the common needs of most activities and minimize impact to the user.

### Downgrade

You can **downgrade** a policy or resource by changing from better to lesser conditions to make it more permissive and increase the likelihood of the policy's conditions being satisfied. For example, you can downgrade a **good** condition for **CPU** by changing it to a **medium** condition. A medium condition has less restrictive requirements and is therefore more likely to be met. At the policy level, this increases the likelihood that the policy will open (all resource conditions are satisfied) more frequently and for longer periods of time, keeping in mind that these may be times when there is greater likelihood of causing user impact or degrading system performance.

## Available actions

The API allows the developer to do the following actions:

- Configure a policy.
- Subscribe / unsubscribe to notifications for policies.

The API provides the flexibility of customizing policies to best fit the developer scenario, starting from either an empty policy configuration or one of the template configurations which target the needs of most apps. In the simplest case:

- Allocate a policy using a template policy-ID within **ACTIVITY_COORDINATOR_POLICY_TEMPLATE**.

For a more custom developer scenario,

- Allocate a template policy (potentially an empty one).
- Set the desired conditions for the relevant resources.

## Related topics

[Activity Coordinator API overview](activity-coordinator-api-overview.md)

[Choosing the right Activity Coordinator policy](choosing-the-right-activity-coordinator-policy.md)

[Activity Coordinator example project](activity-coordinator-example-project.md)
