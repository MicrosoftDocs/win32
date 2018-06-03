---
title: SetByNetworkSettings method of the MSFT\_DtcNetworkSettingTask class
description: Modifies DTC network and security configuration settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 929813f5-1503-4be4-93f6-983f9041cbfe
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByNetworkSettings method
- SetByNetworkSettings method, MSFT_DtcNetworkSettingTask class
- MSFT_DtcNetworkSettingTask class, SetByNetworkSettings method
topic_type:
- apiref
api_name:
- MSFT_DtcNetworkSettingTask.SetByNetworkSettings
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByNetworkSettings method of the MSFT\_DtcNetworkSettingTask class

Modifies DTC network and security configuration settings.

## Syntax


```mof
uint32 SetByNetworkSettings(
  [in] string  DtcName,
  [in] boolean InboundTransactionsEnabled,
  [in] boolean OutboundTransactionsEnabled,
  [in] boolean RemoteClientAccessEnabled,
  [in] boolean RemoteAdministrationAccessEnabled,
  [in] boolean XATransactionsEnabled,
  [in] boolean LUTransactionsEnabled,
  [in] string  AuthenticationLevel
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance. If you do not specify this parameter, or if you specify a value of "Local", this method modifies the local DTC instance.

</dd> <dt>

*InboundTransactionsEnabled* \[in\]
</dt> <dd>

**true** if to enable inbound transactions to the DTC instance; otherwise, **false**.

</dd> <dt>

*OutboundTransactionsEnabled* \[in\]
</dt> <dd>

**true** if to enable outbound transactions from the DTC instance; otherwise, **false**.

</dd> <dt>

*RemoteClientAccessEnabled* \[in\]
</dt> <dd>

**true** if to enable remote client access for the DTC instance; otherwise, **false**.

</dd> <dt>

*RemoteAdministrationAccessEnabled* \[in\]
</dt> <dd>

**true** if to enable remote administration access for the DTC instance; otherwise, **false**.

</dd> <dt>

*XATransactionsEnabled* \[in\]
</dt> <dd>

**true** if to enable XA transactions in the DTC instance; otherwise, **false**.

</dd> <dt>

*LUTransactionsEnabled* \[in\]
</dt> <dd>

**true** if to enable LU transactions in the DTC instance; otherwise, **false**.

</dd> <dt>

*AuthenticationLevel* \[in\]
</dt> <dd>

The network authentication level of the DTC instance.

The possible values are:

NoAuth

Incoming

Mutual

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

 

 





