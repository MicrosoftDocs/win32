---
title: GetByActiveStatistics method of the PS\_RemoteAccessAccountingStatisticsSummary class
description: Used to query Active Connection stats.
audience: developer
ms.assetid: '64fd4b4b-599e-4bb6-9128-ee46da869eff'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByActiveStatistics method", "GetByActiveStatistics method, PS_RemoteAccessAccountingStatisticsSummary class", "PS_RemoteAccessAccountingStatisticsSummary class, GetByActiveStatistics method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessAccountingStatisticsSummary.GetByActiveStatistics
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# GetByActiveStatistics method of the PS\_RemoteAccessAccountingStatisticsSummary class

Used to query Active Connection stats

## Syntax


```mof
uint32 GetByActiveStatistics(
  [out] RemoteAccessActiveConnectionSummaryLocal cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains an array of [**RemoteAccessActiveConnectionSummaryLocal**](remoteaccessactiveconnectionsummarylocal.md) objects that contain the Remote Access active connection summary from Accounting data.

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

[**PS\_RemoteAccessAccountingStatisticsSummary**](ps-remoteaccessaccountingstatisticssummary.md)
</dt> </dl>

 

 





