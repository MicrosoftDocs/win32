---
Description: An explicit Application User Model ID (AppUserModelID) used to associate processes, files, and windows with a particular application.
ms.assetid: 07858b3c-e601-40ec-a87a-d66612d5473a
title: System.AppUserModel.ID
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.AppUserModel.ID

An explicit Application User Model ID (AppUserModelID) used to associate processes, files, and windows with a particular application. In some cases, it is sufficient to rely on the internal AppUserModelID assigned to a process by the system. However, an application that owns multiple processes or an application that is running in a host process might need to explicitly identify itself through this property so that it can group its otherwise disparate windows under a single taskbar button and control the contents of that application's Jump List.

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/win32/Shellapi/nf-shellapi-shgetpropertystoreforwindow?branch=master) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](shell.IPropertyStore) object to set the [System.AppUserModel.ID](shell.props_System_AppUserModel_Id) property of that window.

For more information, see [Application User Model IDs (AppUserModelIDs)](shell.AppIDs).

At the time the [System.AppUserModel.ID](shell.props_System_AppUserModel_Id) property is set, the taskbar is notified to refresh its information on the window or shortcut given that AppUserModelID.

Other window and shortcut properties can be used in conjunction with an explicit AppUserModelID to further control the grouping and pinning associated with a window, the display name and icon used for it in the taskbar, and the command to launch either an application pinned to the taskbar or a new instance of the application through that application's Jump List. These properties should be set before setting the [System.AppUserModel.ID](shell.props_System_AppUserModel_Id) property. For more information, see the following topics:

-   [System.AppUserModel.PreventPinning](shell.props_System_AppUserModel_PreventPinning)
-   [System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand)
-   [System.AppUserModel.RelaunchDisplayNameResource](shell.props_System_AppUserModel_RelaunchDisplayNameResource)
-   [System.AppUserModel.RelaunchIconResource](shell.props_System_AppUserModel_RelaunchIconResource)

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.ID
   shellPKey = PKEY_AppUserModel_ID
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 5
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

[**SHGetPropertyStoreForWindow**](/windows/win32/Shellapi/nf-shellapi-shgetpropertystoreforwindow?branch=master)
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

 

 



