---
title: NetLogonSetServiceBits function
description: Notifies the Netlogon service of the running state of the services on a domain controller. The caller must be running in the context of either the LocalSystem or the LocalService account.
ms.assetid: 4b527a5b-4ae7-4703-b920-6923bca8e99e
keywords:
- NetLogonSetServiceBits function Network Management
topic_type:
- apiref
api_name:
- NetLogonSetServiceBits
api_location:
- Netapi32.dll
- Logoncli.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NetLogonSetServiceBits function

The **NetLogonSetServiceBits** function notifies the Netlogon service of the running state of the services on a domain controller. The caller must be running in the context of either the LocalSystem or the LocalService account.

## Syntax


```C++
NTSTATUS WINAPI NetLogonSetServiceBits(
  _In_ LPWSTR ServerName,
  _In_ DWORD  ServiceBitsOfInterest,
  _In_ DWORD  ServiceBits
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the domain controller. If this parameter is **NULL**, the local computer is used.

</dd> <dt>

*ServiceBitsOfInterest* \[in\]
</dt> <dd>

A set of flags used as a mask to indicate which service's state (running or not running) is being set. This parameter can be a combination of the following values.



| Value                                                                                                                                                                                                                                                   | Meaning                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <span id="DS_TIMESERV_FLAG"></span><span id="ds_timeserv_flag"></span><dl> <dt>**DS\_TIMESERV\_FLAG**</dt> <dt>0x00000040</dt> </dl>                 | The state of the time service is being set.<br/>                     |
| <span id="DS_GOOD_TIMESERV_FLAG"></span><span id="ds_good_timeserv_flag"></span><dl> <dt>**DS\_GOOD\_TIMESERV\_FLAG**</dt> <dt>0x00000200</dt> </dl> | The state of the time service with clock hardware is being set.<br/> |
| <span id="DS_WS_FLAG"></span><span id="ds_ws_flag"></span><dl> <dt>**DS\_WS\_FLAG**</dt> <dt>0x00002000</dt> </dl>                                   | The state of the Active Directory web service is being set.<br/>     |



 

</dd> <dt>

*ServiceBits* \[in\]
</dt> <dd>

A set of flags used as a mask to indicate whether the service indicated by *ServiceBitsOfInterest* parameter is running or not. If the flag is set to 0, the corresponding service indicated by the *ServiceBitsOfInterest* parameter is not running. Otherwise, if the flag is set to 1, the corresponding service indicated by the *ServiceBitsOfInterest* parameter is running. This parameter can be a combination of the following values.



| Value                                                                                                                                                                                                                                                   | Meaning                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <span id="DS_TIMESERV_FLAG"></span><span id="ds_timeserv_flag"></span><dl> <dt>**DS\_TIMESERV\_FLAG**</dt> <dt>0x00000040</dt> </dl>                 | The time service is running.<br/>                     |
| <span id="DS_GOOD_TIMESERV_FLAG"></span><span id="ds_good_timeserv_flag"></span><dl> <dt>**DS\_GOOD\_TIMESERV\_FLAG**</dt> <dt>0x00000200</dt> </dl> | The time service with clock hardware is running.<br/> |
| <span id="DS_WS_FLAG"></span><span id="ds_ws_flag"></span><dl> <dt>**DS\_WS\_FLAG**</dt> <dt>0x00002000</dt> </dl>                                   | The Active Directory web service is running.<br/>     |



 

</dd> </dl>

## Return value

If the function succeeds, the return value is STATUS\_SUCCESS.

If the function fails, the return value can be one of the following error codes or one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).



| Return code                                                                                               | Description                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STATUS\_ACCESS\_DENIED**</dt> </dl>     | Access is denied. This error is returned if the caller was not a member of the Administrators local group on the target computer.<br/> |
| <dl> <dt>**STATUS\_INVALID\_PARAMETER**</dt> </dl> | A parameter is incorrect. This error is returned if one or more specified service bits are not valid.<br/>                             |



 

## Remarks

The list of running services for the domain controller returned by the [**DsGetDcName**](https://msdn.microsoft.com/library/ms675983) function will contain the running services notified by the **NetLogonSetServiceBits** function.

No header file is available for the **NetLogonSetServiceBits** function . Include the function definition at the top of this page in your source code.

An import library containing the **NetLogonSetServiceBits** function is not included in the Microsoft Windows Software Development Kit (SDK). Applications must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to retrieve the function pointer from the corresponding DLL and call this function.

## Requirements



|                                     |                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| DLL<br/>                      | <dl> <dt>Netapi32.dll on Windows Vista and Windows Server 2008; </dt> <dt>Logoncli.dll on Windows 7, Windows Server 2008 R2, Windows 8 and Windows Server 2012</dt> </dl> |



## See also

<dl> <dt>

[Directory Service functions](directory-service-functions.md)
</dt> <dt>

[**DsGetDcName**](https://msdn.microsoft.com/library/ms675983)
</dt> <dt>

[**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212)
</dt> <dt>

[**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175)
</dt> <dt>

[**NetGetAnyDCName**](/windows/win32/Lmaccess/nf-lmaccess-netgetanydcname?branch=master)
</dt> <dt>

[**NetGetDCName**](/windows/win32/Lmaccess/nf-lmaccess-netgetdcname?branch=master)
</dt> <dt>

[Network Management Overview](network-management.md)
</dt> <dt>

[Network Management Functions](network-management-functions.md)
</dt> </dl>

 

 





