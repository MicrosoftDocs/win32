---
description: By default, as of Windows Vista Control Panel items are not shown when Windows is run in safe mode.
title: Accessing the Control Panel in Safe Mode
ms.topic: article
ms.date: 05/31/2018
ms.assetid: f37bcb0f-9417-4cc4-a57d-4f67a9ccda19
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Accessing the Control Panel in Safe Mode

By default, as of Windows Vista Control Panel items are not shown when Windows is run in safe mode. To allow a new Control Panel item to be viewed in safe mode, registry values appropriate to the item type can be set. The values are interpreted as follows:



| Value | Meaning                                                            |
|-------|--------------------------------------------------------------------|
| 1     | The item should appear in minimal safe mode only.                  |
| 2     | The item should appear in safe mode only if networking is enabled. |
| 3     | The item should always appear in any form of safe mode.            |



 

This example shows the entries required for an item implemented as a .cpl or .dll file. It specifies that the item should appear in safe mode with networking.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Control Panel
                  Extended Properties
                     System.ControlPanel.EnableInSafeMode
                        %ProgramFiles%\MyCorp\MyApp\MyCpl.cpl = [REG_DWORD] 2
```

This example shows the entries required for an item implemented as a .exe file. It specifies that the item should appear in any form of safe mode.

```
HKEY_CLASSES_ROOT
   CLSID
      {0052D9FC-6764-4D29-A66F-2F3BD9E2BB40}
         System.ControlPanel.EnableInSafeMode = [REG_DWORD] 3
```

## Related topics

<dl> <dt>

[Control Panel Items](control-panel-applications.md)
</dt> <dt>

[User Experience Guidelines](user-experience-guidelines.md)
</dt> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
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
</dt> </dl>

 

 



