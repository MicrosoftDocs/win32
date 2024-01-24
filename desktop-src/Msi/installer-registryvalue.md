---
description: The RegistryValue method of the Installer object reads information about a specified registry key of value.
ms.assetid: 63c258f9-8649-419d-9f79-3681f9f97302
title: Installer.RegistryValue method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.RegistryValue
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.RegistryValue method

The **RegistryValue** method of the [**Installer**](installer-object.md) object reads information about a specified registry key of value. If the key or value specified does not exist, the method returns an error of 9, "Subscript out of Range."

## Syntax


```JScript
Installer.RegistryValue(
  root,
  key,
  value
)
```



## Parameters

<dl> <dt>

*root* 
</dt> <dd>

In Windows NT 4.0, the registry root is either a numeric root key or a machine name as a string. Machine names are always strings. In Windows 95, Windows 98, or Windows Me, the registry root is a numeric root key only. You can only access HKLM on a remote machine.



| Root                                                                                                                                                                                   | Meaning      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| <span id="HKEY_CLASSES_ROOT"></span><span id="hkey_classes_root"></span><dl> <dt>**HKEY\_CLASSES\_ROOT**</dt> </dl>             | 0<br/> |
| <span id="HKEY_CURRENT_USER"></span><span id="hkey_current_user"></span><dl> <dt>**HKEY\_CURRENT\_USER**</dt> </dl>             | 1<br/> |
| <span id="HKEY_LOCAL_MACHINE"></span><span id="hkey_local_machine"></span><dl> <dt>**HKEY\_LOCAL\_MACHINE**</dt> </dl>          | 2<br/> |
| <span id="HKEY_USERS"></span><span id="hkey_users"></span><dl> <dt>**HKEY\_USERS**</dt> </dl>                                   | 3<br/> |
| <span id="HKEY_PERFORMANCE_DATA"></span><span id="hkey_performance_data"></span><dl> <dt>**HKEY\_PERFORMANCE\_DATA**</dt> </dl> | 4<br/> |
| <span id="HKEY_CURRENT_CONFIG"></span><span id="hkey_current_config"></span><dl> <dt>**HKEY\_CURRENT\_CONFIG**</dt> </dl>       | 5<br/> |
| <span id="HKEY_DYN_DATA"></span><span id="hkey_dyn_data"></span><dl> <dt>**HKEY\_DYN\_DATA**</dt> </dl>                         | 6<br/> |



 

</dd> <dt>

*key* 
</dt> <dd>

A string containing the complete key path from the root.

</dd> <dt>

*value* 
</dt> <dd>

This optional parameter designates which associated value to return for the specified key. The value is one of the values shown in the following table.



| Value                                                                                                                                                                                                    | Meaning                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Missing_or_blank"></span><span id="missing_or_blank"></span><span id="MISSING_OR_BLANK"></span><dl> <dt>**Missing or blank**</dt> </dl> | Returns a Boolean designating whether the key exists.<br/>                                                                                        |
| <span id="String"></span><span id="string"></span><span id="STRING"></span><dl> <dt>**String**</dt> </dl>                                         | Returns the data associated with the named value, fails if the value name is non-existent.<br/>                                                   |
| <span id="Positive_integer"></span><span id="positive_integer"></span><span id="POSITIVE_INTEGER"></span><dl> <dt>**Positive integer**</dt> </dl> | Returns the 1-based enumerated value name, it is empty if non-existent. This option uses the [**RegEnumValue**](/windows/win32/api/winreg/nf-winreg-regenumvaluea) function.<br/> |
| <span id="Negative_integer"></span><span id="negative_integer"></span><span id="NEGATIVE_INTEGER"></span><dl> <dt>**Negative integer**</dt> </dl> | Returns the 1-based enumerated subkey name, this is empty if non-existent. This option uses the [**RegEnumKey**](/windows/win32/api/winreg/nf-winreg-regenumkeya) function.<br/>  |
| <span id="Zero_integer"></span><span id="zero_integer"></span><span id="ZERO_INTEGER"></span><dl> <dt>**Zero integer**</dt> </dl>                 | Returns the string class name for the designated key.<br/>                                                                                        |
| <span id="Empty_string____"></span><span id="empty_string____"></span><span id="EMPTY_STRING____"></span><dl> <dt>**Empty string " "**</dt> </dl> | Returns the default value of the registry key.<br/>                                                                                               |



 

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 
