---
title: Binding to the Search Start Point
description: The start point for a search is a container that directly or indirectly contains the objects searched for.
ms.assetid: f93c1310-7c8b-4d28-bd4d-6fab969d3353
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , binding to a search start point
ms.topic: article
ms.date: 05/31/2018
---

# Binding to the Search Start Point

The start point for a search is a container that directly or indirectly contains the objects searched for. The search will not be performed in containers above the search start point. For example, take the following hypothetical directory structure:

``` syntax
Domain A
    Container 1
        Object 1
        Object 2
    Container 2
        Object 3
        Object 4
```

If a search is performed for all objects and the search start point is "Container 2", only "Object 3" and "Object 4" would be retrieved. If the same search was performed with the search start point at "Container 1", "Object 1" and "Object 2" would be retrieved.

To bind to the search start point, bind to the ADsPath of the container that will be the search start point.

 

 




