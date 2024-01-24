---
description: Public properties can be authored into the installation database in the same way as private properties.
ms.assetid: 032aa55f-d97a-4455-bd32-571b0e05763b
title: Public Properties
ms.topic: article
ms.date: 05/31/2018
---

# Public Properties

Public properties can be authored into the installation database in the same way as [private properties](private-properties.md). In addition, the values of public properties can be changed by a user or system administrator by setting the property on the command line, by applying a transform, or by interacting with an authored user interface. Public property names cannot contain lowercase letters. See [Restrictions on Property Names](restrictions-on-property-names.md).

Public properties are commonly set by users during the installation. For example, the public property [**INSTALLLEVEL**](installlevel.md) property can be specified at the command line used to launch the installation or chosen by using an authored user interface.

Public property values can be overridden either at a command line, by using a [standard](standard-actions.md) or [custom](custom-actions.md) action, by applying a transform, or by having the user interact with an authored user interface. To clear a public property in the property table, leave it out of the table. Properties that are to be set by the user interface during the installation and then passed to the execution phase of the installation must be public.

For a list of the standard public properties used by the installer see [Property Reference](property-reference.md). An author can also define a custom public property by entering the property's name and an initial value into the [Property table](property-table.md). All public properties can be overridden by all users if any of the following conditions are true.

-   The user is a system administrator.
-   The per-machine EnableUserControl policy is set to 1. See [System Policy](system-policy.md).
-   The [**EnableUserControl**](-enableusercontrol.md) property is set to 1.
-   This is an unmanaged installation that is not being done with elevated privileges.

If none of the above conditions are true, the installer defaults to limiting which public properties can be overridden by a user that is not a system administrator. See [**Restricted Public Properties**](restricted-public-properties.md).

 

 



