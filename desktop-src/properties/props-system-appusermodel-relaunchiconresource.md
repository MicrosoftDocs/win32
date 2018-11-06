---
Description: Specifies the icon used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List.
ms.assetid: 3559d1f5-988c-41d9-ba9a-dfa4ba643ee2
title: System.AppUserModel.RelaunchIconResource
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.RelaunchIconResource

Specifies the icon used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List. This is the icon used for the taskbar group and is shown for a pinned application whether that application is running or not. This should be specified in one of the following formats:

-   Standard resource format, such as "%systemdir%\\system32\\shell32.dll,-128". The '-' character before the resource ID is required. Do not use the '@' character at the front of the path string.
-   Direct path to an icon file, such as "%programfiles%\\Microsoft\\Notepad\\Notepad.ico,0". Note that because .ico files can contain multiple icon resources, a resource ID is required in the string. If the .ico file is a single image, use "0" (without the '-' character) as the resource ID.

[System.AppUserModel.RelaunchIconResource](https://msdn.microsoft.com/library/Dd391573(v=VS.85).aspx) is an optional property. If it is not set, the icon of the target of the relaunch command ([System.AppUserModel.RelaunchCommand](https://msdn.microsoft.com/library/Dd391571(v=VS.85).aspx)) is used. However, because that can lead to undesired results, we strongly encourage you to provide an icon explicitly through this property.

This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx), set through [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)). If the window does not have an explicit AppUserModelID (System.AppUserModel.ID), this property is ignored and the window is grouped and pinned as if it were part of its owning process. For more information on the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx). This property is meant to be used by applications or windows that want to provide non-default relaunch information. For more information, see [System.AppUserModel.RelaunchCommand](https://msdn.microsoft.com/library/Dd391571(v=VS.85).aspx).

If an explicit AppUserModelID is set on the window, but this property is not set, the system attempts to find a shortcut with the same AppUserModelID, and pins that shortcut to the taskbar to represent the window. If no such shortcut can be located, then the backing executable of the process that owns it is used.

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](https://msdn.microsoft.com/library/Dd561983(v=VS.85).aspx) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx) object to set the [System.AppUserModel.RelaunchIconResource](https://msdn.microsoft.com/library/Dd391573(v=VS.85).aspx) property of that window.

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

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx)
</dt> <dt>

[System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx)
</dt> <dt>

[propertyDescriptionList](https://msdn.microsoft.com/library/Bb773882(v=VS.85).aspx)
</dt> <dt>

[propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx)
</dt> <dt>

[searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx)
</dt> <dt>

[labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx)
</dt> <dt>

[typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx)
</dt> <dt>

[displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx)
</dt> <dt>

[aliasInfo](https://msdn.microsoft.com/library/Bb773860(v=VS.85).aspx)
</dt> <dt>

[stringFormat](https://msdn.microsoft.com/library/Bb773886(v=VS.85).aspx)
</dt> <dt>

[booleanFormat](https://msdn.microsoft.com/library/Bb773862(v=VS.85).aspx)
</dt> <dt>

[numberFormat](https://msdn.microsoft.com/library/Bb773877(v=VS.85).aspx)
</dt> <dt>

[dateTimeFormat](https://msdn.microsoft.com/library/Bb773863(v=VS.85).aspx)
</dt> <dt>

[enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx)
</dt> <dt>

[enum](https://msdn.microsoft.com/library/Bb773869(v=VS.85).aspx)
</dt> <dt>

[enumRange](https://msdn.microsoft.com/library/Bb773873(v=VS.85).aspx)
</dt> <dt>

[image](https://msdn.microsoft.com/library/Dd798383(v=VS.85).aspx)
</dt> <dt>

[drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx)
</dt> <dt>

[editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx)
</dt> <dt>

[filterControl](https://msdn.microsoft.com/library/Bb773874(v=VS.85).aspx)
</dt> <dt>

[queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx)
</dt> <dt>

[relatedPropertyInfo](https://msdn.microsoft.com/library/Dd798385(v=VS.85).aspx)
</dt> <dt>

[relatedProperty](https://msdn.microsoft.com/library/Dd798384(v=VS.85).aspx)
</dt> </dl>

 

 



