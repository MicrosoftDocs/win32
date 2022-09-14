---
title: Edge UI is suppressed in “in-out-in” and “inertia” scenarios
description: Edge UI is suppressed in “in-out-in” and “inertia” scenarios
ms.assetid: 005B6D03-52A6-4780-8D3E-4A5CDA5EED8C
ms.topic: article
ms.date: 05/31/2018
---

# Edge UI is suppressed in “in-out-in” and “inertia” scenarios

## Platform

<dl> Clients - Windows 8.1  
</dl>

## Description

There are some cases where users may unintentionally invoke Edge UI (Charms, App Bar, app switching). We have introduced a feature to allow developers to design their UI for the whole screen without making affordances (for example, borders) to prevent the user from accidentally hitting the edges.

There are two cases that might lead most often to inadvertent edge swipes:

-   In fast panning, the speed and imprecision of the interaction can occasionally cause them to come in from the edge of the screen
-   If users rapidly leave and re-enter the screen area while inking with their finger, for example, in a painting app, this in-out-in behavior can mistakenly trigger the Edge UI and interrupt the user experience

To improve the user and developer experience, the Edge UI will now be suppressed in two specific instances:

-   When a user is panning in an application that supports DManip Inertia and swipes outside of the screen while inertia is occurring, the Edge UI will not be invoked within a timeout window
-   On certified devices, when a user quickly swipes from within the screen to outside the screen and back inside (in-out-in motion) within certain parameters, the Edge UI will not be invoked

## Manifestations

Users quickly swiping against the edge while using an app will see a decrease in unintentional edge invocation.

## Solution

Developers should keep these mitigations in mind and should be able to use the full screen without fear that users will accidentally trigger the Edge UI while interacting with the application along the edge.

 

 




