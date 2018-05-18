---
title: GetByAccountingStatistics method of the PS\_RemoteAccessConnectionStatisticsLocal class
description: This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN connections for a specified time duration, based on accounting data.
audience: developer
ms.assetid: '2f979ade-8385-4582-95aa-cc0218136d9a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByAccountingStatistics method", "GetByAccountingStatistics method, PS_RemoteAccessConnectionStatisticsLocal class", "PS_RemoteAccessConnectionStatisticsLocal class, GetByAccountingStatistics method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatisticsLocal.GetByAccountingStatistics
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# GetByAccountingStatistics method of the PS\_RemoteAccessConnectionStatisticsLocal class

This cmdlet displays the following1. Statistics of current (real-time) active DirectAccess and VPN connections2. Statistics of DirectAccess and VPN connections for a specified time duration, based on accounting data

## Syntax


```mof
uint32 GetByAccountingStatistics(
  [in]  datetime                              StartDateTime,
  [in]  datetime                              EndDateTime,
  [out] RemoteAccessAccountingConnectionLocal cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*StartDateTime* \[in\]
</dt> <dd>

Start date from when to retrieve the summary.

</dd> <dt>

*EndDateTime* \[in\]
</dt> <dd>

End date till when to retrieve the summary.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of A [**RemoteAccessAccountingConnectionLocal**](remoteaccessaccountingconnectionlocal.md) containing the Remote Access connection objects from Accounting data.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessConnectionStatisticsLocal**](ps-remoteaccessconnectionstatisticslocal.md)
</dt> </dl>

 

 





