---
title: UI_PKEY_QuickAccessToolbarDock
description: Identifies the UI\_PKEY\_QuickAccessToolbarDock property.
ms.assetid: 77f7b0a8-f276-4501-9d53-fb5a3185edcc
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_QuickAccessToolbarDock

Identifies the UI\_PKEY\_QuickAccessToolbarDock property.

```
propertyDescription
   name = UI_PKEY_QuickAccessToolbarDock
   shellPKey = UI_PKEY_QuickAccessToolbarDock
   formatID = 00001002-7363-696e-8441798acf5aebb7
   propID = 1002
   typeInfo
      type = UI_CONTROLDOCK
```

## Remarks

UI\_PKEY\_QuickAccessToolbarDock is used by an application to query the dock-state of the Quick Access Toolbar (QAT).

The property value is from the [**UI\_CONTROLDOCK**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_controldock) enumeration.



|    Enumeration                     |    Description                                                                                                                                                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UI\_CONTROLDOCK\_TOP    | The QAT is docked in the nonclient area of the Ribbon host application, as shown in the following screen shot.![screen shot of the quick access toolbar docked above the ribbon in the nonclient area.](images/properties/qat-docktop.png)<br/> |
| UI\_CONTROLDOCK\_BOTTOM | The QAT is docked as a visually integral band below the Ribbon, as shown in the following screen shot. ![screen shot of the quick access toolbar docked below the ribbon.](images/properties/qat-dockbottom.png)<br/>                           |



 

## Related topics

<dl> <dt>

[Ribbon Properties](windowsribbon-reference-properties-ribbon.md)
</dt> </dl>

 

