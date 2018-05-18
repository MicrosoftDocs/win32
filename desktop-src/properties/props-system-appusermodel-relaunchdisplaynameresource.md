---
Description: 'Specifies the display name used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button''s Jump List.'
ms.assetid: 'a149838b-83b6-44ce-b705-e2804efb3d31'
title: 'System.AppUserModel.RelaunchDisplayNameResource'
---

# System.AppUserModel.RelaunchDisplayNameResource

Specifies the display name used for the shortcut created on the taskbar when the user chooses to pin an application to the taskbar or launch a new instance through its button's Jump List. The value of this property must be one of the following:

-   An indirect resource string such as "@%systemdir%\\system32\\shell32.dll,-19263". Note that the '@' character is required to distinguish an indirect string from a plain-text string (described in the next bulleted paragraph). This indirect string consists of a binary file and a resource ID of the string contained in that binary. We strongly recommend that you use this indirect string form, which ensures that the display name changes appropriately when the system language is changed through the Multilingual User Interface (MUI). The '-' character before the resource ID is required.
-   A plain-text string that does not point to a resource. This should only be used when the display name is dynamically calculated or obtained from a data source that does not support MUI. For example, the string could be the name of a device, such as "Microsoft Zune", in cases where the application appears when that device is attached to the computer.

> [!Note]  
> [System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand) and [System.AppUserModel.RelaunchDisplayNameResource](shell.props_System_AppUserModel_RelaunchDisplayNameResource) must always be set together. If one of those properties is not set, then neither is used.

 

This property is used only if a window has an explicit Application User Model ID (AppUserModelID) ([System.AppUserModel.ID](shell.props_System_AppUserModel_Id), set through [**SHGetPropertyStoreForWindow**](shgetpropertystoreforwindow.md)). If the window does not have an explicit AppUserModelID, this property is ignored and the window is grouped and pinned as if it were part of the process that owns it. For more information on the application of explicit AppUserModelIDs and their effect on taskbar pinning, see [Application User Model IDs (AppUserModelIDs)](shell.AppIDs). This property is meant to be used by applications or windows that want to provide non-default relaunch information. For more information, see [System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand).

> [!Note]  
> This property is ignored if [System.AppUserModel.PreventPinning](shell.props_System_AppUserModel_PreventPinning) is set. This enables an application to control the grouping of its windows by assigning them explicit AppUserModelIDs but preventing those windows from being pinned.

 

To set this property on a window, use [**SHGetPropertyStoreForWindow**](shgetpropertystoreforwindow.md) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](shell.IPropertyStore) object to set the [System.AppUserModel.RelaunchDisplayNameResource](shell.props_System_AppUserModel_RelaunchDisplayNameResource) property of that window.

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

 

 



