---
title: Pointer-Attribute Type Inheritance
description: According to the DCE specification, each IDL file must define attributes for its pointers.
ms.assetid: ab8821ce-d52a-42bf-aa5e-582bb24adf93
ms.topic: article
ms.date: 05/31/2018
---

# Pointer-Attribute Type Inheritance

According to the DCE specification, each IDL file must define attributes for its pointers. If an explicit attribute is not assigned to a pointer, the pointer uses the value specified by the \[ [pointer\_default](/windows/desktop/Midl/pointer-default)\] keyword. Some DCE implementations do not allow unattributed pointers. If a pointer does not have an explicit attribute, the IDL file must have a **\[pointer\_default\]** specification so that the pointer attribute can be set.

In default (Microsoft-extensions) mode, you can specify a pointer's attribute in the IDL file that imports the defining IDL file. Pointers defined in one IDL file can inherit attributes that are specified in other IDL files. Also, in default mode, IDL files can include unattributed pointers. If neither the base nor the imported IDL files specify a pointer attribute or **\[pointer\_default\]**, unattributed pointers are interpreted as unique pointers.

The MIDL compiler assigns pointer attributes to pointers using the following priority rules (1 is highest).



| Priority | Description                                                                                                                |
|----------|----------------------------------------------------------------------------------------------------------------------------|
| 1        | Explicit pointer attributes are applied to the pointer at the definition or use site.                                      |
| 2        | The default is the **\[pointer\_default\]** attribute in the IDL file that defines the type.                               |
| 3        | The default is the **\[pointer\_default\]** attribute in the IDL file that imports the type.                               |
| 4        | The default is \[ [ptr](/windows/desktop/Midl/ptr)\] in DCE-compatibility mode, or \[ [unique](/windows/desktop/Midl/unique)\] in Microsoft-extensions mode. |



 

 

 