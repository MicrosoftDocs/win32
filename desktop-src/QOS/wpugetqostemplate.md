---
title: WPUGetQOSTemplate function
description: The WPUGetQOSTemplate function retrieves a QOS template for a particular service provider.
ms.assetid: edd66b0a-04c8-42c6-9cd4-c3d20ddec20a
keywords:
- WPUGetQOSTemplate function QOS
topic_type:
- apiref
api_name:
- WPUGetQOSTemplate
api_location:
- Qosname.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPUGetQOSTemplate function

\[ This function is not supported as of Windows Vista.\]

The **WPUGetQOSTemplate** function retrieves a QOS template for a particular service provider.

## Syntax


```C++
INT WPUGetQOSTemplate(
  _In_  const LPGUID   lpProviderId,
  _In_        LPWSABUF lpQOSName,
  _Out_       LPQOS    lpQOS
);
```



## Parameters

<dl> <dt>

*lpProviderId* \[in\]
</dt> <dd>

Pointer to a provider selected globally unique identifier (GUID).

</dd> <dt>

*lpQOSName* \[in\]
</dt> <dd>

Specifies the QOS template name.

</dd> <dt>

*lpQOS* \[out\]
</dt> <dd>

Pointer to a [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure.

</dd> </dl>

## Return value

If **WPUGetQOSTemplate** succeeds, the return value is zero. If the function fails, the return value is SOCKET\_ERROR. For extended error information, call [**WSAGetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms741580).



| Return code                                                                                | Description                                                                                    |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <dl> <dt>**WSAEFAULT**</dt> </dl>   | The *lpQOS* or *lpQOSName* parameter is not a valid part of the user address space.<br/> |
| <dl> <dt>**WSAEINVAL**</dt> </dl>   | The specified *lpProviderId* is invalid, or the *lpQOS* template is invalid.<br/>        |
| <dl> <dt>**WSA\_NODATA**</dt> </dl> | The specified QOS name could not be found.<br/>                                          |
| <dl> <dt>**WSAENOBUFS**</dt> </dl>  | The ProviderSpecific buffer is too small.<br/>                                           |



 

## Remarks

In Windows Vista and later, this function always returns with an error.

The **WPUGetQOSTemplate** function retrieves a QOS-named template containing the associated [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure. If *lpProviderId* is **NULL**, **WPUGetQOSTemplate** attempts to find the QOS-named template in the global list of QOS names. Otherwise, **WPUGetQOSTemplate** searches the template list specific to the service provider indicated by lpProviderId.

The *lpQOS* parameter can include a [ProviderSpecific](the-providerspecific-buffer.md) buffer for retrieval with the basic [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure. In this case, the ProviderSpecific buffer must be large enough to hold the provider-specific information stored in the template; otherwise **WPUGetQOSTemplate** returns WSAENOBUFS.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Header<br/>                   | <dl> <dt>Qosname.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Qosname.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qosname.dll</dt> </dl> |



## See also

<dl> <dt>

[**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice)
</dt> <dt>

[**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587)
</dt> <dt>

[**WSCInstallQOSTemplate**](wscinstallqostemplate.md)
</dt> <dt>

[**WSCRemoveQOSTemplate**](wscremoveqostemplate.md)
</dt> </dl>

 

 





