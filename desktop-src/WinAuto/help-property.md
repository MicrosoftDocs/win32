---
title: Help Property
description: The Help property provides information that tells the user about the function of an object.
ms.assetid: 3df0cc01-cc99-42a1-9d56-591e6e00e53d
ms.topic: article
ms.date: 05/31/2018
---

# Help Property

The **Help** property provides information that tells the user about the function of an object.

The **Help** property is retrieved by calling [**IAccessible::get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp).

This property contains balloon-style information (as found in ToolTips) that is used either to describe what the object does or how to use it. For example, the **Help** property for a toolbar button that shows a printer might provide the following text: "Prints the current document."

The text for the **Help** property does not have to be unique within the user interface.

## When to Support the Help Property

Servers do not support the **Help** property if other properties provide sufficient information about the object's purpose and the actions the object performs. Accessible objects that expose system-provided controls do not support the **Help** property.

 

 




