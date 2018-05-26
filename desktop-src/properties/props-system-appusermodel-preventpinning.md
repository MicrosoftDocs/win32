---
Description: Disables the ability of a shortcut or window to be pinned to the taskbar or the Start menu. This property also makes the item ineligible for inclusion in the Start menus Most Frequently Used (MFU) list.
ms.assetid: 86239BF8-BCFC-4e76-BF94-5ABA4639562C
title: System.AppUserModel.PreventPinning
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.AppUserModel.PreventPinning

Disables the ability of a shortcut or window to be pinned to the taskbar or the **Start** menu. This property also makes the item ineligible for inclusion in the **Start** menu's Most Frequently Used (MFU) list.

This property must be set on a window before the [PKEY\_AppUserModel\_ID](shell.props_System_AppUserModel_Id) property. After the PKEY\_AppUserModel\_ID property is set, changes to [PKEY\_AppUserModel\_PreventPinning](shell.props_System_AppUserModel_PreventPinning) are ignored.

For more information about Application User Model IDs (AppUserModelIDs) and other methods of excluding an item from being pinned to the taskbar and from MFU inclusion, see [Application User Model IDs (AppUserModelIDs)](shell.AppIDs).

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/win32/Shellapi/nf-shellapi-shgetpropertystoreforwindow?branch=master) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](shell.IPropertyStore) object to set the [System.AppUserModel.PreventPinning](shell.props_System_AppUserModel_PreventPinning) property of that window.

Setting this property causes the following properties to be ignored:

-   [System.AppUserModel.RelaunchCommand](shell.props_System_AppUserModel_RelaunchCommand)
-   [System.AppUserModel.RelaunchDisplayNameResource](shell.props_System_AppUserModel_RelaunchDisplayNameResource)
-   [System.AppUserModel.RelaunchIconResource](shell.props_System_AppUserModel_RelaunchIconResource)

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.PreventPinning
   shellPKey = PKEY_AppUserModel_PreventPinning
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 9
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
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

 

 



