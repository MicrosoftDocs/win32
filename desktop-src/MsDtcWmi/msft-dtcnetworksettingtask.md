---
title: MSFT\_DtcNetworkSettingTask class
description: Retrieves and modifies DTC network and security configuration settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d51bec72-d948-43dc-b93b-b1dd131c612f
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcNetworkSettingTask class
- MSFT_DtcNetworkSettingTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcNetworkSettingTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DtcNetworkSettingTask class

Retrieves and modifies DTC network and security configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcNetworkSettingTask
{
};
```

## Members

The **MSFT\_DtcNetworkSettingTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcNetworkSettingTask** class has these methods.



| Method                                                                          | Description                                                           |
|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**Get**](get-msft-dtcnetworksettingtask.md)                                   | Retrieves DTC network and security configuration settings.<br/> |
| [**SetByDisableNetwork**](setbydisablenetwork-msft-dtcnetworksettingtask.md)   | Modifies network access for a DTC instance.<br/>                |
| [**SetByNetworkSettings**](setbynetworksettings-msft-dtcnetworksettingtask.md) | Modifies DTC network and security configuration settings.<br/>  |



 

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

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





