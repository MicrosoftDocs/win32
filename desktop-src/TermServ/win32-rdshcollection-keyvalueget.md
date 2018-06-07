---
title: KeyValueGet method of the Win32\_RDSHCollection class
description: Retrieves the value associated with the specified key in the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 69d309a4-b32e-4dbc-bd28-be79d395ac26
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- KeyValueGet method Remote Desktop Services
- KeyValueGet method Remote Desktop Services , Win32_RDSHCollection class
- Win32_RDSHCollection class Remote Desktop Services , KeyValueGet method
topic_type:
- apiref
api_name:
- Win32_RDSHCollection.KeyValueGet
api_location:
- RDMS.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# KeyValueGet method of the Win32\_RDSHCollection class

Retrieves the value associated with the specified key in the collection.

## Syntax


```mof
uint32 KeyValueGet(
  [in]  string Key,
  [out] string Value
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The key that identifies the value you wish to retrieve.

</dd> <dt>

*Value* \[out\]
</dt> <dd>

On success, returns the value associated with the specified key.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDSHCollection**](win32-rdshcollection.md)
</dt> </dl>

 

 





