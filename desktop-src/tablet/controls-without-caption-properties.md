---
description: Introduction to using controls without caption properties for the Tablet PC.
ms.assetid: 8c44e1eb-8d57-4c3b-a329-c8ad77423cb7
title: Controls Without Caption Properties
ms.topic: article
ms.date: 05/31/2018
---

# Controls Without Caption Properties

When a control does not have its own caption property, take the following steps to ensure that accessibility aids can identify the controls:

-   Create a static text control with a meaningful and descriptive name.
-   Place the static label so it immediately precedes the referenced control, in tab order.
-   Ensure that the label text ends with a colon, for example, "Settings:"
-   Position the label text immediately to the left or preceding the referenced control.
-   Make the static text invisible if it is not appropriate to display it visually. Do this by assigning the appropriate attribute in the resource script. This may be appropriate when the name or function of a control is visually provided by means other than static text control, such as a graphic or a related radio button.

The proper use of static controls is the only way to correctly implement underlined access keys for controls that do not have intrinsic labels. For more information about using controls that do not have caption properties, see the [Accessibility](/windows/desktop/accessibility) section.

 

 
