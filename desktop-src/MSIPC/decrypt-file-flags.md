---
title: Decrypt file flags
description: Constants for specifying file decryption behavior.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: C34F8ABD-6395-4C30-B62D-A1A498D4BC40
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPCF_DF_FLAG_DEFAULT
- IPCF_DF_FLAG_OPEN_AS_RMS_AWARE
api_location:
- Ipcfile.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Decrypt file flags

Constants for specifying file decryption behavior.

<dl> <dt>

<span id="IPCF_DF_FLAG_DEFAULT"></span><span id="ipcf_df_flag_default"></span>**IPCF\_DF\_FLAG\_DEFAULT**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Specifies that default settings should be used. For usage, see for [**IpcfDecryptFile**](ipcfdecryptfile.md).


</dt> </dl> </dd> <dt>

<span id="IPCF_DF_FLAG_OPEN_AS_RMS_AWARE"></span><span id="ipcf_df_flag_open_as_rms_aware"></span>**IPCF\_DF\_FLAG\_OPEN\_AS\_RMS\_AWARE**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Allows applications to decrypt the file, even if the EXTRACT right is not granted.

Applications that pass this flag must ensure that all RMS rights are enforced, including but not limited to:

EXTRACT   if this right is not granted, the application will ensure that all decrypted copies of this content are deleted after use. If decrypted content is displayed to the user (e.g., in an editor), the application will block clipboard access and screen capture for this content (see: [**IpcfGetSerializedLicenseFromFile**](ipcfgetserializedlicensefromfile.md), [**IpcGetKey**](ipcgetkey.md), [**IpcAccessCheck**](ipcaccesscheck.md), and [**IpcProtectWindow**](ipcprotectwindow.md).

For a complete list of rights that your application must support, see [Usage restriction reference](usage-restriction-reference.md).


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |



 

 





