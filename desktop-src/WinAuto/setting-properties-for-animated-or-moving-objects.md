---
title: Setting Properties for Animated or Moving Objects
description: For animation controls, such as the animation control displayed when copying files, use the ROLE\_SYSTEM\_ANIMATION object role.
ms.assetid: 8c5ebbc3-4066-452b-8f37-2fb595adea53
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Properties for Animated or Moving Objects

For animation controls, such as the animation control displayed when copying files, use the [**ROLE\_SYSTEM\_ANIMATION**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_ANIMATION**) object role. For graphics that are occasionally animated, use the [**ROLE\_SYSTEM\_GRAPHIC**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_GRAPHIC**) object role with the [**State**](state-property.md) set to [**STATE\_SYSTEM\_ANIMATED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_ANIMATED**).

Use the [**STATE\_SYSTEM\_ANIMATED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_ANIMATED**) flag to mark an object whose appearance changes rapidly. Clients use this flag to avoid notifying users repeatedly for what is really a single series of visual changes.

An example of this is marquee text, which is disclosed progressively as it scrolls across the screen. Such objects are given the attribute of [**STATE\_SYSTEM\_ANIMATED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_ANIMATED**). In most cases the object's [**Value**](value-property.md) string reflects the entire text, even the portion not currently visible. Changing the **Value** string frequently to correspond to the text currently visible is not recommended because it results in far too many [**EVENT\_OBJECT\_VALUECHANGE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_VALUECHANGE**) events that do not convey useful information.

For example, in a window that contains a rectangular region that shows the word "Yes!" moving in a figure-eight pattern, the [**Role**](role-property.md) is [**ROLE\_SYSTEM\_GRAPHIC**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_GRAPHIC**), the [**Value**](value-property.md) property is the string displayed, the [**Location**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation) property is the bounding rectangle around the text, and the [**STATE\_SYSTEM\_ANIMATED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_ANIMATED**) attribute flag is set. The [**Description**](description-property.md) is "The word 'Yes!' is moving around the screen in a figure-eight pattern." The server generates only [**EVENT\_OBJECT\_STATECHANGE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_STATECHANGE**) events when the object starts or ceases animation.

 

 




