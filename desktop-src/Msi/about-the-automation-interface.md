---
description: An Installer object must be created initially to load the automation support required to access the installer components through COM.
ms.assetid: 113ed443-a866-43d4-86bd-fc3b244f2edb
title: About the Automation Interface
ms.topic: article
ms.date: 05/31/2018
---

# About the Automation Interface

An [**Installer object**](installer-object.md) must be created initially to load the automation support required to access the installer components through COM. This object provides wrappers to create the top-level objects and access their methods. These wrappers simply provide parameter translations to expose the installer functions in a manner consistent with Microsoft Visual Basic without changing the behavior of the methods.

Whenever possible, a pair of Get and Set C++ methods are exposed to Visual Basic as a single property. In some cases C++ methods taking an index argument are exposed as an indexed property. Many C++ methods return the result through a parameter because the return value is used for the error return. However, in Visual Basic, errors are handled by a separate mechanism, and the result is always passed in the return value.

For information about using automation and creating the Installer object, see [Using the Automation Interface](using-the-automation-interface.md).

For reference material for the Windows Installer objects, see [Automation Interface Reference](automation-interface-reference.md).

## Related topics

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 



