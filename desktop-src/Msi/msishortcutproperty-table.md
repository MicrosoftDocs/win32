---
description: The MsiShortcutProperty table enables Window Installer to set properties for shortcuts that are also Windows Shell objects.
ms.assetid: d959769d-113f-4af2-89d4-ad3f5322de33
title: MsiShortcutProperty Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiShortcutProperty Table

The MsiShortcutProperty table enables Window Installer to set properties for shortcuts that are also [Windows Shell](/previous-versions/windows/desktop/legacy/bb773177(v=vs.85)) objects. Beginning with Windows Vista and Windows Server 2008 the Windows Shell provides an IPropertyStore Interface for shell objects such as shortcuts. A Windows Installer 5.0 package running on Windows Server 2008 R2 or Windows 7 can set these properties when the shortcut is installed.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This table is available beginning with Windows Installer 5.0.

The MsiShortcutProperty table has the following columns.



| Column              | Type                         | Key | Nullable |
|---------------------|------------------------------|-----|----------|
| MsiShortcutProperty | [Identifier](identifier.md) | Y   | N        |
| Shortcut\_          | [Identifier](identifier.md) | N   | N        |
| PropertyKey         | [Formatted](formatted.md)   | N   | N        |
| PropVariantValue    | [Formatted](formatted.md)   | N   | N        |



 

## Columns

<dl> <dt>

<span id="MsiShortcutProperty"></span><span id="msishortcutproperty"></span><span id="MSISHORTCUTPROPERTY"></span>MsiShortcutProperty
</dt> <dd>

Unique identifier for this row of the MsiShortcutProperty table.

</dd> <dt>

<span id="Shortcut_"></span><span id="shortcut_"></span><span id="SHORTCUT_"></span>Shortcut\_
</dt> <dd>

A key into the [Shortcut](shortcut-table.md) table that identifies the shortcut having a property set.

</dd> <dt>

<span id="PropertyKey"></span><span id="propertykey"></span><span id="PROPERTYKEY"></span>PropertyKey
</dt> <dd>

A string value that provides information for the [**PROPERTYKEY**](/windows/win32/api/wtypes/ns-wtypes-propertykey) structure. The information in this field must refer to the canonical name of a property registered with the Windows property system. For more information about the Windows property system, see the [Property System Overview](/previous-versions//bb776909(v=vs.85)).

</dd> <dt>

<span id="PropVariantValue"></span><span id="propvariantvalue"></span><span id="PROPVARIANTVALUE"></span>PropVariantValue
</dt> <dd>

A string value that provides information for the [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure.

</dd> </dl>

Multiple properties can be set on a shortcut. If the same property is set multiple times on the same shortcut the value is set in an unspecified order.

Windows Installer can set shortcut properties only when the shortcut is installed or reinstalled. A patch that does not reinstall a shortcut that has already been installed does not update the shortcut's properties. A patch can update the properties by including a [Shortcut](shortcut-table.md) table in the patch package and reinstalling the shortcut.

## Remarks

[Windows Installer Error Message](windows-installer-error-messages.md) 1946 is returned as a warning, and the installation continues, if Windows Installer is unable to set a shortcut property specified in the MsiShortcutProperty table.

## Validation

<dl>

[ICE03](ice03.md)  
</dl>

 

 
