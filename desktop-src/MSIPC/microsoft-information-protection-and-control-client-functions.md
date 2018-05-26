---
title: Functions
description: The platform provides the following functions.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 30462ABC-008E-4832-91A3-21A16A472960
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Functions

The platform provides the following functions.

Note that the functions relating to the File API, prefaced with *Ipcf* rather than *Ipc*, are grouped together at the end of the functions listing.

> [!Note]  
> For error condition processing, always use a call to [**IpcGetErrorMessageText**](ipcgeterrormessagetext.md) right after an SDK API call fails, so you get complete information about the nature of the error.

 

## In this section

<dl> <dt>

[*IPC\_OAUTH2\_CALLBACK*](ipc-oauth2-callback.md)
</dt> <dd>

A pointer to a function that is called when the RMS client requests an OAuth authentication token.

</dd> <dt>

[**IpcAccessCheck**](ipcaccesscheck.md)
</dt> <dd>

Checks whether a key object grants the requested right.

</dd> <dt>

[**IpcCloseHandle**](ipcclosehandle.md)
</dt> <dd>

Closes a handle.

</dd> <dt>

[**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
</dt> <dd>

Returns a handle to a license created from scratch.

</dd> <dt>

[**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md)
</dt> <dd>

Returns a handle to a license created from a template.

</dd> <dt>

[**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md)
</dt> <dd>

Creates a handle for create or modify operations on the metadata of the serialized license.

</dd> <dt>

[**IpcCreateOAuth2Token**](ipccreateoauth2token.md)
</dt> <dd>

Returns a handle to an authentication token object that is created from an authentication token string.

</dd> <dt>

[**IpcDecrypt**](ipcdecrypt.md)
</dt> <dd>

Decrypts encrypted data.

</dd> <dt>

[**IpcEncrypt**](ipcencrypt.md)
</dt> <dd>

Encrypts plaintext data.

</dd> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dd>

Frees a buffer allocated by another Rights Management Services SDK 2.1 function.

</dd> <dt>

[**IpcGetErrorMessageText**](ipcgeterrormessagetext.md)
</dt> <dd>

Returns the error message text associated with a supplied error code.

</dd> <dt>

[**IpcGetGlobalProperty**](ipcgetglobalproperty.md)
</dt> <dd>

Returns information about environment properties.

</dd> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dd>

Returns a handle to a key object created from a serialized license.

</dd> <dt>

[**IpcGetKeyProperty**](ipcgetkeyproperty.md)
</dt> <dd>

Returns requested property information.

</dd> <dt>

[**IpcGetLicenseProperty**](ipcgetlicenseproperty.md)
</dt> <dd>

Returns information about a license.

</dd> <dt>

[**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md)
</dt> <dd>

Retrieves the information available from a serialized license.

</dd> <dt>

[**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md)
</dt> <dd>

Returns available issuers of rights policy templates.

</dd> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dd>

Returns official rights policy templates.

</dd> <dt>

[**IpcInitialize**](ipcinitialize.md)
</dt> <dd>

Locates the installed version of Msipc.dll and calls the Windows [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) against it.

</dd> <dt>

[**IpcInitializeEnvironment**](ipcinitializeenvironment.md)
</dt> <dd>

Initializes the environment for use.

</dd> <dt>

[**IpcProtectWindow**](ipcprotectwindow.md)
</dt> <dd>

Protects a window by using mechanisms available on the current operating system.

</dd> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dd>

Serializes a license.

</dd> <dt>

[**IpcSetGlobalProperty**](ipcsetglobalproperty.md)
</dt> <dd>

Sets environment properties for the system.

</dd> <dt>

[**IpcSetLicenseProperty**](ipcsetlicenseproperty.md)
</dt> <dd>

Sets license properties for the platform.

</dd> <dt>

[**IpcUninitializeEnvironment**](ipcuninitializeenvironment.md)
</dt> <dd>

Un-initializes the environment.

</dd> <dt>

[**IpcUnprotectWindow**](ipcunprotectwindow.md)
</dt> <dd>

Removes the protection from a window protected using [**IpcProtectWindow**](ipcprotectwindow.md).

</dd> <dt>

[**IpcRegisterLicense**](ipcregisterlicense.md)
</dt> <dd>

Used to register the license with server.

</dd> <dt>

[**IpcSerializeLicenseWithMetadata**](ipcserializelicensemetadata.md)
</dt> <dd>

Used to finalize the metadata of the license and serialize it.

</dd> <dt>

[**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md)
</dt> <dd>

Used to set the metadata of the license.

</dd> <dt>

[File API](file-api.md)
</dt> <dd>

Functions relating to the File API.

</dd> </dl>

 

 




