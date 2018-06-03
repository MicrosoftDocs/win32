---
title: IpcGetTemplateList function
description: Returns official rights policy templates.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: e6762de3-9312-4f59-889a-c4db9a8fa800
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcGetTemplateList function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcGetTemplateList
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcGetTemplateList function

Returns official rights policy templates.

> [!Note]  
> Templates are available beginning with Windows Server 2003 with Service Pack 2 (SP2).

 

## Syntax


```C++
HRESULT WINAPI IpcGetTemplateList(
  _In_opt_   PCIPC_CONNECTION_INFO pConnectionInfo,
             DWORD                 dwFlags,
             LCID                  lcid,
  _In_opt_   PCIPC_PROMPT_CTX      pContext,
  _Reserved_ LPVOID                pvReserved,
  _Out_      PCIPC_TIL             *ppcTil
);
```



## Parameters

<dl> <dt>

*pConnectionInfo* \[in, optional\]
</dt> <dd>

Optional AD RMS server information from which to get templates. For more information, see [**IPC\_CONNECTION\_INFO**](ipc-connection-info.md).

</dd> <dt>

*dwFlags* 
</dt> <dd>

Specifies optional behavior for this function. For a list of optional flags, [**Get Template List Flags**](get-template-list-flags.md).

</dd> <dt>

*lcid* 
</dt> <dd>

The locale ID (LCID) to use for template names and descriptions.

When passing a nonzero value as the *lcid*, only information from templates that have a name and description for that *lcid* will be retrieved.

When zero is passed as the *lcid*, the RMS SDK 2.1 infrastructure follows a particular process, described in the Frequently asked questions section of the [Release notes](release-notes--rtm-.md) topic, to select a locale to use. For more information, see Release notes.

For more information about language IDs, see [Locale Identifiers](https://msdn.microsoft.com/library/windows/desktop/dd373763).

</dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

An optional pointer to an [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure. This can be used in cases where authentication prompts are not desired or when an application wants to control the modal behavior of any prompt dialog boxes.

</dd> <dt>

*pvReserved* 
</dt> <dd>

This parameter is reserved for future use and must be set to **NULL**.

</dd> <dt>

*ppcTil* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the buffer that contains the Template Information List. For more information, see [**IPC\_TIL**](ipc-til.md).

> [!Note]  
> The buffer is allocated by the RMS SDK 2.1 and must be freed by calling [**IpcFreeMemory**](ipcfreememory.md).

 

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_NEEDS\_ONLINE**
</dt> <dd>

Meaning: RMS SDK 2.1 needs network access to complete the operation, but the application requested offline mode.

Action: Call the function again, without specifying the **IPC\_PROMPT\_FLAG\_OFFLINE** flag. Typically, this flag is used in situations in which failure is acceptable and preferred to performing a network access. The system is already optimized to use the network only when absolutely necessary, so we do not recommend that developers use the **IPC\_PROMPT\_FLAG\_OFFLINE** flag as an optimization.

</dd> <dt>

**IPCERROR\_NEEDS\_UI**
</dt> <dd>

Meaning: The RMS SDK 2.1 needs to display a window to complete the operation, but the application requested silent mode.

Action: Call the function again, without specifying the **IPC\_PROMPT\_FLAG\_SILENT** flag.

</dd> <dt>

**IPCERROR\_LOCALE\_NOT\_FOUND**
</dt> <dd>

Meaning: The application specified a nonzero *lcid*, but no templates were available that had a descriptor in this locale.

Action: For more information about *lcid* see, the description of **IPC\_LI\_DESCRIPTOR** in [**License Property Types**](license-property-types.md). Also see the Frequently asked questions section of the [Release notes](release-notes--rtm-.md) topic.

</dd> </dl>

## Remarks

> [!Note]  
> Templates are available starting with Windows Server 2003 with SP2.

 

Typical application behavior:

-   When displaying template selection UI, it typically displays both **IPC\_TEMPLATE\_INFO::wszIssuerDisplayName** and **IPC\_TEMPLATE\_INFO::wszName** for each available template.
-   Extract **IPC\_TEMPLATE\_INFO::wszID** from the [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) selected by the user.
-   Pass the extracted **wszID** to [**IpcSerializeLicense**](ipcserializelicense.md) to generate a Rights Management Services (RMS) license.

All templates returned are sorted based on the issuer name in the [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) structure. Downloaded templates are cached locally and are not downloaded again on successive calls unless the cache is expired. To modify this behavior, set *dwFlags* to **IPC\_GTL\_FLAG\_FORCE\_DOWNLOAD**. For more information, see [**Get Template List Flags**](get-template-list-flags.md).

Because template updates can occur in the background, in general, applications should call **IpcGetTemplateList** immediately before presenting the templates to the user.

**IpcGetTemplateList** may initialize COM with the **COINIT\_APARTMENTTHREADED** flag to display user interface elements. As a result, callers who have initialized COM with the **COINIT\_MULTITHREADED** flag must use the **IpcGetTemplateList** function in silent mode by using the **IPC\_PROMPT\_FLAG\_SILENT** flag on with the [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**IPC\_CONNECTION\_INFO**](ipc-connection-info.md)
</dt> <dt>

[**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md)
</dt> <dt>

[**IPC\_TEMPLATE\_INFO**](ipc-template-info.md)
</dt> <dt>

[**IPC\_TIL**](ipc-til.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md)
</dt> <dt>

[**Get Template List Flags**](get-template-list-flags.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**License Property Types**](license-property-types.md)
</dt> <dt>

[Locale Identifiers](https://msdn.microsoft.com/library/windows/desktop/dd373763)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> <dt>

[Release notes](release-notes--rtm-.md)
</dt> </dl>

 

 





