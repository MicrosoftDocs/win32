---
title: SetDefaultLayoutOrTip function
description: Sets the specified keyboard layout or a text service as the default input item of the current user.
ms.assetid: e602065c-776b-47ba-b050-4325197e03de
keywords:
- SetDefaultLayoutOrTip function Text Services Framework
topic_type:
- apiref
api_name:
- SetDefaultLayoutOrTip
api_location:
- input.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# SetDefaultLayoutOrTip function

Sets the specified keyboard layout or a text service as the default input item of the current user.

## Syntax


```C++
BOOL CALLBACK SetDefaultLayoutOrTip(
  _In_ LPCWSTR           psz,
  _In_ LPCWSTR psz DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*psz* \[in\]
</dt> <dd>

A string that represents a keyboard layout list or a text services profile list.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A bitfield that specifies the following flags.

> [!Note]  
> The following identifiers are not defined in a public header file. You must either use the hexadecimal value or \#define the identifiers. For example, to use SDLOT\_NOAPPLYTOCURRENTSESSION you must include \#define SDLOT\_NOAPPLYTOCURRENTSESSION 0x00000001 in your code.

 



| Value                                                                                                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SDLOT_NOAPPLYTOCURRENTSESSION"></span><span id="sdlot_noapplytocurrentsession"></span><dl> <dt>**SDLOT\_NOAPPLYTOCURRENTSESSION**</dt> <dt>0x00000001</dt> </dl> | Stores the setting in the registry but dose not update the runtime keyboard setting of the current session. If the alternative registry path is set in [**SetDefaultLayoutOrTipUserReg**](/windows/desktop/TSF/setdefaultlayoutortipuserreg), this flag should be set.<br/> |
| <span id="SDLOT_APPLYTOCURRENTTHREAD"></span><span id="sdlot_applytocurrentthread"></span><dl> <dt>**SDLOT\_APPLYTOCURRENTTHREAD**</dt> <dt>0x00000002</dt> </dl>          | Applies the setting immediately on the current thread.<br/>                                                                                                                                                                                                |



 

</dd> </dl>

## Return value



| Return code                                                                          | Description                               |
|--------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | The function was successful.<br/>   |
| <dl> <dt>**FALSE**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

The string format of the layout list is:

\<LangID 1\>:\<KLID 1\>;\[...\<LangID N\>:\<KLID N\>

The string format of the text service profile list is:

\<LangID 1\>:{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx};

The following is an example of a value for the *psz* parameter:


```C++
"0x0407:0x00000407"
"0x0407:0x00000407;0x040C:0x0000040C"
"0x0407:0x00000407;0x0412:{A028AE76-01B1-46C2-99C4-ACD9858AE02F}{B5FE1F02-D5F2-4445-9C03-C568F23C99A1};0x040C:0x0000040C"
```



## Examples

There is no import library available that defines this function, so it is necessary to obtain a pointer to this function using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress). The following example demonstrates how to obtain a pointer to this function.

> [!Note]  
> Using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) incorrectly can compromise the security of your application by loading the wrong DLL. Refer to [Dynamic-Link Library Search Order](/windows/desktop/Dlls/dynamic-link-library-search-order) for information on how to correctly load DLLs with different versions of Microsoft Windows.

 


```C++
typedef HRESULT (WINAPI *PTF_ SETDEFAULTLAYOUTORTIP)(LPCWSTR psz);

HMODULE hInputDLL = LoadLibrary(TEXT("input.dll"));
BOOL bRet = FALSE;

if(hInputDLL == NULL)
{
    // Error loading module; fail as securely as possible. 
}
else
{
    PTF_ SETDEFAULTLAYOUTORTIP pfnSetDefaultLayoutOrTip;
    
    pfnSetDefaultLayoutOrTip = (PTF_ SETDEFAULTLAYOUTORTIP)GetProcAddress(hInputDLL, "SetDefaultLayoutOrTip");

    if(pfnSetDefaultLayoutOrTip)
    {
        bRet = (*pfnSetDefaultLayoutOrTip)(psz);
    }

    FreeLibrary(hInputDLL);
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Input.dll</dt> </dl> |



 

