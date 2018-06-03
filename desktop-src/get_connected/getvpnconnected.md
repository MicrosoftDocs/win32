---
title: GetVPNConnected function
description: Launches the Get Connected wizard within the calling application to enable virtual private network (VPN) connectivity.
ms.assetid: fbdacda7-979d-4cbc-b33a-6adee742c3b8
keywords:
- GetVPNConnected function Get Connected Wizard API
topic_type:
- apiref
api_name:
- GetVPNConnected
api_location:
- connect.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetVPNConnected function

The **GetVPNConnected** function launches the Get Connected wizard within the calling application to enable virtual private network (VPN) connectivity.

## Syntax


```C++
HRESULT WINAPI GetVPNConnected(
  _In_     const HWND   hwndParent,
  _In_     const DWORD  dwWizardType,
  _In_     const DWORD  dwContextFlags,
  _In_     const DWORD  dwUserFlags,
  _In_     const HANDLE hUserContext,
  _In_opt_       LPWSTR pszCommandLine
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Handle to the parent window that called this API.

This parameter is optional and can be set to **NULL**.

</dd> <dt>

*dwWizardType* \[in\]
</dt> <dd>

Specifies the style of the Get Connected wizard to be launched.

This parameter is optional and can be set to 0.



| Value                                                                           | Meaning                   |
|---------------------------------------------------------------------------------|---------------------------|
| <dl> <dt>0x00</dt> </dl> | Default style.<br/> |



 

</dd> <dt>

*dwContextFlags* \[in\]
</dt> <dd>

A set of context flags that describes wizard behaviors.

This parameter is optional and can be set to 0.



| Value                                                                           | Meaning                                                                                         |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>0x00</dt> </dl> | The wizard returns the results synchronously and blocks until this call is complete.<br/> |
| <dl> <dt>0x1</dt> </dl>  | The wizard returns the results immediately and asynchronously via a Windows event.<br/>   |



 

</dd> <dt>

*dwUserFlags* \[in\]
</dt> <dd>

A set of user-defined application-specific flags. These flags are defined and interpreted by the calling application.

This parameter is optional and should be set to 0 by default.

</dd> <dt>

*hUserContext* \[in\]
</dt> <dd>

User context handle for the parent application thread.

This parameter is optional and should be set to **NULL** by default.

</dd> <dt>

*pszCommandLine* \[in, optional\]
</dt> <dd>

User command line parameters, if any.

This parameter is optional and can be set to **NULL**.

The following command-line options are supported:



| Value                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="-HideFinishPage"></span><span id="-hidefinishpage"></span><span id="-HIDEFINISHPAGE"></span><dl> <dt>**-HideFinishPage**</dt> </dl>                                     | Hide the Finish page of the Get Connected wizard.<br/>                                                                                                                                                                                                                                                                                                        |
| <span id="-SkipInternetDetection"></span><span id="-skipinternetdetection"></span><span id="-SKIPINTERNETDETECTION"></span><dl> <dt>**-SkipInternetDetection**</dt> </dl>         | Do not display the Get Connected wizard page that shows whether or not the user has a working or active Internet connection. <br/>                                                                                                                                                                                                                            |
| <span id="-SkipExistingConnections"></span><span id="-skipexistingconnections"></span><span id="-SKIPEXISTINGCONNECTIONS"></span><dl> <dt>**-SkipExistingConnections**</dt> </dl> | Do not display the Get Connected wizard page that shows a list of existing Internet connections. This command-line option is commonly used when creating additional Internet connections after one has been previously established, and to prevent novice users from creating a completely new connection each time they attempt to access the Internet.<br/> |



 

</dd> </dl>

## Return value

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the standard error codes.

## Remarks

This API attempts to connect the current user to a VPN. This process can involve creating a new connection, or repairing an existing one.

Note that while this API might indicate that the user is connected to a VPN, resources within that VPN may remain unavailable due to VPN configuration or infrastructure settings.

To launch a Get Connected wizard for an Internet connection, call the [**GetInternetConnected**](getinternetconnected.md) API.

To launch a Get Connected wizard for an local network (LAN) connection, call the [**GetNetworkConnected**](getnetworkconnected.md) API.

An import library containing the **GetVPNConnected** function is not included in the Microsoft Windows Software Development Kit (SDK). Applications must use the [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to retrieve the function pointer from the corresponding DLL and call this function.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Connect.dll</dt> </dl> |



 

 





