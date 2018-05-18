---
title: SetQWORDValue method of the StdRegProv class
description: The SetQWORDValue method sets the data value for a named value whose data type is REG\_QWORD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4f078f83-d099-4695-98dc-919e185273e8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetQWORDValue method", "SetQWORDValue method, StdRegProv class", "StdRegProv class, SetQWORDValue method"]
topic_type:
- apiref
api_name:
- StdRegProv.SetQWORDValue
api_location:
- Stdprov.dll
api_type:
- COM
---

# SetQWORDValue method of the StdRegProv class

The **SetQWORDValue** method sets the data value for a named value whose data type is **REG\_QWORD**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetQWORDValue(
  [in] uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in] string sSubKeyName,
  [in] string sValueName,
  [in] uint64 uValue = 
);
```



## Parameters

<dl> <dt>

*hDefKey* \[in\]
</dt> <dd>

An optional parameter that specifies the tree that contains the *sSubKeyName* path. The default value is **HKEY\_LOCAL\_MACHINE**.

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

A path that contains the named values.

</dd> <dt>

*sValueName* \[in\]
</dt> <dd>

A named value whose data value you are retrieving. Specify an empty string to get the default named value.

</dd> <dt>

*uValue* \[in\]
</dt> <dd>

A **QWORD** data value for the named value. The default value is "3".

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

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

 

 





