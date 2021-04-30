---
description: Control Panel items must be registered in order to appear in the Control Panel window.
title: Registering Control Panel Items
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 6f21f223-a293-47b5-95e9-06b7a4ff1652
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Registering Control Panel Items

Control Panel items must be registered in order to appear in the Control Panel window. If the Control Panel item is implemented as part of a .exe file then it is registered as a command object. Registration differs if the item is implemented as a .dll file that exports the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function.

Specific requirements are discussed in these topics:

-   [How To Register Executable Control Panel Items](how-to-register-an-executable-control-panel-item-registration-.md)
-   [How To Register DLL Control Panel Items](how-to-register-dll-control-panel-item-registration-.md)

## Related topics

<dl> <dt>

[Control Panel Items](control-panel-applications.md)
</dt> <dt>

[User Experience Guidelines](user-experience-guidelines.md)
</dt> <dt>

[Using CPLApplet](using-cplapplet.md)
</dt> <dt>

[Control Panel Message Processing](message-processing.md)
</dt> <dt>

[Executing Control Panel Items](executing-control-panel-items.md)
</dt> <dt>

[Extending System Control Panel Items](extending-system-control-panel-items.md)
</dt> <dt>

[Assigning Control Panel Categories](assigning-control-panel-categories.md)
</dt> <dt>

[Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md)
</dt> <dt>

[Accessing the Control Panel in Safe Mode under Windows Vista](accessing-the-cp-in-safe-mode-under-vista.md)
</dt> </dl>

 

 
