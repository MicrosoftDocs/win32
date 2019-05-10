---
title: Windows Accessibility Features
description: Windows Accessibility supports two categories of features for Windows developers - Win32 APIs and User Settings.
ms.assetid: 823bbc5b-062b-43ef-9f3e-822dc6f55c5d
ms.topic: article
ms.date: 05/31/2018
---

# Windows Accessibility Features

Windows Accessibility supports two categories of features for Windows developers designing accessible applications, assistive technology developers building tools such as screen readers and magnifiers, and software test engineers creating automated scripts for testing Windows applications.

## Win32 APIs

The Win32 API includes a set of accessibility features that help developers build apps that can be used by as many people as possible, including those with disabilities, personal preferences, and specific work styles.

## Settings

There are two types of settings available to users (through the Ease of Access Center in Control Panel) that are also exposed to developers:

- [Accessibility parameters](accessibility-parameters.md). When set, these parameters indicate that applications should change their default behavior. Applications can check the state of an accessibility parameter to determine whether the user wants special behavior that can be provided in an application-specific manner. For example, the ShowSounds parameter indicates that an application that typically uses sound to convey important information should also provide the information visually.
- [Built-in accessibility features](built-in-accessibility-features.md). These features are built into the system or provided as an extension to the system. They affect how the user provides keyboard and mouse input to the computer. When enabled, their functionality is available regardless of which applications are running. An example is a keyboard filter that makes it easier for users with movement impairments to type key combinations such as CTRL+ALT+DEL.

Each accessibility parameter and each built-in accessibility feature corresponds to a system parameter that can be set or queried with the [SystemParametersInfo](https://msdn.microsoft.com/library/windows/desktop/ms724947) function.

## Related topics

[Security Considerations for Assistive Technologies](uiauto-securityoverview.md)
