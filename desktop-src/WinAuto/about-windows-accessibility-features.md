---
title: About Windows Accessibility Features
description: There are two categories of accessibility features that correspond to the settings available to users through the Ease of Access Center in Control Panel
ms.assetid: 823bbc5b-062b-43ef-9f3e-822dc6f55c5d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Windows Accessibility Features

There are two categories of accessibility features that correspond to the settings available to users through the Ease of Access Center in Control Panel:

-   [Accessibility parameters](accessibility-parameters.md). When set, these parameters indicate that applications should change their default behavior. Applications can check the state of an accessibility parameter to determine whether the user wants special behavior that can be provided in an application-specific manner. For example, the ShowSounds parameter indicates that an application that typically uses sound to convey important information should also provide the information visually.
-   [Built-in accessibility features](built-in-accessibility-features.md). These features are built into the system or provided as an extension to the system. They affect how the user provides keyboard and mouse input to the computer. When enabled, their functionality is available regardless of which applications are running. An example is a keyboard filter that makes it easier for users with movement impairments to type key combinations such as CTRL+ALT+DEL.

Each accessibility parameter and each built-in accessibility feature corresponds to a system parameter that can be set or queried with the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function.

## Related topics

<dl> <dt>

[Windows Accessibility Features](windows-accessibility-features.md)
</dt> <dt>

[Security Considerations for Assistive Technologies](uiauto-securityoverview.md)
</dt> </dl>

 

 




