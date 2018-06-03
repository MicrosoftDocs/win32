---
Description: Specifies the icon used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List.
ms.assetid: 3559d1f5-988c-41d9-ba9a-dfa4ba643ee2
title: System.AppUserModel.RelaunchIconResource
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.RelaunchIconResource

Specifies the icon used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List. This is the icon used for the taskbar group and is shown for a pinned application whether that application is running or not. This should be specified in one of the following formats:

-   Standard resource format, such as "%systemdir%\\system32\\shell32.dll,-128". The '-' character before the resource ID is required. Do not use the '@' character at the front of the path string.
-   Direct path to an icon file, such as "%programfiles%\\Microsoft\\Notepad\\Notepad.ico,0". Note that because .ico files can contain multiple icon resources, a resource ID is required in the string. If the .ico file is a single image, use "0" (without the '-' character) as the resource ID.

[System.AppUserModel.RelaunchIconResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchIconResource) is an optional property. If it is not set, the icon of the target of the relaunch command ([System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand)) is used. However, because that can lead to undesired results, we strongly encourage you to provide an icon explicitly through this property.

This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID), set through [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)). If the window does not have an explicit AppUserModelID (System.AppUserModel.ID), this property is ignored and the window is grouped and pinned as if it were part of its owning process. For more information on the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/windows/desktop/ebce2d99-6f20-4545-9f12-d79cd8d0828f). This property is meant to be used by applications or windows that want to provide non-default relaunch information. For more information, see [System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand).

If an explicit AppUserModelID is set on the window, but this property is not set, the system attempts to find a shortcut with the same AppUserModelID, and pins that shortcut to the taskbar to represent the window. If no such shortcut can be located, then the backing executable of the process that owns it is used.

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](https://www.bing.com/search?q=System.AppUserModel.PreventPinning) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) object to set the [System.AppUserModel.RelaunchIconResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchIconResource) property of that window.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1

```
propertyDescription
   name = System.AppUserModel.RelaunchIconResource
   shellPKey = PKEY_AppUserModel_RelaunchIconResource
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 3
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = String
      IsInnate = false
```

## Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.RelaunchIconResource
   shellPKey = PKEY_AppUserModel_RelaunchIconResource
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 3
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = String
      IsInnate = false
```

## Related topics

<dl> <dt>

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/windows/desktop/ebce2d99-6f20-4545-9f12-d79cd8d0828f)
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

 

 



