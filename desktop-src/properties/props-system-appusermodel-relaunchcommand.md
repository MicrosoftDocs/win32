---
Description: Specifies a command that can be executed through ShellExecute to launch an application when it is pinned to the taskbar or when a new instance of the application is launched through the applications Jump List.
ms.assetid: 83aab060-0629-48e3-a2db-9ba96a8631e5
title: System.AppUserModel.RelaunchCommand
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.AppUserModel.RelaunchCommand

Specifies a command that can be executed through [**ShellExecute**](shell.ShellExecute) to launch an application when it is pinned to the taskbar or when a new instance of the application is launched through the application's Jump List.

Examples include the following:


```
shell:::{ED228FDF-9EA8-4870-83B1-96B02CFE0D52}

virtualhost.exe /virtualapp:12345

notepad.exe
```



This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](shell.props_System_AppUserModel_Id), set through [**SHGetPropertyStoreForWindow**](/windows/win32/Shellapi/nf-shellapi-shgetpropertystoreforwindow?branch=master)). If the window does not have an explicit AppUserModelID, this property is ignored and the window is grouped and pinned as if it were part of the process that owns it. For more information about the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](shell.AppIDs).

This property is meant to be used by applications or windows that want to provide non-default relaunch information.

> [!Note]  
> [System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand) and [System.AppUserModel.RelaunchDisplayNameResource](shell.props_System_AppUserModel_RelaunchDisplayNameResource) must always be set together. If one of those properties is not set, then neither is used.

 

This property, together with [System.AppUserModel.RelaunchDisplayNameResource](shell.props_System_AppUserModel_RelaunchDisplayNameResource) and [System.AppUserModel.RelaunchIconResource](shell.props_System_AppUserModel_RelaunchIconResource) can be used to visually define a window as an application to the user. This is useful for host application scenarios, where a single host instance runs multiple child applications. For example, a virtual machine that hosts several virtualized applications might want those virtualized applications to appear as individual applications to the user. The virtual machine could label each window with an explicit AppUserModelID and the appropriate relaunch properties to make them appear as applications. The user could then pin them to the taskbar and "relaunch" the pinned instance.

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](shell.props_System_AppUserModel_PreventPinning) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/win32/Shellapi/nf-shellapi-shgetpropertystoreforwindow?branch=master) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](shell.IPropertyStore) object to set the [System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand) property of that window.

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

[Application User Model IDs (AppUserModelIDs)](shell.AppIDs)
</dt> <dt>

[System.AppUserModel.ID](shell.props_System_AppUserModel_Id)
</dt> <dt>

[propertyDescriptionList](shell.propdesc_schema_propertyDescriptionList)
</dt> <dt>

[propertyDescription](shell.propdesc_schema_propertyDescription)
</dt> <dt>

[searchInfo](shell.propdesc_schema_searchInfo)
</dt> <dt>

[labelInfo](shell.propdesc_schema_labelInfo)
</dt> <dt>

[typeInfo](shell.propdesc_schema_typeInfo)
</dt> <dt>

[displayInfo](shell.propdesc_schema_displayInfo)
</dt> <dt>

[aliasInfo](shell.propdesc_schema_aliasInfo)
</dt> <dt>

[stringFormat](shell.propdesc_schema_stringFormat)
</dt> <dt>

[booleanFormat](shell.propdesc_schema_booleanFormat)
</dt> <dt>

[numberFormat](shell.propdesc_schema_numberFormat)
</dt> <dt>

[dateTimeFormat](shell.propdesc_schema_dateTimeFormat)
</dt> <dt>

[enumeratedList](shell.propdesc_schema_enumeratedList)
</dt> <dt>

[enum](shell.propdesc_schema_enum)
</dt> <dt>

[enumRange](shell.propdesc_schema_enumRange)
</dt> <dt>

[image](shell.propdesc_schema_image)
</dt> <dt>

[drawControl](shell.propdesc_schema_drawControl)
</dt> <dt>

[editControl](shell.propdesc_schema_editControl)
</dt> <dt>

[filterControl](shell.propdesc_schema_filterControl)
</dt> <dt>

[queryControl](shell.propdesc_schema_queryControl)
</dt> <dt>

[relatedPropertyInfo](shell.propdesc_schema_relatedPropertyInfo)
</dt> <dt>

[relatedProperty](shell.propdesc_schema_relatedProperty)
</dt> </dl>

 

 



