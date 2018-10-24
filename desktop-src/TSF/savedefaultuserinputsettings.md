---
title: SaveDefaultUserInputSettings function
description: Applies the user keyboard layout and text service setting to the default user hive.
ms.assetid: ab3ec13f-fc5b-4c4d-ba11-679f97624651
keywords:
- SaveDefaultUserInputSettings function Text Services Framework
topic_type:
- apiref
api_name:
- SaveDefaultUserInputSettings
api_location:
- input.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SaveDefaultUserInputSettings function

Applies the user keyboard layout and text service setting to the default user hive.

## Syntax


```C++
BOOL CALLBACK SaveDefaultUserInputSettings(
  _In_ HWND hwndParent,
  _In_ HKEY hSourceRegKey
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

The parent window for the warning dialog box. The warning dialog box is not always shown and appears appropriately. If this parameter is NULL, the warning dialog box will not be shown.

</dd> <dt>

*hSourceRegKey* \[in\]
</dt> <dd>

The root registry key of the user setting to be copied.

</dd> </dl>

## Return value



| Return code                                                                          | Description                               |
|--------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | The function was successful.<br/>   |
| <dl> <dt>**FALSE**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Examples

There is no import library available that defines this function, so it is necessary to obtain a pointer to this function using [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212). The following example demonstrates how to obtain a pointer to this function.

> [!Note]  
> Using [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) incorrectly can compromise the security of your application by loading the wrong DLL. Refer to [Dynamic-Link Library Search Order](https://msdn.microsoft.com/library/windows/desktop/ms682586) for information on how to correctly load DLLs with different versions of Microsoft Windows.

 


```C++
typedef HRESULT (WINAPI *PTF_ SAVEDEFAULTUSERINPUTSETTINGS)(HWND hwndParent, HKEY hSourceRegKey);

HMODULE hInputDLL = LoadLibrary(TEXT("input.dll"));
BOOL bRet = FALSE;

if(hInputDLL == NULL)
{
    // Error loading module; fail as securely as possible. 
}
else
{
    PTF_ SAVEDEFAULTUSERINPUTSETTINGS pfnSaveDefaultUserInputSettings;
    
    pfnSaveDefaultUserInputSettings = (PTF_ SAVEDEFAULTUSERINPUTSETTINGS)GetProcAddress(hInputDLL, "SaveDefaultUserInputSettings ");

    if(pfnSaveDefaultUserInputSettings)
    {
        bRet = (*pfnSaveDefaultUserInputSettings)( hwndParent, hSourceRegKey);
    }

    FreeLibrary(hInputDLL);
}
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Input.dll</dt> </dl> |



 

 





