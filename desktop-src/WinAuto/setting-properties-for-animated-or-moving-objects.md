---
title: Setting Properties for Animated or Moving Objects
description: For animation controls, such as the animation control displayed when copying files, use the ROLE\_SYSTEM\_ANIMATION object role.
ms.assetid: '8c5ebbc3-4066-452b-8f37-2fb595adea53'
---

# Setting Properties for Animated or Moving Objects

For animation controls, such as the animation control displayed when copying files, use the [**ROLE\_SYSTEM\_ANIMATION**](object-roles.md#role-system-animation) object role. For graphics that are occasionally animated, use the [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md#role-system-graphic) object role with the [**State**](state-property.md) set to [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md#state-system-animated).

Use the [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md#state-system-animated) flag to mark an object whose appearance changes rapidly. Clients use this flag to avoid notifying users repeatedly for what is really a single series of visual changes.

An example of this is marquee text, which is disclosed progressively as it scrolls across the screen. Such objects are given the attribute of [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md#state-system-animated). In most cases the object's [**Value**](value-property.md) string reflects the entire text, even the portion not currently visible. Changing the **Value** string frequently to correspond to the text currently visible is not recommended because it results in far too many [**EVENT\_OBJECT\_VALUECHANGE**](event-constants.md#event-object-valuechange) events that do not convey useful information.

For example, in a window that contains a rectangular region that shows the word "Yes!" moving in a figure-eight pattern, the [**Role**](role-property.md) is [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md#role-system-graphic), the [**Value**](value-property.md) property is the string displayed, the [**Location**](iaccessible-iaccessible--acclocation.md) property is the bounding rectangle around the text, and the [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md#state-system-animated) attribute flag is set. The [**Description**](description-property.md) is "The word 'Yes!' is moving around the screen in a figure-eight pattern." The server generates only [**EVENT\_OBJECT\_STATECHANGE**](event-constants.md#event-object-statechange) events when the object starts or ceases animation.

 

 




