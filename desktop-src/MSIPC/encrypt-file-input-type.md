---
title: Encrypt file input type
description: Constants for specifying the type of license information.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '3675FC03-BEC0-4BAC-BA9D-65E34AA66AD7'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPCF_EF_TEMPLATE_ID
- IPCF_EF_LICENSE_HANDLE
api_location:
- Ipcfile.h
api_type:
- HeaderDef
---

# Encrypt file input type

Constants for specifying the type of license information. The template/license will be used to create a key to encrypt a file.

<dl> <dt>

<span id="IPCF_EF_TEMPLATE_ID"></span><span id="ipcf_ef_template_id"></span>**IPCF\_EF\_TEMPLATE\_ID**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



A template ID that represents an official template.

The *pvTemplateInfo* parameter should be of type **PWSTR** representing a Template ID which can be retrieved by calling [**IpcGetTemplateList**](ipcgettemplatelist.md).


</dt> </dl> </dd> <dt>

<span id="IPCF_EF_LICENSE_HANDLE"></span><span id="ipcf_ef_license_handle"></span>**IPCF\_EF\_LICENSE\_HANDLE**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



A license handle. The *pvLicenseInfo* parameter is of type **IPC\_LICENSE\_HANDLE** created by calling [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md) or [**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md).


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |



 

 





