---
Description: Specifies the display name used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List.
ms.assetid: a149838b-83b6-44ce-b705-e2804efb3d31
title: System.AppUserModel.RelaunchDisplayNameResource
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.RelaunchDisplayNameResource

Specifies the display name used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List. The value of this property must be one of the following:

-   An indirect resource string such as "@%systemdir%\\system32\\shell32.dll,-19263". Note that the '@' character is required to distinguish an indirect string from a plain-text string (described in the next bulleted paragraph). This indirect string consists of a binary file and a resource ID of the string contained in that binary. We strongly recommend that you use this indirect string form, which ensures that the display name changes appropriately when the system language is changed through the Multilingual User Interface (MUI). The '-' character before the resource ID is required.
-   A plain-text string that does not point to a resource. This should only be used when the display name is dynamically calculated or obtained from a data source that does not support MUI. For example, the string could be the name of a device, such as "Microsoft Zune", in cases where the application appears when that device is attached to the computer.

> [!Note]  
> [System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand) and [System.AppUserModel.RelaunchDisplayNameResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchDisplayNameResource) must always be set together. If one of those properties is not set, then neither is used.

 

This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID), set through [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)). If the window does not have an explicit AppUserModelID, this property is ignored and the window is grouped and pinned as if it were part of the process that owns it. For more information on the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/ebce2d99-6f20-4545-9f12-d79cd8d0828f). This property is meant to be used by applications or windows that want to provide non-default relaunch information. For more information, see [System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand).

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](https://www.bing.com/search?q=System.AppUserModel.PreventPinning) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) object to set the [System.AppUserModel.RelaunchDisplayNameResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchDisplayNameResource) property of that window.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.RelaunchDisplayNameResource
   shellPKey = PKEY_AppUserModel_RelaunchDisplayNameResource
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 4
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = String
      IsInnate = false
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/ebce2d99-6f20-4545-9f12-d79cd8d0828f)
</dt> <dt>

[System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID)
</dt> <dt>

[propertyDescriptionList](https://www.bing.com/search?q=propertyDescriptionList)
</dt> <dt>

[propertyDescription](https://www.bing.com/search?q=propertyDescription)
</dt> <dt>

[searchInfo](https://www.bing.com/search?q=searchInfo)
</dt> <dt>

[labelInfo](https://www.bing.com/search?q=labelInfo)
</dt> <dt>

[typeInfo](https://www.bing.com/search?q=typeInfo)
</dt> <dt>

[displayInfo](https://www.bing.com/search?q=displayInfo)
</dt> <dt>

[aliasInfo](https://www.bing.com/search?q=aliasInfo)
</dt> <dt>

[stringFormat](https://www.bing.com/search?q=stringFormat)
</dt> <dt>

[booleanFormat](https://www.bing.com/search?q=booleanFormat)
</dt> <dt>

[numberFormat](https://www.bing.com/search?q=numberFormat)
</dt> <dt>

[dateTimeFormat](https://www.bing.com/search?q=dateTimeFormat)
</dt> <dt>

[enumeratedList](https://www.bing.com/search?q=enumeratedList)
</dt> <dt>

[enum](https://www.bing.com/search?q=enum)
</dt> <dt>

[enumRange](https://www.bing.com/search?q=enumRange)
</dt> <dt>

[image](https://www.bing.com/search?q=image)
</dt> <dt>

[drawControl](https://www.bing.com/search?q=drawControl)
</dt> <dt>

[editControl](https://www.bing.com/search?q=editControl)
</dt> <dt>

[filterControl](https://www.bing.com/search?q=filterControl)
</dt> <dt>

[queryControl](https://www.bing.com/search?q=queryControl)
</dt> <dt>

[relatedPropertyInfo](https://www.bing.com/search?q=relatedPropertyInfo)
</dt> <dt>

[relatedProperty](https://www.bing.com/search?q=relatedProperty)
</dt> </dl>

 

 



