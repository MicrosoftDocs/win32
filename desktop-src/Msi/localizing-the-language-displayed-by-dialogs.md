---
description: The Windows Installer service uses the current user's language in all dialogs until a Windows Installer package is opened.
ms.assetid: c9902990-7a26-48fd-96ac-4d5a749e34be
title: Localizing the Language Displayed by Dialogs
ms.topic: article
ms.date: 05/31/2018
---

# Localizing the Language Displayed by Dialogs

The Windows Installer service uses the current user's language in all dialogs until a Windows Installer package is opened. The Windows Installer determines this by using **GetUserDefaultUILanguage**. When a Windows Installer package is opened, the installer displays dialogs using the package's language as specified by the [**Template Summary**](template-summary.md) Property.

For more information about localizing the language of a Windows Installer package, see also [A Localization Example](a-localization-example.md).

 

 



