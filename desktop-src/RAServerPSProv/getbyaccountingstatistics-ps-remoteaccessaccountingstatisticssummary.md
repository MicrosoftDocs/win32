---
title: GetByAccountingStatistics method of the PS\_RemoteAccessAccountingStatisticsSummary class
description: Used to query Statistics Summary maintained by Inbox Accounting.
audience: developer
ms.assetid: 637eb2ef-89a1-41a3-b526-128f2fd76de8
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByAccountingStatistics method
- GetByAccountingStatistics method, PS_RemoteAccessAccountingStatisticsSummary class
- PS_RemoteAccessAccountingStatisticsSummary class, GetByAccountingStatistics method
topic_type:
- apiref
api_name:
- PS_RemoteAccessAccountingStatisticsSummary.GetByAccountingStatistics
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByAccountingStatistics method of the PS\_RemoteAccessAccountingStatisticsSummary class

Used to query Statistics Summary maintained by Inbox Accounting.

## Syntax


```mof
uint32 GetByAccountingStatistics(
  [in]  datetime                                     StartDateTime,
  [in]  datetime                                     EndDateTime,
  [out] RemoteAccessAccountingConnectionSummaryLocal cmdletOutput
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

A [**RemoteAccessAccountingConnectionSummaryLocal**](remoteaccessaccountingconnectionsummarylocal.md) containing the Remote Access connection summary from Accounting data.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessAccountingStatisticsSummary**](ps-remoteaccessaccountingstatisticssummary.md)
</dt> </dl>

 

 





