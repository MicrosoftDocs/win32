---
title: GetDataByFqdn method of the MsftSil\_GuestTasks class
description: This class has been removed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1a92c628-5a29-467f-bffc-018da13cb2b2
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDataByFqdn method Software Inventory Logging
- GetDataByFqdn method Software Inventory Logging , MsftSil_GuestTasks class
- MsftSil_GuestTasks class Software Inventory Logging , GetDataByFqdn method
topic_type:
- apiref
api_name:
- MsftSil_GuestTasks.GetDataByFqdn
api_location:
- SILProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetDataByFqdn method of the MsftSil\_GuestTasks class

This class has been removed.

**Windows Server 2012 R2:** Retrieves Software Inventory Logging data from the virtual machine with the specified fully qualified domain name.

## Syntax


```mof
uint32 GetDataByFqdn(
  [in]  string            fqdn,
  [out] MsftSil_GuestData objects[]
);
```



## Parameters

<dl> <dt>

*fqdn* \[in\]
</dt> <dd>

The fully qualified domain name of the virtual machine.

</dd> <dt>

*objects* \[out\]
</dt> <dd>

A [**MsftSil\_GuestData**](msftsil-guestdata.md) object that receives the Software Inventory Logging data from the guest operating system.

</dd> </dl>

## Return value

If this method succeeds, it returns 0. If this method fails, it returns 1. For a complete list of return values, see [**MI\_Result**](https://msdn.microsoft.com/library/hh437490) enumeration.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| End of client support<br/>    | None supported<br/>                                                                  |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MsftSil\_GuestTasks**](msftsil-guesttasks.md)
</dt> </dl>

 

 





