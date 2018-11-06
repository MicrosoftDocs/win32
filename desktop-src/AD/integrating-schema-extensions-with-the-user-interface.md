---
title: Integrating Schema Extensions with the User Interface
description: The administration tools of Active Directory Domain Services use a common architecture for connecting the administrative user interface to the directory schema.
ms.assetid: 62cf9f9d-7091-4cff-9995-5934dfa3e97e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Integrating Schema Extensions with the User Interface

The administration tools of Active Directory Domain Services use a common architecture for connecting the administrative user interface to the directory schema. The centerpiece of this architecture is the **displaySpecifier** object class. Display specifiers and their usage are described in detail in [Extending the User Interface for Directory Objects](extending-the-user-interface-for-directory-objects.md).

When you create a new class by subclassing an existing class, you can leverage the existing UI for the superclass by copying the superclass' display specifier. An easy way to copy the display specifier for a class is to export it into an LDIF file using LDIFDE, edit the Distinguished name and CN, then import the modified LDIF file. If the subclass has additional attributes, you will need to provide additional property pages to support editing. If the subclass has additional must-have properties, you will need to provide Creation Dialog extension pages since the UI provided by the superclass has no way to create these new attributes.

 

 




