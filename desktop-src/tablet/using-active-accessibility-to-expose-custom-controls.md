---
description: Description of using active accessibility to expose custom controls for the Tablet PC.
ms.assetid: 1557bde2-c382-4259-ae0c-a70902fa91bd
title: Using Active Accessibility to Expose Custom Controls
ms.topic: article
ms.date: 05/31/2018
---

# Using Active Accessibility to Expose Custom Controls

You can use Microsoft Active Accessibility as an effective way to make custom controls compatible with accessibility aids. Active Accessibility requires that the application:

-   Create Component Object Model (COM) objects that represent individual custom controls or groups of controls that properly support the **IAccessible** interface. (The object may be created on demand when it is requested by an Active Accessibility client.)
-   Call [**NotifyWinEvent**](/windows/win32/api/winuser/nf-winuser-notifywinevent) when the controls are created or destroyed, gain or lose focus, or otherwise change state.
-   Handle the WM\_GETOBJECT message when used to query properties of the object or objects.

For the purposes of this discussion, a window containing other custom objects also needs to be exposed to Active Accessibility, allowing the client to discover and navigate to the child objects. For more information about how to make custom controls compatible with accessibility aids, see [Accessibility](../accessibility/accessibility.md).

 

 
