---
description: Private properties are used internally by the installer and their values must be entered into the database by the author of the installation package or set by the installer during the installation to values determined by the operating environment.
ms.assetid: 7d574bf0-bcb3-4e19-9659-fe741ace9f21
title: Private Properties
ms.topic: article
ms.date: 05/31/2018
---

# Private Properties

Private properties are used internally by the installer and their values must be entered into the database by the author of the installation package or set by the installer during the installation to values determined by the operating environment. The only way a user can interact with private properties is through [Control Events](control-events.md) in the package's authored user interface. Private property names must include lowercase letters. See [Restrictions on Property Names](restrictions-on-property-names.md).

Private properties commonly describe the operating environment. For example, if the installation is run on a Windows platform, the installer sets the [**WindowsFolder**](windowsfolder.md) property to the value specified in the Property table.

Private property values cannot be overridden at a command line. To clear a private property from an installation, leave it out of the [Property table](property-table.md). On Windows XP, and Windows 2000 you cannot set a private property in the user interface phase of the installation and then pass the value to the execution phase.

For a list of all the standard private properties used by the installer, see [Property Reference](property-reference.md). You can define a custom private property by entering the property's name and initial value in the Property table. Private property names must always include lowercase letters.

## Related topics

<dl> <dt>

[Public Properties](public-properties.md)
</dt> </dl>

 

 



