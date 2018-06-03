---
title: IpcRegisterLicense function
description: Used to register the license with server.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: C48AEBF7-D812-4952-8B91-80445C928FF3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcRegisterLicense function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcRegisterLicense
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcRegisterLicense function

Used to register the license with server. This function is used for content tracking purposes.

> \[!Important\]
>
> An application needs to use this API to register the PL of every protected document with the server. If this step is missed, the document will not be tracked.

 

For more information on content tracking and the use of this function, see [Tracking Content](tracking-content.md).

## Syntax


```C++
HRESULT WINAPI IpcRegisterLicense(
  _In_       PCIPC_BUFFER     pvLicenseWithMetadata,
  _Reserved_ LPVOID           pvReserved,
  _In_opt_   PCIPC_PROMPT_CTX pContext,
  _In_opt_   LPCWSTR          wszContentName,
             BOOL             fSendRegistrationMail
);
```



## Parameters

<dl> <dt>

*pvLicenseWithMetadata* \[in\]
</dt> <dd>

Pointer to the serialized license with the metadata information added.

</dd> <dt>

*pvReserved* 
</dt> <dd>

This is a reserved. The parameter must be set to NULL.

</dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

Optional pointer to information that helps the IPC Client decide what the user prompt behavior should be.

This parameter can be used in cases where authentication prompts are not desirable or when an application wants to control the modal behavior of prompt dialogs.

</dd> <dt>

*wszContentName* \[in, optional\]
</dt> <dd>

If *pvLicenseWithMetadata* does not specify a content name, the server will use this parameter, otherwise it will be ignored.

</dd> <dt>

*fSendRegistrationMail* 
</dt> <dd>

Set to **TRUE** to notify the publisher via email of the tracking portal URL to manage the document, or **FALSE** to not send the notification.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**E\_INVALIDARG**
</dt> <dt>

**IPCERROR\_NEEDS\_ONLINE**
</dt> </dl>

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

[**License metadata property types**](license-metadata-property-types.md)
</dt> <dt>

[**Notification preference**](notification-preference.md)
</dt> <dt>

[**Notification type**](notification-type.md)
</dt> <dt>

[**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md)
</dt> <dt>

[**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md)
</dt> <dt>

[**IpcSerializeLicenseWithMetadata**](ipcserializelicensemetadata.md)
</dt> <dt>

[**IpcfEncryptFileWithMetadata**](ipcfencryptfilewithmetadata.md)
</dt> <dt>

[**IpcfEncryptFileStreamWithMetadata**](ipcfencryptfilestreamwithmetadata.md)
</dt> <dt>

[**IpcRegisterLicense**](ipcregisterlicense.md)
</dt> </dl>

 

 





