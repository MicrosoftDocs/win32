---
description: Windows Installer can configure software installation by using the values of variables defined in an installation package or by the user.
ms.assetid: b7b715e7-e92c-4b84-b60d-a0ff8412749b
title: About Properties
ms.topic: article
ms.date: 05/31/2018
---

# About Properties

Windows Installer can configure software installation by using the values of variables defined in an installation package or by the user.

Windows Installer uses three categories of global variables during an installation:

-   Private properties: The installer uses private properties internally and their values must be authored into the installation database or set to values determined by the operating environment.
-   Public properties: Public properties can be authored into the database and changed by a user or system administrator on the command line, by applying a transform, or by interacting with an authored user interface.
-   Restricted public properties: For security purposes, the author of an installation package can restrict the public properties a user can change.

Not all properties need to be defined in every package, there is a small set of required properties that must be defined in every package. The installer sets the values of properties in a particular order of precedence.

[Private Properties](private-properties.md)

[Public Properties](public-properties.md)

[Restricted Public Properties](restricted-public-properties.md)

[Required Properties](required-properties.md)

[Order of Property Precedence](order-of-property-precedence.md)

## Related topics

<dl> <dt>

[Using Properties](using-properties.md)
</dt> <dt>

[Property Reference](property-reference.md)
</dt> </dl>

 

 



