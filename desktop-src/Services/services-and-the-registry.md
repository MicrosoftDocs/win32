---
description: A service should not access HKEY\_CURRENT\_USER or HKEY\_CLASSES\_ROOT, especially when impersonating a user. Instead, use the RegOpenCurrentUser or RegOpenUserClassesRoot function.
ms.assetid: 8ad6c081-7ac0-4557-88dc-d8f1ec139926
title: Services and the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Services and the Registry

A service should not access **HKEY\_CURRENT\_USER** or **HKEY\_CLASSES\_ROOT**, especially when impersonating a user. Instead, use the [**RegOpenCurrentUser**](/windows/desktop/api/winreg/nf-winreg-regopencurrentuser) or [**RegOpenUserClassesRoot**](/windows/desktop/api/winreg/nf-winreg-regopenuserclassesroot) function.

If you attempt to access **HKEY\_CURRENT\_USER** or **HKEY\_CLASSES\_ROOT** from a service it may fail, or it may appear to work but there is an underlying leak that can lead to problems loading or unloading the user profile.

 

 
