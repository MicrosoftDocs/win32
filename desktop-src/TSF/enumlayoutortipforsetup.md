---
title: EnumLayoutOrTipForSetup function
description: Enumerates the installed keyboard layouts and text services of the setup UI or OOBE.
ms.assetid: 3c6fc11c-36a5-4718-b584-b7f98f1b4180
keywords:
- EnumLayoutOrTipForSetup function Text Services Framework
topic_type:
- apiref
api_name:
- EnumLayoutOrTipForSetup
api_location:
- input.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# EnumLayoutOrTipForSetup function

Enumerates the installed keyboard layouts and text services of the setup UI or OOBE.

## Syntax


```C++
UINT CALLBACK EnumLayoutOrTipForSetup(
  _In_  LANGID      langid,
  _Out_ LAYOUTORTIP *pLayoutOrTip,
  _In_  UINT        uBufLength,
  _In_  DWORD       dwFlags
);
```



## Parameters

<dl> <dt>

*langid* \[in\]
</dt> <dd>

The language id of the item to be enumerated.

</dd> <dt>

*pLayoutOrTip* \[out\]
</dt> <dd>

Pointer to the buffer that receives the array of LAYOUTORTIP structures. This can be **NULL** to get the number of items.

</dd> <dt>

*uBufLength* \[in\]
</dt> <dd>

The length of the buffer pointed to by *pLayoutOrTip*. This is ignored if *pLayoutOrTip* is **NULL**.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Not used. This must be zero.

</dd> </dl>

## Return value

If *pLayoutOrTip* is **NULL**, the number of keyboard items that are registered in System; otherwise, the number of keyboard items that are copied into *pLayoutOrTip*.

## Remarks

There is no import library available that defines this function, so it is necessary to obtain a pointer to this function using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress).

> [!Note]  
> Using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) incorrectly can compromise the security of your application by loading the wrong DLL. Refer to [Dynamic-Link Library Search Order](/windows/desktop/Dlls/dynamic-link-library-search-order) for information on how to correctly load DLLs with different versions of Microsoft Windows.

 

The definition of LAYOUTORTIP is:

``` syntax
typedef struct tagLAYOUTORTIP {
    DWORD dwFlags;
#define LOT_DEFAULT    0x0001 // If this is on, this is a default item. 
#define LOT_DISABLED   0x0002 // if this is on, this is not enabled. 
    WCHAR szId[MAX_PATH]; // Id of the keyboard item in the string format. 
    WCHAR szName[MAX_PATH]; // The description of the keyboard item. 
} LAYOUTORTIP;
```

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Input.dll</dt> </dl> |



 

