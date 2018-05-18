---
title: Retrieving Change Status and Ignoring Changes
description: The client can query the routing table manager to find out if a notification of a change to a destination is pending by calling RtmGetChangeStatus. This function returns TRUE until the caller retrieves this change by calling RtmGetChangedDests.
ms.assetid: '778279ac-00c5-4de0-9ac7-eca1ac7fec6a'
---

# Retrieving Change Status and Ignoring Changes

The client can query the routing table manager to find out if a notification of a change to a destination is pending by calling [**RtmGetChangeStatus**](rtmgetchangestatus.md). This function returns **TRUE** until the caller retrieves this change by calling [**RtmGetChangedDests**](rtmgetchangeddests.md).

A client can use this query to avoid performing an action that would have to be undone after the change notification is received and processed. Using this feature allows the client to work efficiently by deferring certain operations to a later time.

The client can also ignore a pending change notification for a destination by calling [**RtmIgnoreChangedDests**](rtmignorechangeddests.md). A later call to [**RtmGetChangedDests**](rtmgetchangeddests.md) does not return this destination unless another change occurs after the call to [**RtmIgnoreChangedDests**](rtmignorechangeddests.md).

 

 




