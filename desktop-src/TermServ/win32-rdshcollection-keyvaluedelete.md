---
title: KeyValueDelete method of the Win32\_RDSHCollection class
description: Deletes the specified key (and associated value) from the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 968d6744-7b4a-45e5-87fb-90c408dbc771
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- KeyValueDelete method Remote Desktop Services
- KeyValueDelete method Remote Desktop Services , Win32_RDSHCollection class
- Win32_RDSHCollection class Remote Desktop Services , KeyValueDelete method
topic_type:
- apiref
api_name:
- Win32_RDSHCollection.KeyValueDelete
api_location:
- RDMS.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# KeyValueDelete method of the Win32\_RDSHCollection class

Deletes the specified key (and associated value) from the collection.

## Syntax


```mof
uint32 KeyValueDelete(
  [in] string Key
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The key to delete.

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

 

 





