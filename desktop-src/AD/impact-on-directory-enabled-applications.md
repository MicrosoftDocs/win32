---
title: Impact on Directory-Enabled Applications
description: This topic describes the impact on directory-enabled applications when version skews, partial updates, or collisions occur.
ms.assetid: 0aec6fe3-7757-4472-bc18-add2327d4e1b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Impact on Directory-Enabled Applications

## Version Skew

Version skew occurs when applications read the same objects from different replicas before a change has replicated. Applications reading the remote replica recognize the unchanged object. Version skew is an issue when a given application or set of applications use the data in the directory to interoperate.

For example, an RPC Service can publish its endpoints in the directory using standard RPC APIs (such as [**RpcNsBindingExport**](/windows/desktop/api/rpcnsi/nf-rpcnsi-rpcnsbindingexporta)). Clients connect to the service by looking up the desired endpoint in the directory ( [**RpcNsBindingLookupBegin**](/windows/desktop/api/rpcnsi/nf-rpcnsi-rpcnsbindinglookupbegina), [**RpcNsBindingLookupNext**](/windows/desktop/api/rpcnsi/nf-rpcnsi-rpcnsbindinglookupnext), and so on) and binding to it.

Assume that an RPC Service S₁ publishes endpoint Eₛ₁ and subsequently moves to a different computer. The original endpoint Eₛ₁ is changed to E<sub>s2,</sub> reflecting the new computer's address. Clients reading remote replicas of the directory service are unable to connect to the service until the updated endpoint is replicated. However, moving a service from one computer to another is a rare occurrence; therefore, this interruption/delay should rarely be encountered, especially if the movement of the service is well-planned.

## Partial Updates

In general, partial update occurs when one application is reading a set of data while another application is writing to that same set of data. This is a situation that can occur with any application in a multi-mastered system. There are many ways this can occur. You could have more than one application writing to the same data set at once. If you look at it this way, the directory replication service is just another application that could potentially be writing to the same data set that another application may be reading. This could be a potential problem for an application. However, the window of time in which a partial update can affect your application is relatively small. This should rarely if ever be an issue for applications that are not dependent on the synchronization of multiple objects. If your application is highly dependent on the synchronization of a related set of objects, you should consider the effects of a partial update in your application design.

In terms of the directory replication, partial update occurs when applications read the same set of objects from different replicas while replication is in progress. Applications at the remote replica see some, but not all, of the changes.

> [!Note]  
> The window in which partial update can affect an application is small: the application must start reading objects while inbound replication is in progress, after one or more of the related, changed objects have been received but before all have been received. The time between the updates at the source replica directly affects the size of this window—updates that occur close together in time are replicated close together in time. Partial update can be an issue when an application uses a related set of objects.

 

For example, a remote access service can use the directory to store policy and profile data. The policy data is stored in one set of objects, and the profile in another set. When a user connects to the remote access service, the remote access service reads the policy to determine whether the user is allowed to connect, and if so what profile to apply to the user session. Partial update can affect the remote access service in several ways:

-   If the policy is complex and consists of multiple objects, the remote access service might read a partially updated policy resulting in incorrect denial or granting of service to the user, inability to process the policy due to internal inconsistency, and so on.
-   If both the policy and profiles have been updated, the service might correctly process the policy but apply a stale profile, because the policy objects have replicated but the profile objects have not.
-   If the profile is complex and consists of multiple objects, the service might correctly process the policy but apply a partially updated profile because the policy objects have replicated, but only some of the profile objects have done so.

## Collisions

Collisions occur when the same attributes of two or more replicas of a given object are changed during the same replication interval. The replication process reconciles the collision; because of reconciliation a user or application may "see" a value other than the one they wrote.

A simple example is user address information: A user changes a mailing address at replica R1 and an administrator changes the same mailing address at replica R2. A written value propagates until another value is selected over that value by the collision reconciliation mechanism. As long as a value continues to "win" against other values in the collision resolution process, the value continues to propagate. Ultimately, this "winning" value will be propagated to R1,R2, and all other replicas if no other changes are made.

Collision resolution is an issue for applications that make assumptions about the internal consistency of objects or sets of objects. For example, a network bandwidth allocation management service stores network bandwidth data for a given network segment in the directory in an object O1. The object contains the bandwidth available in bits-per-second and the maximum bandwidth any single user can reserve. The service expects that the user reservable bandwidth will always be less than or equal to the bandwidth available.

Consider the following sequence of events:

-   The object in the initial fully replicated state gives the available bandwidth as 56 kilobits-per-second, and the user reservable bandwidth as 9,600 bits-per-second.
-   An administrator at replica R₁ changes the values to 64k and 19,200 respectively.
-   An administrator at replica R₂ changes the values to 10 million and 1 million respectively before the update from R₁ arrives.

Assuming the attributes in question have equal version numbers when the updates occur, there is a small, but real, possibility that the object will end up with a maximum bandwidth of 64k and a user reservable maximum of 1 million—if the application performs the updates as separate write operations. The application should always update both properties in a single operation.

 

 