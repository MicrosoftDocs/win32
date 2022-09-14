---
description: You can update the values of nonkey properties of union view class instances. The changes you make to the view class instance will be propagated back to the source class instances that form the union view class.
ms.assetid: 375c9bc8-9f7b-42b4-a841-cf6af88887de
ms.tgt_platform: multiple
title: Updating a Union View
ms.topic: article
ms.date: 05/31/2018
---

# Updating a Union View

You can update the values of nonkey properties of union view class instances. The changes you make to the view class instance will be propagated back to the source class instances that form the union view class.

The following restrictions apply to changes to view class instances:

-   You cannot create new instances of view classes.
-   Only union classes support updates; join and association views create read-only view instances.
-   Success of an update depends on whether a source instance is updateable. If a view instance property maps to a read-only property of a source instance, attempts to modify the view property fail.

 

 



