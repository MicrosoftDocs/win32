---
title: PS\_RemoteAccessAccountingStatisticsSummary class
description: Refers to the connection statistics summary based on accounting data.
audience: developer
ms.assetid: '637eb2ef-89a1-41a3-b526-128f2fd76de8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccessAccountingStatisticsSummary class", "PS_RemoteAccessAccountingStatisticsSummary class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessAccountingStatisticsSummary
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccessAccountingStatisticsSummary class

Refers to the connection statistics summary based on accounting data

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class PS_RemoteAccessAccountingStatisticsSummary
{
};
```

## Members

The **PS\_RemoteAccessAccountingStatisticsSummary** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessAccountingStatisticsSummary** class has these methods.



| Method                                                                                                    | Description                                                                |
|:----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**GetByAccountingStatistics**](getbyaccountingstatistics-ps-remoteaccessaccountingstatisticssummary.md) | Used to query Statistics Summary maintained by Inbox Accounting<br/> |
| [**GetByActiveStatistics**](getbyactivestatistics-ps-remoteaccessaccountingstatisticssummary.md)         | Used to query Active Connection stats<br/>                           |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





