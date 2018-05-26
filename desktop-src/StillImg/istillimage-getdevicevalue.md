---
title: GetDeviceValue method
description: The IStillImage GetDeviceValue method is used to obtain information from the registry that has been associated with an image acquisition device API such as TWAIN or ISIS.
ms.assetid: 3d8fb259-d023-4351-97bd-4aaed69bc5c4
keywords:
- GetDeviceValue method Still Image
topic_type:
- apiref
api_name:
- GetDeviceValue
api_location:
- Sti.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetDeviceValue method

The **IStillImage::GetDeviceValue** method is used to obtain information from the registry that has been associated with an image acquisition device API such as TWAIN or ISIS.

## Syntax


```C++
HRESULT GetDeviceValue(
  [in]  LPWSTR  pwszDeviceName,
  [out] LPWSTR  pValueName,
  [out] LPDWORD pType,
  [out] LPBYTE  pData,
  [out] LPDWORD cbData
);
```



## Parameters

<dl> <dt>

*pwszDeviceName* \[in\]
</dt> <dd>

Pointer to a string that represents the name of the value tag. It is the key that is used with **GetDeviceValue** to look up the ancillary data. Microsoft has defined and reserved the following device values:



| Value                                                                                                                                                                                                                           | Meaning                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <span id="STI_DEVICE_VALUE_TWAIN_NAME"></span><span id="sti_device_value_twain_name"></span><dl> <dt>**STI\_DEVICE\_VALUE\_TWAIN\_NAME**</dt> </dl>                      | The data associated with this registry key is the name of a TWAIN device.<br/>                                          |
| <span id="STI_DEVICE_VALUE_ISIS_NAME"></span><span id="sti_device_value_isis_name"></span><dl> <dt>**STI\_DEVICE\_VALUE\_ISIS\_NAME**</dt> </dl>                         | The data associated with this registry key is the name of an ISIS device.<br/>                                          |
| <span id="STI_DEVICE_VALUE_ICM_PROFILE"></span><span id="sti_device_value_icm_profile"></span><dl> <dt>**STI\_DEVICE\_VALUE\_ICM\_PROFILE**</dt> </dl>                   | The data associated with this registry key is the file name of the ICM device profile for the device.<br/>              |
| <span id="STI_DEVICE_VALUE_DEFAULT_LAUNCHAPP"></span><span id="sti_device_value_default_launchapp"></span><dl> <dt>**STI\_DEVICE\_VALUE\_DEFAULT\_LAUNCHAPP**</dt> </dl> | The data associated with this registry key is the name of the default launch application for events on the device.<br/> |



 

</dd> <dt>

*pValueName* \[out\]
</dt> <dd>

Pointer to a string that receives information from the registry that has been associated with an image acquisition device API.

</dd> <dt>

*pType* \[out\]
</dt> <dd>

Pointer to a variable that receives the key's value type. The *pType* parameter can be **NULL** if the type is not required. The value returned through this parameter is one of the following.



| Value                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="REG_BINARY"></span><span id="reg_binary"></span><dl> <dt>**REG\_BINARY**</dt> </dl>                                          | Binary data in any form.<br/>                                                                                                                                                                                                                                   |
| <span id="REG_DWORD"></span><span id="reg_dword"></span><dl> <dt>**REG\_DWORD**</dt> </dl>                                             | A 32-bit number.<br/>                                                                                                                                                                                                                                           |
| <span id="REG_DWORD_LITTLE_ENDIAN"></span><span id="reg_dword_little_endian"></span><dl> <dt>**REG\_DWORD\_LITTLE\_ENDIAN**</dt> </dl> | A 32-bit number in little-endian format (same as REG\_DWORD). In little-endian format, the most significant byte of a word is the high-order byte. This is the most common format for computers running Windows NT/Windows 2000 and Windows 98/Windows Me.<br/> |
| <span id="REG_DWORD_BIG_ENDIAN"></span><span id="reg_dword_big_endian"></span><dl> <dt>**REG\_DWORD\_BIG\_ENDIAN**</dt> </dl>          | A 32-bit number in big-endian format. In big-endian format, the most significant byte of a word is the low-order byte.<br/>                                                                                                                                     |
| <span id="REG_EXPAND_SZ"></span><span id="reg_expand_sz"></span><dl> <dt>**REG\_EXPAND\_SZ**</dt> </dl>                                | A **null**-terminated string that contains unexpanded references to environment variables (for example, "%PATH%"). It is a Unicode or ANSI string depending on whether you use the Unicode or ANSI methods.<br/>                                                |
| <span id="REG_LINK"></span><span id="reg_link"></span><dl> <dt>**REG\_LINK**</dt> </dl>                                                | A Unicode symbolic link.<br/>                                                                                                                                                                                                                                   |
| <span id="REG_MULTI_SZ"></span><span id="reg_multi_sz"></span><dl> <dt>**REG\_MULTI\_SZ**</dt> </dl>                                   | An array of **null**-terminated strings, terminated by two **null** characters.<br/>                                                                                                                                                                            |
| <span id="REG_NONE"></span><span id="reg_none"></span><dl> <dt>**REG\_NONE**</dt> </dl>                                                | No defined value type.<br/>                                                                                                                                                                                                                                     |
| <span id="REG_RESOURCE_LIST"></span><span id="reg_resource_list"></span><dl> <dt>**REG\_RESOURCE\_LIST**</dt> </dl>                    | A device-driver resource list.<br/>                                                                                                                                                                                                                             |
| <span id="REG_SZ"></span><span id="reg_sz"></span><dl> <dt>**REG\_SZ**</dt> </dl>                                                      | A **null**-terminated string. It is a Unicode or ANSI string depending on whether you use the Unicode or ANSI methods.<br/>                                                                                                                                     |



 

</dd> <dt>

*pData* \[out\]
</dt> <dd>

Pointer to a buffer that receives the value's data. This parameter can be **NULL** if the data is not required.

</dd> <dt>

*cbData* \[out\]
</dt> <dd>

Pointer to a variable that specifies the size, in bytes, of the buffer pointed to by the *pData* parameter. When the method returns, this variable contains the size of the data copied to *pData* .

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK.

If the method fails because the buffer specified by *pData* parameter is not large enough to hold the data, the return value is ERROR\_MORE\_DATA.

If the method fails for another reason, the return value is the appropriate COM error.

## Remarks

If the buffer specified by *pData* parameter is not large enough to hold the data, the method returns the value ERROR\_MORE\_DATA, and stores the required buffer size, in bytes, into the parameter pointed to by *cbData* .

If *pData* is **NULL**, and *cbData* is non-**NULL**, the method returns S\_OK, and stores the size of the data, in bytes, in the parameter pointed to by *cbData* . This allows an application to determine the best way to allocate a buffer for the value key's data.

If the data has the REG\_SZ, REG\_MULTI\_SZ or REG\_EXPAND\_SZ type, then *pData* also includes the size of the terminating **null** character.

The *cbData* parameter can be **NULL** only if *pData* is **NULL**.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Sti.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Sti.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sti.dll</dt> </dl> |



## See also

<dl> <dt>

[About Still Image](about-still-image.md)
</dt> <dt>

[Making an Application Still Image-Aware](making-an-application-still-image-aware.md)
</dt> </dl>

 

 





