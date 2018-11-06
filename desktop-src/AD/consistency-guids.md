---
title: Consistency GUIDs
description: Consistency GUIDs are a detection strategy that allows an application to detect partial updates.
ms.assetid: 3418667f-4d5a-4a4b-b0f5-7744a21608f7
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Consistency GUIDs

Consistency GUIDs are a detection strategy that allows an application to detect partial updates. A consistency GUID (Globally Unique IDentifier) is applied to each object in a related set. In implementation, a source application generates a new GUID and applies it to each object it updates in the set of related objects. It then applies the new GUID to the rest of the objects in the set, and finishes by applying the new GUID to the "master" object. Typically, the "master" object will be a container that is the parent of the other objects in the set.

Some important considerations:

-   Consistency GUIDs combined with object counts or checksums are more effective than consistency GUIDs alone, because the application reading the objects may not know how many objects with the GUID should be present.
-   Applications must generate their own GUIDs (a Microsoft Win32 API, UuidCreate, provides this function), and not use the system-generated GUIDs found in an object's **objectGUID** attribute. This is because a consistency GUID needs to change each time the set of objects is updated. Object identity GUIDs found in **objectGUID** never change after the object has been created.
-   Consistency GUIDs assume that no object is shared among sets, so each set can have a unique consistency GUID.

 

 




