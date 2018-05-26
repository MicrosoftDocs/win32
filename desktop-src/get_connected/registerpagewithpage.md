---
title: RegisterPageWithPage function
description: Registers external pages with existing pages in the Get Connected Wizard.
ms.assetid: 20534226-1402-432b-9115-995c60bb3d11
keywords:
- RegisterPageWithPage function Get Connected Wizard API
topic_type:
- apiref
api_name:
- RegisterPageWithPage
api_location:
- connect.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RegisterPageWithPage function

The **RegisterPageWithPage** function registers external pages with existing pages in the Get Connected Wizard.

## Syntax


```C++
HRESULT WINAPI RegisterPageWithPage(
           const GUID   *pguidParentPage,
           const GUID   *pguidChildPage,
  _In_opt_ const LPWSTR pszChildModuleFileName,
  _In_opt_ const LPWSTR pszFriendlyName,
  _In_     const DWORD  dwBehaviorFlags,
  _In_     const DWORD  dwUserFlags,
  _In_opt_       LPWSTR pszCommandLine
);
```



## Parameters

<dl> <dt>

*pguidParentPage* 
</dt> <dd>

Pointer to a GUID that uniquely identifies the parent page within the wizard.

</dd> <dt>

*pguidChildPage* 
</dt> <dd>

Pointer to a GUID that uniquely identifies the child page to register with the parent page.

</dd> <dt>

*pszChildModuleFileName* \[in, optional\]
</dt> <dd>

A Unicode string that contains the installation filename and path of the module for the child page.

This parameter is optional and can be set to **NULL**.

</dd> <dt>

*pszFriendlyName* \[in, optional\]
</dt> <dd>

Unicode string that contains the display name of the child page to register.

This parameter is optional and can be set to **NULL**.

</dd> <dt>

*dwBehaviorFlags* \[in\]
</dt> <dd>

A set of user-defined behavior flags.

This parameter is optional and can be set to 0.

</dd> <dt>

*dwUserFlags* \[in\]
</dt> <dd>

A set of user-defined registration flags.

This parameter is optional and can be set to 0.

</dd> <dt>

*pszCommandLine* \[in, optional\]
</dt> <dd>

User command line parameters to use when invoking the child module, if any.

This parameter is optional and can be set to **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return value is S\_OK.

If the page is already registered, the return value is S\_FALSE.

If the function fails, the return value is one of the standard error codes.



| Return code                                                                                    | Description                                               |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl> | The component to register is currently in use.<br/> |



 

## Remarks

A *page* is a user interface form within the Wizard, usually corresponding to a specific step or steps. For example, one page might be the form the describes an IP address and prompts the user to provide IP address data. *Child pages* are pages that are accessible from a parent page; for example, clicking a "More Information" button or link on a page will take you a child page that contains the requested information.

An import library containing the **RegisterPageWithPage** function is not included in the Microsoft Windows Software Development Kit (SDK). Applications must use the [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to retrieve the function pointer from the corresponding DLL and call this function.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Connect.dll</dt> </dl> |



 

 





