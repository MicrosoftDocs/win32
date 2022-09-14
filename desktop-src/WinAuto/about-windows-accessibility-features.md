---
title: Windows Accessibility features
description: Windows Accessibility supports two categories of features for Windows developers - Win32 APIs and User Settings.
ms.assetid: 823bbc5b-062b-43ef-9f3e-822dc6f55c5d
ms.topic: article
ms.date: 05/31/2018
---

# Windows Accessibility features

Windows Accessibility supports two categories of features to help Windows developers design accessible applications, assistive technology developers build tools such as screen readers and magnifiers, and software test engineers create automated scripts for testing Windows applications.

## Settings

There are two types of settings available to users (through the Ease of Access Center in Control Panel) that are also exposed to developers:

- [Accessibility parameters](accessibility-parameters.md). When set, these parameters indicate that applications should change their default behavior. Applications can check the state of an accessibility parameter to determine whether the user wants special behavior that can be provided in an application-specific manner. For example, the ShowSounds parameter indicates that an application that typically uses sound to convey important information should also provide the information visually.
- [Built-in accessibility features](built-in-accessibility-features.md). These features are built into the system or provided as an extension to the system. They affect how the user provides keyboard and mouse input to the computer. When enabled, their functionality is available regardless of which applications are running. An example is a keyboard filter that makes it easier for users with movement impairments to type key combinations such as CTRL+ALT+DEL.

Each accessibility parameter and each built-in accessibility feature corresponds to a system parameter that can be set or queried with the [SystemParametersInfo](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function.

## Win32 APIs

The Win32 APIs provide accessibility and automation features to help developers build applications and UI frameworks, assistive technology vendors build tools, testers ensure quality implementations, and people with disabilities use their computers and devices.

## Related topics

[Security Considerations for Assistive Technologies](uiauto-securityoverview.md)