---
title: IpcSerializeLicense function
description: Serializes a license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 355bef41-bcef-403d-8d3e-b7b526401d39
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcSerializeLicense function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcSerializeLicense
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcSerializeLicense function

Serializes a license.

Serialization is the final mandatory step that is needed before the license can be used for encryption. Call this function to finalize a license. This applies to [**IpcEncrypt**](ipcencrypt.md) but not [**IpcfEncryptFile**](ipcfencryptfile.md).

## Syntax


```C++
HRESULT WINAPI IpcSerializeLicense(
  _In_      LPCVOID          pvLicenseInfo,
            DWORD            dwType,
            DWORD            dwFlags,
  _In_opt_  PCIPC_PROMPT_CTX pContext,
  _Out_opt_ PIPC_KEY_HANDLE  phKey,
  _Out_     PIPC_BUFFER      *ppvLicense
);
```



## Parameters

<dl> <dt>

*pvLicenseInfo* \[in\]
</dt> <dd>

A pointer to the template ID or a license handle, depending on the value of the *dwType* parameter. The template ID or license handle identifies the license to be serialized.

</dd> <dt>

*dwType* 
</dt> <dd>

The type of data for the *pvLicenseInfo* parameter.

<dt>

<span id="IPC_SL_TEMPLATE_ID"></span><span id="ipc_sl_template_id"></span>

<span id="IPC_SL_TEMPLATE_ID"></span><span id="ipc_sl_template_id"></span>**IPC\_SL\_TEMPLATE\_ID** (1)


</dt> <dd>

Generate a serialized license based on a supplied Rights Management Services (RMS) Template ID. *pvLicenseInfo* must contain an **LPCWSTR** that represents the template ID. The template ID must be computed by calling [**IpcGetTemplateList**](ipcgettemplatelist.md), and extracting the **wszID** field from one of the returned [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) structures.

</dd> <dt>

<span id="IPC_SL_LICENSE_HANDLE"></span><span id="ipc_sl_license_handle"></span>

<span id="IPC_SL_LICENSE_HANDLE"></span><span id="ipc_sl_license_handle"></span>**IPC\_SL\_LICENSE\_HANDLE** (2)


</dt> <dd>

A license handle returned by the [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md) or [**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md) function that is used to serialize the license. *pvLicenseInfo* is of type **IPC\_LICENSE\_HANDLE** and points to the returned handle.

</dd> </dl> </dd> <dt>

*dwFlags* 
</dt> <dd>

Specifies optional behavior for this function.

<dt>

<span id="IPC_SL_FLAG_DEFAULT"></span><span id="ipc_sl_flag_default"></span>

<span id="IPC_SL_FLAG_DEFAULT"></span><span id="ipc_sl_flag_default"></span>**IPC\_SL\_FLAG\_DEFAULT** (0)


</dt> <dd>

Uses all of the default settings for **IpcSerializeLicense**. Most applications should use this flag when serializing a license.

</dd> <dt>

<span id="IPC_SL_FLAG_KEY_NO_PERSIST"></span><span id="ipc_sl_flag_key_no_persist"></span>

<span id="IPC_SL_FLAG_KEY_NO_PERSIST"></span><span id="ipc_sl_flag_key_no_persist"></span>**IPC\_SL\_FLAG\_KEY\_NO\_PERSIST** (2)


</dt> <dd>

Use this flag to prevent a key from being cached locally and inserted within the serialized license. If this flag is used, the content creator must contact the RMS server in order to access the content.

> [!Note]  
> If this flag is used, the creator of the serialized license will require a network connection to the RMS server if they attempt to create a key from it using [**IpcGetKey**](ipcgetkey.md).

 

</dd> <dt>

<span id="IPC_SL_FLAG_KEY_NO_PERSIST_DISK"></span><span id="ipc_sl_flag_key_no_persist_disk"></span>

<span id="IPC_SL_FLAG_KEY_NO_PERSIST_DISK"></span><span id="ipc_sl_flag_key_no_persist_disk"></span>**IPC\_SL\_FLAG\_KEY\_NO\_PERSIST\_DISK** (4)


</dt> <dd>

Use this flag to prevent the content key from being cached locally. The content key will still be cached in the serialized license.

</dd> <dt>

<span id="IPC_SL_FLAG_DEPRECATED_UNSIGNED_LICENSE_TEMPLATE"></span><span id="ipc_sl_flag_deprecated_unsigned_license_template"></span>

<span id="IPC_SL_FLAG_DEPRECATED_UNSIGNED_LICENSE_TEMPLATE"></span><span id="ipc_sl_flag_deprecated_unsigned_license_template"></span>**IPC\_SL\_FLAG\_DEPRECATED\_UNSIGNED\_LICENSE\_TEMPLATE** (8)


</dt> <dd>

This flag should only be used by applications that protect content using functions of the MSDRM library. For more information, see [AD RMS Functions](https://msdn.microsoft.com/library/bb204612). Passing this flag will generate an issuance license template that is compatible with MSDRM.

> \[!Important\]
>
> Licenses that are created with this flag cannot be used with RMS SDK 2.1. This flag cannot be combined with any other flag.

 

</dd> <dt>

<span id="IPC_SL_FLAG_KEY_NO_PERSIST_LICENSE"></span><span id="ipc_sl_flag_key_no_persist_license"></span>

<span id="IPC_SL_FLAG_KEY_NO_PERSIST_LICENSE"></span><span id="ipc_sl_flag_key_no_persist_license"></span>**IPC\_SL\_FLAG\_KEY\_NO\_PERSIST\_LICENSE** (16)


</dt> <dd>

Use this flag to prevent an encrypted copy of this key from being cached within the serialized license. The key may still be cached locally on disk.

> [!Note]  
> If you are storing confidential information in the AppSpecific data field, you should specify the IPC\_SL\_FLAG\_KEY\_NO\_PERSIST\_LICENSE when serializing your license so your information will remain confidential.

 

</dd> </dl> </dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

An optional pointer to an [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure. This can be used in cases where authentication prompts are not desirable or when an application wants to control the modal behavior of any prompt dialogs.

</dd> <dt>

*phKey* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives a handle to the key object corresponding to the owner license that can be used for encrypting with the serialized license.

</dd> <dt>

*ppvLicense* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the buffer that contains the serialized license. The buffer is allocated by the IPC Client and must be freed using [**IpcFreeMemory**](ipcfreememory.md).

</dd> </dl>

## Return value

If the function succeeds the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_ISSUANCELICENSE\_LENGTH\_LIMIT\_EXCEEDED**
</dt> <dd>

Meaning: Returns this value when the user rights list is too large and the call would have produced a serialized license that exceeds the limits put in place by the RMS system. This is a common occurrence for applications that expand groups and attempt to assign them to the license (for example, a mail client like Outlook).

Action: We recommend that your application user interface prompt the user to express the user rights list by using distribution groups instead of individual user's email addresses.

</dd> <dt>

**IPCERROR\_NEEDS\_ONLINE**
</dt> <dd>

Meaning: The RMS SDK 2.1 needs network access to complete the operation, but the application requested offline mode.

Action: Call the function again, without specifying the **IPC\_PROMPT\_FLAG\_OFFLINE** flag. Typically, this flag is used in situations in which failure is acceptable and preferred to performing a network access. The system is already optimized to use the network only when absolutely necessary, so we do not recommend that developers use the **IPC\_PROMPT\_FLAG\_OFFLINE** flag as an optimization.

</dd> <dt>

**IPCERROR\_NEEDS\_UI**
</dt> <dd>

Meaning: RMS SDK 2.1 needs to display a window to complete the operation, but the application requested silent mode.

Action: Call the function again, without specifying the **IPC\_PROMPT\_FLAG\_SILENT** flag.

</dd> <dt>

**IPCERROR\_RIGHT\_NOT\_GRANTED**
</dt> <dd>

Meaning: The user does not have the rights required to serialize this license.

This error can be returned in the following scenarios:

<dl> <dd>1. A license handle is created using either [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md) or [**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md).</dd> <dd>2. Setting the content key on a license handle created in \#1 using [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md) with the **IPC\_LI\_CONTENT\_KEY**.</dd> <dd>3. The user does not have **IPC\_WRITE\_RIGHTS** on the key handle used in \#2.</dd> </dl>

Action: If you serialized a license on which you had set the **IPC\_LI\_CONTENT\_KEY** property, inform the user that they do not have rights to change the access policy for this content.

</dd> <dt>

**IPCERROR\_USER\_RIGHTS\_NOT\_SET**
</dt> <dd>

Meaning: The license handle specified by *pvLicenseInfo* does not have a user rights list specified.

Action: Add user rights to the license handle by calling [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md) with *dwPropID* set to **IPC\_LI\_USER\_RIGHTS\_LIST**. For an example of how to add user rights to a license, see the example in [add explicit owner rights](add-explicit-owner-rights.md).

</dd> </dl>

## Remarks

**IpcSerializeLicense** may initialize COM with the **COINIT\_APARTMENTTHREADED** flag to display user interface elements. As a result, callers who have initialized COM with the **COINIT\_MULTITHREADED** flag must use the **IpcSerializeLicense** function in silent mode by using the **IPC\_PROMPT\_FLAG\_SILENT** flag with the [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure.

License buffer data is encoded in UTF8 when using the default flags and UTF16 when using the **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** flag.

If you are storing confidential information in the **AppSpecific** data field, you should specify the **IPC\_SL\_FLAG\_KEY\_NO\_PERSIST\_LICENSE** when serializing your license (**IpcSerializeLicense**) so your information will remain confidential.

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

[**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md)
</dt> <dt>

[**IPC\_TEMPLATE\_INFO**](ipc-template-info.md)
</dt> <dt>

[**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
</dt> <dt>

[**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





