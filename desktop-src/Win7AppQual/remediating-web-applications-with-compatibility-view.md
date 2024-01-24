---
description: Fixing Compatibility Issues in Web Applications by Using Compatibility View
ms.assetid: ACAC2375-EA6C-4AA1-90B7-0BF237A51C02
title: Fixing Compatibility Issues in Web Applications by Using Compatibility View
ms.topic: article
ms.date: 05/31/2018
---

# Fixing Compatibility Issues in Web Applications by Using Compatibility View

This section describes basic mitigation steps and how to plan for future application compatibility while you are addressing any issues now.

Windows Internet Explorer supports the legacy Internet Explorer models whenever feasible so that sites that you develop to them continue to behave as expected in newer versions of Internet Explorer. Starting with Windows Internet Explorer 8, you can choose to support legacy behaviors by selecting the rendering mode on a page-by-page basis.

Internet Explorer 8 includes the following rendering modes that you can set by using the X-UA-Compatible header.



| Content value | Description                                                                           |
|---------------|---------------------------------------------------------------------------------------|
| IE=5          | Use quirks mode.                                                                      |
| IE=7          | Always use Windows Internet Explorer 7 mode.                                          |
| IE=EmulateIE7 | Display in Internet Explorer 7 mode unless the site has the quirks DOCTYPE.           |
| IE=8          | Always use Internet Explorer 8 mode.                                                  |
| IE=EmulateIE8 | Override Compatibility View on client machines and use Internet Explorer 8 mode.      |
| IE=Edge       | Display in the latest mode. In Internet Explorer 8, this value is equivalent to IE=8. |



 

The following topics describe how to update web applications by using Compatibility View.



| Topic                                                                                                  | Description                                                                    |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [What Is Compatibility View](what-is-compatibility-view-.md)                                          | Describes Compatibility View.                                                  |
| [Why Do You Need Compatibility View?](why-do-you-need-compatibility-view-.md)                         | Describes why you should use Compatibility View.                               |
| [Use the Meta Tag to Ensure Future Compatibility](use-the-meta-tag-to-ensure-future-compatibility.md) | Describes how you can use the **meta** element to ensure future compatibility. |



 

 

 



