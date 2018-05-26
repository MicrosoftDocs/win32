---
title: License handle types
description: License handle types.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: B7CEEC45-2E0D-47C5-B1C3-A5EB7DCF3CA7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_MD_LICENSE_HANDLE
- IPC_SL_LICENSE_METADATA_HANDLE
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# License handle types

License handle types.

<dl> <dt>

<span id="IPC_MD_LICENSE_HANDLE"></span><span id="ipc_md_license_handle"></span>**IPC\_MD\_LICENSE\_HANDLE**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



License handle returned by [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md) or [**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md) is used as parameter.

**pvHandle** is of type [**IPC\_LICENSE\_HANDLE**](microsoft-information-protection-and-control-client-data-types.md) created using [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md) or [**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md).


</dt> </dl> </dd> <dt>

<span id="IPC_SL_LICENSE_METADATA_HANDLE"></span><span id="ipc_sl_license_metadata_handle"></span>**IPC\_SL\_LICENSE\_METADATA\_HANDLE**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



License metadata handle returned by [**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md) is used as parameter.

**pvHandle** is of type [**IPC\_LICENSE\_METADATA\_HANDLE**](microsoft-information-protection-and-control-client-data-types.md) created using [**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md).


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



 

 





