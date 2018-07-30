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
> [System.AppUserModel.RelaunchCommand](https://msdn.microsoft.com/library/Dd391571(v=VS.85).aspx) and [System.AppUserModel.RelaunchDisplayNameResource](https://msdn.microsoft.com/library/Dd391572(v=VS.85).aspx) must always be set together. If one of those properties is not set, then neither is used.

 

This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx), set through [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)). If the window does not have an explicit AppUserModelID, this property is ignored and the window is grouped and pinned as if it were part of the process that owns it. For more information on the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx). This property is meant to be used by applications or windows that want to provide non-default relaunch information. For more information, see [System.AppUserModel.RelaunchCommand](https://msdn.microsoft.com/library/Dd391571(v=VS.85).aspx).

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](https://msdn.microsoft.com/library/Dd561983(v=VS.85).aspx) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx) object to set the [System.AppUserModel.RelaunchDisplayNameResource](https://msdn.microsoft.com/library/Dd391572(v=VS.85).aspx) property of that window.

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

 

 



