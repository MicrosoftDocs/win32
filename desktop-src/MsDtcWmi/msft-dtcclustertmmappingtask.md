---
title: MSFT\_DtcClusterTMMappingTask class
description: Manages tasks for cluster DTC mappings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '56790e4a-28e9-4285-b01b-19a219456e32'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DtcClusterTMMappingTask class", "MSFT_DtcClusterTMMappingTask class, described"]
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
---

# MSFT\_DtcClusterTMMappingTask class

Manages tasks for cluster DTC mappings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcClusterTMMappingTask
{
};
```

## Members

The **MSFT\_DtcClusterTMMappingTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcClusterTMMappingTask** class has these methods.



| Method                                                                                                  | Description                                                    |
|:--------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|
| [**AddByComPlusSet**](addbycomplusset-msft-dtcclustertmmappingtask.md)                                 | Creates a DTC mapping for a COM+ application.<br/>       |
| [**AddByExeSet**](addbyexeset-msft-dtcclustertmmappingtask.md)                                         | Creates a cluster DTC mapping for an application.<br/>   |
| [**AddByServiceSet**](addbyserviceset-msft-dtcclustertmmappingtask.md)                                 | Creates a cluster DTC mapping for a service.<br/>        |
| [**Get**](get-msft-dtcclustertmmappingtask.md)                                                         | Retrieves cluster DTC mapping data.<br/>                 |
| [**RemoveByAllParameterSet**](removebyallparameterset-msft-dtcclustertmmappingtask.md)                 | Deletes all cluster DTC mappings.<br/>                   |
| [**RemoveByMappingNameParameterSet**](removebymappingnameparameterset-msft-dtcclustertmmappingtask.md) | Deletes a cluster DTC mapping object.<br/>               |
| [**SetByComPlusSet**](setbycomplusset-msft-dtcclustertmmappingtask.md)                                 | Updates cluster DTC mapping for a COM+ application.<br/> |
| [**SetByExeSet**](setbyexeset-msft-dtcclustertmmappingtask.md)                                         | Updates cluster DTC mapping for an application.<br/>     |
| [**SetByServiceSet**](setbyserviceset-msft-dtcclustertmmappingtask.md)                                 | Updates cluster DTC mapping for a service.<br/>          |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





