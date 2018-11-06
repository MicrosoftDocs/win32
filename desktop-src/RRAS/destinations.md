---
title: Destinations
description: A destination in the routing table is a network entry represented by a network address and a network mask.
ms.assetid: 115d86e3-f933-4601-af10-abaab287b509
ms.topic: article
ms.date: 05/31/2018
---

# Destinations

A destination in the routing table is a network entry represented by a network address and a network mask.

A destination entry in the routing table includes:

-   The address, expressed as a network address and network mask.
-   A list of routes to the destination.
-   A list of opaque pointer slots.
-   The views in which this destination is valid. The destination contains a structure for each view that contains the following information:
    -   An identifier for the view.
    -   A pointer to the best route to the destination in this view.
    -   The owner of the best route in this view.
    -   Flags associated with the best route in this view.
    -   Handle to any routes that are in a hold-down state in this view.

 

 




