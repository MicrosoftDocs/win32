---
title: CreateVPNConnection function
description: Creates a VPN connection.
ms.assetid: '3d4a3b5d-b7fa-426f-bc71-15a4c38c4e7b'
keywords: ["CreateVPNConnection function Get Connected Wizard API"]
topic_type:
- apiref
api_name:
- CreateVPNConnection
api_location:
- connect.dll
api_type:
- DllExport
---

# CreateVPNConnection function

The **CreateVPNConnection** function creates a VPN connection.

## Syntax


```C++
HRESULT WINAPI CreateVPNConnection(
  _In_     const HWND   hwndParent,
  _In_     const DWORD  dwWizardType,
  _In_     const DWORD  dwContextFlags,
  _In_     const DWORD  dwUserFlags,
  _In_     const HANDLE hUserContext,
  _In_opt_       LPWSTR pszCommandLine
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

Unlike [**GetVPNConnected**](getvpnconnected.md), this function does not attempt to repair an existing connection to a VPN, but creates a new and separate connection entirely.

An import library containing the **CreateVPNConnection** function is not included in the Microsoft Windows Software Development Kit (SDK). Applications must use the [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to retrieve the function pointer from the corresponding DLL and call this function.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Connect.dll</dt> </dl> |



 

 





