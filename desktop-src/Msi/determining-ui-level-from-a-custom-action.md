---
description: A custom action in a UI sequence table or an external executable file may need the current user interface level of the installation.
ms.assetid: d1ddadd5-b4ec-4c7c-aee4-b2d688a57eb4
title: Determining UI Level from a Custom Action
ms.topic: article
ms.date: 05/31/2018
---

# Determining UI Level from a Custom Action

A custom action in a UI sequence table or an external executable file may need the current user interface level of the installation. For example, a custom action that has a dialog box should only display the dialog when the user interface level is Full UI or Reduced UI, it should not display the dialog if the user interface level is Basic UI or None. You should use the [**UILevel**](uilevel.md) property to determine the current user interface level. You cannot call [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui) from a custom action and it is not possible to change the UI level property from within a custom action.

It is recommended that custom actions not use the UI level as a condition for sending error messages to the installer because this can interfere with logging and external messages.

 

 



