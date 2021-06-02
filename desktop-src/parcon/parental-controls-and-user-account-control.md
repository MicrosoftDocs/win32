---
description: Parental Controls and User Account Control
ms.assetid: dc7c322a-f534-4dda-8c62-aa628a7b91bc
title: Parental Controls and User Account Control
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls and User Account Control

User Account Control (UAC) will result in presence of Protected Administrator and Standard User accounts. A Protected Administrator will run with the same rights as a Standard User under normal usage. For privileged operations:

-   A Standard User will be shown the Credentials User Interface dialog box, which requires the input of a user name and password for a Protected Administrator or built-in Administrator.
-   A Protected Administrator will be shown the Consent User Interface dialog box, which requires selection of Allow to proceed.

It is important to note that UAC is implemented on a per-process basis, so a process either runs elevated or not. Generally, it is not suitable from a security standpoint to run large applications as always elevated. For Parental Controls, code that must modify settings should be isolated by one of two implementation options:

1.  Create a small executable for settings management that is marked in its manifest as requiring administrative rights. Invocation of the executable will cause the Consent or Credentials UI to be shown prior to allowing the process to run.
2.  Provide COM interfaces in a product DLL that allow for invocation per UAC documentation. This will also cause the appropriate Consent or Credentials UI to be shown.

 

 



