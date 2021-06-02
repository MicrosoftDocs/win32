---
description: Creates the specified registry key in an offline registry hive. If the key already exists, the function opens it.
ms.assetid: 40e7468d-e781-4945-9023-580c06088b87
title: ORCreateKey function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORCreateKey
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORCreateKey function

Creates the specified registry key in an offline registry hive. If the key already exists, the function opens it.

## Syntax


```C++
DWORD ORCreateKey(
  _In_      ORHKEY               Handle,
  _In_      PCWSTR               lpSubKey,
  _In_opt_  PWSTR                lpClass,
  _In_opt_  DWORD                dwOptions,
  _In_opt_  PSECURITY_DESCRIPTOR pSecurityDescriptor,
  _Out_     PORHKEY              phkResult,
  _Out_opt_ PDWORD               pdwDisposition
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> <dt>

*lpSubKey* \[in\]
</dt> <dd>

A pointer to a Unicode string that contains the name of a subkey that this function opens or creates. The *lpSubKey* parameter must specify a subkey of the key identified by the *Handle* parameter; it can be up to 32 levels deep in the registry tree. For more information about key names, see [Structure of the Registry](../sysinfo/structure-of-the-registry.md).

This parameter cannot be **NULL**.

Key names are not case sensitive.

</dd> <dt>

*lpClass* \[in, optional\]
</dt> <dd>

The class (object type) of this key. This parameter may be ignored. This parameter can be **NULL**.

</dd> <dt>

*dwOptions* \[in, optional\]
</dt> <dd>

This parameter can be 0 or one of the following values.



| Value                                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="REG_OPTION_CREATE_LINK"></span><span id="reg_option_create_link"></span><dl> <dt>**REG\_OPTION\_CREATE\_LINK**</dt> <dt>0x00000002L</dt> </dl>    | The key is a symbolic link. The target path is assigned to the L"SymbolicLinkValue" value of the key. The target path must be an absolute registry path. If this option is set, **REG\_OPTION\_NON\_VOLATILE** must also be set. <br/> If the *lpSubKey* parameter specifies an existing key, it must have been created with **REG\_OPTION\_CREATE\_LINK**.<br/> Registry symbolic links should be used only when absolutely necessary for application compatibility. <br/> |
| <span id="REG_OPTION_NON_VOLATILE"></span><span id="reg_option_non_volatile"></span><dl> <dt>**REG\_OPTION\_NON\_VOLATILE**</dt> <dt>0x00000000L</dt> </dl> | The key is not volatile; this is the default. The information is stored in a file and is preserved when the system is restarted. The [**ORSaveHive**](orsavehive.md) function saves keys that are not volatile.<br/>                                                                                                                                                                                                                                                                   |



 

</dd> <dt>

*pSecurityDescriptor* \[in, optional\]
</dt> <dd>

A pointer to a [SECURITY\_DESCRIPTOR](/windows/win32/api/winnt/ns-winnt-security_descriptor) structure that contains a security descriptor for the new key. If *pSecurityDescriptor* is **NULL**, the key gets a default security descriptor. The ACLs in a default security descriptor for a key are inherited from its direct parent key.

</dd> <dt>

*phkResult* \[out\]
</dt> <dd>

A pointer to a variable that receives a handle to the opened or created key. Use the [**ORCloseKey**](orclosekey.md) function to close the key after you have finished using the handle.

</dd> <dt>

*pdwDisposition* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives one of the following disposition values.



| Value                                                                                                                                                                                                                                                          | Meaning                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <span id="REG_CREATED_NEW_KEY"></span><span id="reg_created_new_key"></span><dl> <dt>**REG\_CREATED\_NEW\_KEY**</dt> <dt>0x00000001L</dt> </dl>             | The key did not exist and was created.<br/>                       |
| <span id="REG_OPENED_EXISTING_KEY"></span><span id="reg_opened_existing_key"></span><dl> <dt>**REG\_OPENED\_EXISTING\_KEY**</dt> <dt>0x00000002L</dt> </dl> | The key existed and was simply opened without being changed.<br/> |



 

If *pdwDisposition* is **NULL**, no disposition information is returned.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

If the *dwOptions* parameter is set with **REG\_OPTION\_CREATE\_LINK** but **REG\_OPTION\_NON\_VOLATILE** is clear, or if the handle to be returned would be a handle to the root key of the hive, the function returns ERROR\_INVALID\_PARAMETER.

## Remarks

The key that the **ORCreateKey** function creates has no values. An application can use the [**ORSetValue**](orsetvalue.md) function to set key values.

The **ORCreateKey** function cannot be used to create the root key in an offline registry hive. Use the [**ORCreateHive**](orcreatehive.md) function to create the root key and obtain a handle to the key.

The offline registry does not support saving individual keys. Use the [**ORSaveHive**](orsavehive.md) function to save a key and its subkeys in a hive.

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



## See also

<dl> <dt>

[**ORCloseKey**](orclosekey.md)
</dt> <dt>

[**ORCreateHive**](orcreatehive.md)
</dt> <dt>

[**ORDeleteKey**](ordeletekey.md)
</dt> <dt>

[**ORSaveHive**](orsavehive.md)
</dt> <dt>

[SECURITY\_DESCRIPTOR](/windows/win32/api/winnt/ns-winnt-security_descriptor)
</dt> </dl>

 

 
