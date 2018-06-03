---
title: UnregisterPagesLink function
description: Removes a registration link between two pages created with the RegisterPageWithPage function.
ms.assetid: 78298ab2-60bb-4db1-ad6c-84d8b29c754a
keywords:
- UnregisterPagesLink function Get Connected Wizard API
topic_type:
- apiref
api_name:
- UnregisterPagesLink
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

# UnregisterPagesLink function

The **UnregisterPagesLink** function removes a registration link between two pages created with the [**RegisterPageWithPage**](registerpagewithpage.md) function.

## Syntax


```C++
HRESULT WINAPI UnregisterPagesLink(
  _In_ const GUID *pguidParentPage,
  _In_ const GUID *pguidChildPage
);
```



## Parameters

<dl> <dt>

*pguidParentPage* \[in\]
</dt> <dd>

Pointer to a GUID that uniquely identifies the parent page whose link to a child page will be removed.

</dd> <dt>

*pguidChildPage* \[in\]
</dt> <dd>

Pointer to a GUID that uniquely identifies the child page whose link will be removed.

</dd> </dl>

## Return value

If the function succeeds, the return value is S\_OK.

If the link has been previously removed, the return value is S\_FALSE.

If the method fails, the return value is one of the standard error codes.

## Remarks

An import library containing the **UnregisterPagesLink** function is not included in the Microsoft Windows Software Development Kit (SDK). Applications must use the [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to retrieve the function pointer from the corresponding DLL and call this function.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Connect.dll</dt> </dl> |



 

 





