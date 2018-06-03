---
title: WSCInstallQOSTemplate function
description: The WSCInstallQOSTemplate function installs a QOS template, based on a QOS name.
ms.assetid: c5e06803-4401-4089-9fe8-cf76669bec7b
keywords:
- WSCInstallQOSTemplate function QOS
topic_type:
- apiref
api_name:
- WSCInstallQOSTemplate
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

# WSCInstallQOSTemplate function

\[ This function is not supported as of Windows Vista.\]

The **WSCInstallQOSTemplate** function installs a QOS template, based on a QOS name. This [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure (and thus its QOS settings) can be retrieved by calling the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) function and passing in its associated QOS name. Note that the caller of this function must have administrative rights.

## Syntax


```C++
BOOL WSCInstallQOSTemplate(
  _In_ const LPGUID   lpProviderId,
  _In_       LPWSABUF lpQOSName,
  _In_       LPQOS    lpQOS
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

</dd> <dt>

*lpQOS* \[in\]
</dt> <dd>

Pointer to a [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure.

</dd> </dl>

## Return value

If **WSCInstallQOSTemplate** succeeds, the return value is **TRUE**. If the function fails, the return value is **FALSE**. For extended error information, call [**WSAGetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms741580).



| Return code                                                                              | Description                                                                                                                                       |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**WSAEINVAL**</dt> </dl> | The specified QOS template name or provider identifier is invalid, or the contents of the template structure is invalid or incomplete.<br/> |
| <dl> <dt>**WSEFAULT**</dt> </dl>  | One or more of the parameters is not a valid part of the user address space.<br/>                                                           |



 

## Remarks

In Windows Vista and later, this function always returns with an error.

The **WSCInstallQOSTemplate** function installs a QOS-named template containing the specified and subsequently associated [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure, or replaces settings of an existing template. Values are stored in nonvolatile storage, so subsequent calls to [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587), passing the same *lpQOSName*, return the **QOS** structure. If *lpProviderId* is set to **NULL**, the installed QOS-named template applies across all service providers; otherwise the QOS-named template applies only to the provider indicated by the *lpProviderId* parameter.

Windows Sockets 2 includes a base set of QOS templates. You can override and replace any of these QOS templates or change an existing QOS template by simply installing a new template with the existing name. You do not need to delete an existing template before replacing or modifying it. You cannot delete the base set of QOS-named templates included in Windows Sockets 2. However, you can delete templates added subsequently, perhaps by other service providers.

The *lpQOS* parameter, which points to a [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure, can include a [ProviderSpecific](the-providerspecific-buffer.md) buffer that will be stored with the basic **QOS** structure and returned in subsequent [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) calls.

You can provide the ProviderSpecific buffer even if *lpProviderId* is set to **NULL** to install global name templates that include provider-specific information. Note that this practice may lead the service provider to ignore the ProviderSpecific buffer if the service provider does not recognize its contents. The recommended use of **WSCInstallQOSTemplate** is to include a ProviderSpecific buffer only if the named template is being installed on a particular service provider, as implemented when *lpProviderId* is not **NULL**.

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

[**WPUGetQOSTemplate**](wpugetqostemplate.md)
</dt> <dt>

[**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587)
</dt> <dt>

[**WSCRemoveQOSTemplate**](wscremoveqostemplate.md)
</dt> </dl>

 

 





