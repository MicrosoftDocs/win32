---
title: GetWindowsEventChannels method of the MSFT\_MTEventChannel class
description: Gets the list of those event channels that are connected to Windows event logs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4a42c8a5-8a83-45ec-9034-0a04d929a037'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetWindowsEventChannels method", "GetWindowsEventChannels method, MSFT_MTEventChannel class", "MSFT_MTEventChannel class, GetWindowsEventChannels method"]
---

# GetWindowsEventChannels method of the MSFT\_MTEventChannel class

Gets the list of those event channels that are connected to Windows event logs.

## Syntax


```mof
uint32 GetWindowsEventChannels(
  [out] MSFT_MTEventChannel Result[]
);
```



## Parameters

<dl> <dt>

*Result* \[out\]
</dt> <dd>

On success, returns an [**MSFT\_MTEventChannel**](msft-mteventchannel.md) containing the list of those event channels that are connected to Windows event logs.

</dd> </dl>

## Return value

TBD

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTEventChannel**](msft-mteventchannel.md)
</dt> </dl>

 

 





