---
title: Remove method of the MSFT\_SMProvider class
description: Removes the provider from the cache.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a0df23cc-cf04-4b24-97f5-2624d73fbf33
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, MSFT_SMProvider class
- MSFT_SMProvider class, Remove method
topic_type:
- apiref
api_name:
- MSFT_SMProvider.Remove
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the MSFT\_SMProvider class

Removes the provider from the cache.

## Syntax


```mof
Uint32 Remove(
  [in]            String                username,
  [in]            String                password,
  [in, optional]  Boolean               force,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*username* \[in\]
</dt> <dd>

The username to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> <dt>

*force* \[in, optional\]
</dt> <dd>

Indicates whether this method uses the default confirmation prompt before performing the operation. **True** to use the default confirmation prompt, otherwise **false**. The default value for this parameter is **True**.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMProvider**](msft-smprovider.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





