---
title: CheckAccess method of the StdRegProv class
description: The CheckAccess method verifies that the user has the specified permissions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9984dc6a-a0f9-47dd-8f73-7be9500cfbd4'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CheckAccess method", "CheckAccess method, StdRegProv class", "StdRegProv class, CheckAccess method"]
topic_type:
- apiref
api_name:
- StdRegProv.CheckAccess
api_location:
- Stdprov.dll
api_type:
- COM
---

# CheckAccess method of the StdRegProv class

The **CheckAccess** method verifies that the user has the specified permissions.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 CheckAccess(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [in]  uint32 uRequired = 3,
  [out] bool   bGranted
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

The key to be verified.

</dd> <dt>

*uRequired* \[in\]
</dt> <dd>

A parameter that specifies the access permissions to be verified. You can add these values together to verify more than one access permission. The default value is 3, **KEY\_QUERY\_VALUE** plus **KEY\_SET\_VALUE**. The following access permission values are defined in WinNT.h.

<dt>

<span id="KEY_QUERY_VALUE"></span><span id="key_query_value"></span>

<span id="KEY_QUERY_VALUE"></span><span id="key_query_value"></span>**KEY\_QUERY\_VALUE** (1)


</dt> <dd>

Required to query the values of a registry key.

</dd> <dt>

<span id="KEY_SET_VALUE"></span><span id="key_set_value"></span>

<span id="KEY_SET_VALUE"></span><span id="key_set_value"></span>**KEY\_SET\_VALUE** (2)


</dt> <dd>

Required to create, delete, or set a registry value.

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3** (KEY\_QUERY\_VALUE \| KEY\_SET\_VALUE)


</dt> <dd>

Default value, allows querying, creating, deleting, or setting a registry value.

</dd> <dt>

<span id="KEY_CREATE_SUB_KEY"></span><span id="key_create_sub_key"></span>

<span id="KEY_CREATE_SUB_KEY"></span><span id="key_create_sub_key"></span>**KEY\_CREATE\_SUB\_KEY** (4)


</dt> <dd>

Required to create a subkey of a registry key.

</dd> <dt>

<span id="KEY_ENUMERATE_SUB_KEYS"></span><span id="key_enumerate_sub_keys"></span>

<span id="KEY_ENUMERATE_SUB_KEYS"></span><span id="key_enumerate_sub_keys"></span>**KEY\_ENUMERATE\_SUB\_KEYS** (8)


</dt> <dd>

Required to enumerate the subkeys of a registry key.

</dd> <dt>

<span id="KEY_NOTIFY"></span><span id="key_notify"></span>

<span id="KEY_NOTIFY"></span><span id="key_notify"></span>**KEY\_NOTIFY** (16)


</dt> <dd>

Required to request change notifications for a registry key or for subkeys of a registry key.

</dd> <dt>

<span id="KEY_CREATE"></span><span id="key_create"></span>

<span id="KEY_CREATE"></span><span id="key_create"></span>**KEY\_CREATE** (32)


</dt> <dd>

Required to create a registry key.

</dd> <dt>

<span id="DELETE"></span><span id="delete"></span>

<span id="DELETE"></span><span id="delete"></span>**DELETE** (65536)


</dt> <dd>

Required to delete a registry key.

</dd> <dt>

<span id="READ_CONTROL"></span><span id="read_control"></span>

<span id="READ_CONTROL"></span><span id="read_control"></span>**READ\_CONTROL** (131072)


</dt> <dd>

Combines the **STANDARD\_RIGHTS\_READ**, **KEY\_QUERY\_VALUE**, **KEY\_ENUMERATE\_SUB\_KEYS**, and **KEY\_NOTIFY** values.

</dd> <dt>

<span id="WRITE_DAC"></span><span id="write_dac"></span>

<span id="WRITE_DAC"></span><span id="write_dac"></span>**WRITE\_DAC** (262144)


</dt> <dd>

Required to modify the DACL in the object's security descriptor.

</dd> <dt>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>**WRITE\_OWNER** (524288)


</dt> <dd>

Required to change the owner in the object's security descriptor.

</dd> </dl> </dd> <dt>

*bGranted* \[out\]
</dt> <dd>

If **true**, the user has the specified access permissions.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

The Registry Provider **CheckAccess** method allows you to determine whether the user of a script has a particular access right on a registry subkey or entry. The Registry Provider does not provide a way to list all of the access rights on a given subkey or entry, or to make any changes to the access rights.

This method returns false if you do not have appropriate permissions; the method also returns false if the parent key described in *hDefKey* does not exist.

## Examples

The [List Registry Key Access Rights](https://Gallery.TechNet.Microsoft.Com/f9ad7bcc-664c-4436-82fb-dd5d9e29e484) VBScript sample uses WMI to check access rights for the logged on user to the **HKLM\\SYSTEM\\CurrentControlSet** portion of the registry.

The [Robust Office Inventory Scan Tool (ROISCAN)](https://Gallery.TechNet.Microsoft.Com/68b80aba-130d-4ad4-aa45-832b1ee49602) is a VBScript script to inventory all Microsoft Office installations on the computer to aid in troubleshooting patch and product installation issues.

The following VBScript code example shows how to use the **CheckAccess** method to verify that the user has the right to read the values of the registry key:

**HKEY\_CURRENT\_USER**\\**SYSTEM**\\**CurrentControlSet**


```VB
' Create constants for access rights and registry hive 
const KEY_QUERY_VALUE = &amp;H0001
const HKEY_LOCAL_MACHINE = &amp;H80000002

strComputer = "."
Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" &amp;_ 
                     strComputer & "\root\default:StdRegProv")

strKeyPath = "SYSTEM\CurrentControlSet"

' Does the account under which the script runs have the 
'    right to query the SYSTEM\CurrentControlSet key
objReg.CheckAccess HKEY_LOCAL_MACHINE, strKeyPath, KEY_QUERY_VALUE, bHasAccessRight
If bHasAccessRight = True Then
    Wscript.Echo "Has Query Value Access Rights on HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet"
Else
    Wscript.Echo "No Query Value Access Rights on HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet"
End If
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
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

 

 





