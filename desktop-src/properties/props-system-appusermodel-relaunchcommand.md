---
Description: Specifies a command that can be executed through ShellExecute to launch an application when it is pinned to the taskbar or when a new instance of the application is launched through the application's Jump List.
ms.assetid: 83aab060-0629-48e3-a2db-9ba96a8631e5
title: System.AppUserModel.RelaunchCommand
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.RelaunchCommand

Specifies a command that can be executed through [**ShellExecute**](https://msdn.microsoft.com/en-us/library/Bb762153(v=VS.85).aspx) to launch an application when it is pinned to the taskbar or when a new instance of the application is launched through the application's Jump List.

Examples include the following:


```
shell:::{ED228FDF-9EA8-4870-83B1-96B02CFE0D52}

virtualhost.exe /virtualapp:12345

notepad.exe
```



This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID), set through [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)). If the window does not have an explicit AppUserModelID, this property is ignored and the window is grouped and pinned as if it were part of the process that owns it. For more information about the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx).

This property is meant to be used by applications or windows that want to provide non-default relaunch information.

> [!Note]  
> [System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand) and [System.AppUserModel.RelaunchDisplayNameResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchDisplayNameResource) must always be set together. If one of those properties is not set, then neither is used.

 

This property, together with [System.AppUserModel.RelaunchDisplayNameResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchDisplayNameResource) and [System.AppUserModel.RelaunchIconResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchIconResource) can be used to visually define a window as an application to the user. This is useful for host application scenarios, where a single host instance runs multiple child applications. For example, a virtual machine that hosts several virtualized applications might want those virtualized applications to appear as individual applications to the user. The virtual machine could label each window with an explicit AppUserModelID and the appropriate relaunch properties to make them appear as applications. The user could then pin them to the taskbar and "relaunch" the pinned instance.

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](https://www.bing.com/search?q=System.AppUserModel.PreventPinning) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) object to set the [System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand) property of that window.

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

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx)
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

 

 



