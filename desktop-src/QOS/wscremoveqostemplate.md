---
title: WSCRemoveQOSTemplate function
description: The WSCRemoveQOSTemplate function removes a QOS template. Note that the caller of this function must have administrative rights.
ms.assetid: 'd697c5bf-efdc-47e6-93c7-1fc4937246e0'
keywords: ["WSCRemoveQOSTemplate function QOS"]
topic_type:
- apiref
api_name:
- WSCRemoveQOSTemplate
api_location:
- Qosname.dll
api_type:
- DllExport
---

# WSCRemoveQOSTemplate function

\[ This function is not supported as of Windows Vista.\]

The **WSCRemoveQOSTemplate** function removes a QOS template. Note that the caller of this function must have administrative rights.

## Syntax


```C++
BOOL WSCRemoveQOSTemplate(
  _In_ const LPGUID   lpProviderId,
  _In_       LPWSABUF lpQOSName
);
```



## Parameters

<dl> <dt>

*lpProviderId* \[in\]
</dt> <dd>

Pointer to a provider-selected globally unique identifier (GUID).

</dd> <dt>

*lpQOSName* \[in\]
</dt> <dd>

Specifies the QOS template name.

</dd> </dl>

## Return value

If **WSCRemoveQOSTemplate** succeeds, the return value is **TRUE**. If the function fails, the return value is **FALSE**. For extended error information, call [**WSAGetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms741580).



| Return code                                                                                | Description                                                                             |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>**WSAEINVAL**</dt> </dl>   | The specified QOS template name is invalid.<br/>                                  |
| <dl> <dt>**WSA\_NODATA**</dt> </dl> | The specified QOS template could not be found.<br/>                               |
| <dl> <dt>**WSEFAULT**</dt> </dl>    | One or more of the parameters is not a valid part of the user address space.<br/> |



 

## Remarks

In Windows Vista and later, this function always returns with an error.

The **WSCRemoveQOSTemplate** function deletes a QOS template previously installed with [**WSCInstallQOSTemplate**](wscinstallqostemplate.md). If *lpProviderId* is **NULL**, **WSCRemoveQOSTemplate** attempts to find and delete a QOS template from the global list of QOS names. Otherwise, **WSCRemoveQOSTemplate** attempts to find and delete a QOS template specific to the service provider associated with *lpProviderId*. You cannot delete the base set of QOS names included with Windows Sockets 2. The **WSAEINVAL** error code will be returned if such an attempt is made.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Header<br/>                   | <dl> <dt>Qosname.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Qosname.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qosname.dll</dt> </dl> |



## See also

<dl> <dt>

[**WPUGetQOSTemplate**](wpugetqostemplate.md)
</dt> <dt>

[**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587)
</dt> <dt>

[**WSCInstallQOSTemplate**](wscinstallqostemplate.md)
</dt> </dl>

 

 





