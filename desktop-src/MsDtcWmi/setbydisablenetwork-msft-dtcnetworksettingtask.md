---
title: SetByDisableNetwork method of the MSFT\_DtcNetworkSettingTask class
description: Modifies network access for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1558d035-421d-478d-ada5-05d82912f3f4
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByDisableNetwork method
- SetByDisableNetwork method, MSFT_DtcNetworkSettingTask class
- MSFT_DtcNetworkSettingTask class, SetByDisableNetwork method
topic_type:
- apiref
api_name:
- MSFT_DtcNetworkSettingTask.SetByDisableNetwork
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByDisableNetwork method of the MSFT\_DtcNetworkSettingTask class

Modifies network access for a DTC instance.

## Syntax


```mof
uint32 SetByDisableNetwork(
  [in] string  DtcName,
  [in] boolean DisableNetworkAccess
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance. If you do not specify this parameter, or if you specify a value of Local, this method modifies the local DTC instance.

</dd> <dt>

*DisableNetworkAccess* \[in\]
</dt> <dd>

**true** to disable network access for the DTC instance; otherwise, **false**.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcNetworkSettingTask**](msft-dtcnetworksettingtask.md)
</dt> </dl>

 

 





