---
title: EnumKey method of the StdRegProv class
description: The EnumKey method enumerates the subkeys for a path. See Obtaining Registry Data for general information on accessing the registry through WMI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d7132e69-7d8c-46a7-8dba-5944d81fddf3
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnumKey method
- EnumKey method, StdRegProv class
- StdRegProv class, EnumKey method
topic_type:
- apiref
api_name:
- StdRegProv.EnumKey
api_location:
- Stdprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnumKey method of the StdRegProv class

The **EnumKey** method enumerates the subkeys for a path. See [Obtaining Registry Data](https://msdn.microsoft.com/library/aa392722) for general information on accessing the registry through WMI.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 EnumKey(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [out] string sNames[]
);
```



## Parameters

<dl> <dt>

*hDefKey* \[in\]
</dt> <dd>

A registry tree, also known as a hive, that contains the *sSubKeyName* path. The default value is **HKEY\_LOCAL\_MACHINE**.

The following trees are defined in WinReg.h.

<dt>

<span id="HKEY_CLASSES_ROOT"></span><span id="hkey_classes_root"></span>

**HKEY\_CLASSES\_ROOT** (2147483648)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_USER"></span><span id="hkey_current_user"></span>

**HKEY\_CURRENT\_USER** (2147483649)


</dt> <dd></dd> <dt>

<span id="HKEY_LOCAL_MACHINE"></span><span id="hkey_local_machine"></span>

**HKEY\_LOCAL\_MACHINE** (2147483650)


</dt> <dd></dd> <dt>

<span id="HKEY_USERS"></span><span id="hkey_users"></span>

**HKEY\_USERS** (2147483651)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_CONFIG"></span><span id="hkey_current_config"></span>

**HKEY\_CURRENT\_CONFIG** (2147483653)


</dt> <dd></dd> </dl> </dd> <dt>

*sSubKeyName* \[in\]
</dt> <dd>

A path that contains the subkeys to be enumerated.

</dd> <dt>

*sNames* \[out\]
</dt> <dd>

An array of subkey strings.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

In some instances, useful configuration information is stored as the names of a set of subkeys. In the following sample script, for instance, the subkey names represent the services on a computer. In a case such as this, simply listing the names of the subkeys provides useful information.

The **EnumKey** method enables you to return the subkeys of a registry key or subkey. Note that the **EnumKey** method returns only the immediate subkeys of a key or subkey; it does not return any subkeys that might be contained within those top-level subkeys. To return all subkeys, you need to use a recursive function.

## Examples

The following PowerShell code example shows how to use the **EnumKey** method to enumerate the services listed as subkeys in the registry key:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**


```PowerShell
$HKEY_LOCAL_MACHINE = 2147483650
$strKeyPath = "SYSTEM\CurrentControlSet\Services"

$objReg = [WMIClass]"root\default:StdRegProv"

$arrSubKeys = $objReg.EnumKey($HKEY_LOCAL_MACHINE, $strKeyPath)
foreach ($subKey in ($arrSubKeys.sNames))
{
    $subKey
}
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Stdprov.dll</dt> </dl>  |



## See also

<dl> <dt>

[**StdRegProv**](stdregprov.md)
</dt> <dt>

[Modifying the System Registry](https://msdn.microsoft.com/library/aa392388)
</dt> <dt>

[WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600)
</dt> </dl>

 

 





