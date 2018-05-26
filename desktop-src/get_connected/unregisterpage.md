---
title: UnregisterPage function
description: Removes a page from the Get Connected Wizard that was added with the RegisterPageWithPage function.
ms.assetid: 488b1a0c-511f-49c4-9cec-8e643956d1c8
keywords:
- UnregisterPage function Get Connected Wizard API
topic_type:
- apiref
api_name:
- UnregisterPage
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

# UnregisterPage function

The **UnregisterPage** function removes a page from the Get Connected Wizard that was added with the [**RegisterPageWithPage**](registerpagewithpage.md) function. This function also removes the links between the page and all other pages that linked to it.

## Syntax


```C++
HRESULT WINAPI UnregisterPage(
  _In_ const GUID *pguidPage,
  _In_ const BOOL fUnregisterFromCOM
);
```



## Parameters

<dl> <dt>

*pguidPage* \[in\]
</dt> <dd>

Pointer to a GUID that uniquely identifies the page to be removed from the Get Connected wizard.

</dd> <dt>

*fUnregisterFromCOM* \[in\]
</dt> <dd>

Specifies if the page module must be deregistered with COM. Set this parameter to **TRUE** if the page module must be deregistered with COM or **FALSE** if it has no module to deregister.

</dd> </dl>

## Return value

If the function succeeds, the return value is S\_OK.

If the page is already deregistered, the return value is S\_FALSE.

If the method fails, the return value is one of the standard error codes.



| Return code                                                                                    | Description                                            |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl> | The page to deregister is currently in use.<br/> |



 

## Remarks

An import library containing the **UnregisterPage** function is not included in the Microsoft Windows Software Development Kit (SDK). Applications must use the [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to retrieve the function pointer from the corresponding DLL and call this function.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Connect.dll</dt> </dl> |



 

 





