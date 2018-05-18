---
title: GetProvidersAndWindowsEventChannels method of the MSFT\_MTEventProvider class
description: Gets the list of those event providers that export at least one event channel. Also gets the list of those event channels that are connected to Windows event logs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e5df8e66-1b4a-4d99-b675-f22f6dec9ee0'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetProvidersAndWindowsEventChannels method", "GetProvidersAndWindowsEventChannels method, MSFT_MTEventProvider class", "MSFT_MTEventProvider class, GetProvidersAndWindowsEventChannels method"]
---

# GetProvidersAndWindowsEventChannels method of the MSFT\_MTEventProvider class

Gets the list of those event providers that export at least one event channel. Also gets the list of those event channels that are connected to Windows event logs.

## Syntax


```mof
uint32 GetProvidersAndWindowsEventChannels(
  [out] MSFT_MTEventProvider EventProviders[],
  [out] MSFT_MTEventChannel  WindowsEventChannels[]
);
```



## Parameters

<dl> <dt>

*EventProviders* \[out\]
</dt> <dd>

An [**MSFT\_MTEventProvider**](msft-mteventprovider.md) containing the list of those event providers that export at least one event channel.

</dd> <dt>

*WindowsEventChannels* \[out\]
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

[**MSFT\_MTEventProvider**](msft-mteventprovider.md)
</dt> </dl>

 

 





