---
Description: Specifies a command that can be executed through ShellExecute to launch an application when it is pinned to the taskbar or when a new instance of the application is launched through the application's Jump List.
ms.assetid: 83aab060-0629-48e3-a2db-9ba96a8631e5
title: System.AppUserModel.RelaunchCommand
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.RelaunchCommand

Specifies a command that can be executed through [**ShellExecute**](https://msdn.microsoft.com/library/Bb762153(v=VS.85).aspx) to launch an application when it is pinned to the taskbar or when a new instance of the application is launched through the application's Jump List.

Examples include the following:


```
shell:::{ED228FDF-9EA8-4870-83B1-96B02CFE0D52}

virtualhost.exe /virtualapp:12345

notepad.exe
```



This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx), set through [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)). If the window does not have an explicit AppUserModelID, this property is ignored and the window is grouped and pinned as if it were part of the process that owns it. For more information about the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/library/Dd378459(v=VS.85).aspx).

This property is meant to be used by applications or windows that want to provide non-default relaunch information.

> [!Note]  
> [System.AppUserModel.RelaunchCommand](https://msdn.microsoft.com/library/Dd391571(v=VS.85).aspx) and [System.AppUserModel.RelaunchDisplayNameResource](https://msdn.microsoft.com/library/Dd391572(v=VS.85).aspx) must always be set together. If one of those properties is not set, then neither is used.

 

This property, together with [System.AppUserModel.RelaunchDisplayNameResource](https://msdn.microsoft.com/library/Dd391572(v=VS.85).aspx) and [System.AppUserModel.RelaunchIconResource](https://msdn.microsoft.com/library/Dd391573(v=VS.85).aspx) can be used to visually define a window as an application to the user. This is useful for host application scenarios, where a single host instance runs multiple child applications. For example, a virtual machine that hosts several virtualized applications might want those virtualized applications to appear as individual applications to the user. The virtual machine could label each window with an explicit AppUserModelID and the appropriate relaunch properties to make them appear as applications. The user could then pin them to the taskbar and "relaunch" the pinned instance.

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](https://msdn.microsoft.com/library/Dd561983(v=VS.85).aspx) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx) object to set the [System.AppUserModel.RelaunchCommand](https://msdn.microsoft.com/library/Dd391571(v=VS.85).aspx) property of that window.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.RelaunchCommand
   shellPKey = PKEY_AppUserModel_RelaunchCommand
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 2
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

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/library/Dd378459(v=VS.85).aspx)
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

 

 



