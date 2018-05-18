---
Description: 'Specifies the icon used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button''s Jump List.'
ms.assetid: '3559d1f5-988c-41d9-ba9a-dfa4ba643ee2'
title: 'System.AppUserModel.RelaunchIconResource'
---

# System.AppUserModel.RelaunchIconResource

Specifies the icon used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List. This is the icon used for the taskbar group and is shown for a pinned application whether that application is running or not. This should be specified in one of the following formats:

-   Standard resource format, such as "%systemdir%\\system32\\shell32.dll,-128". The '-' character before the resource ID is required. Do not use the '@' character at the front of the path string.
-   Direct path to an icon file, such as "%programfiles%\\Microsoft\\Notepad\\Notepad.ico,0". Note that because .ico files can contain multiple icon resources, a resource ID is required in the string. If the .ico file is a single image, use "0" (without the '-' character) as the resource ID.

[System.AppUserModel.RelaunchIconResource](shell.props_System_AppUserModel_RelaunchIconResource) is an optional property. If it is not set, the icon of the target of the relaunch command ([System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand)) is used. However, because that can lead to undesired results, we strongly encourage you to provide an icon explicitly through this property.

This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](shell.props_System_AppUserModel_Id), set through [**SHGetPropertyStoreForWindow**](shgetpropertystoreforwindow.md)). If the window does not have an explicit AppUserModelID (System.AppUserModel.ID), this property is ignored and the window is grouped and pinned as if it were part of its owning process. For more information on the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](shell.AppIDs). This property is meant to be used by applications or windows that want to provide non-default relaunch information. For more information, see [System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand).

If an explicit AppUserModelID is set on the window, but this property is not set, the system attempts to find a shortcut with the same AppUserModelID, and pins that shortcut to the taskbar to represent the window. If no such shortcut can be located, then the backing executable of the process that owns it is used.

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](shell.props_System_AppUserModel_PreventPinning) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](shgetpropertystoreforwindow.md) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](shell.IPropertyStore) object to set the [System.AppUserModel.RelaunchIconResource](shell.props_System_AppUserModel_RelaunchIconResource) property of that window.

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

 

 



