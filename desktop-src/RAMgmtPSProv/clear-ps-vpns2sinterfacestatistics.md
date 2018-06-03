---
title: Clear method of the PS\_VpnS2SInterfaceStatistics class
description: Clears statistics of an S2S interface.
audience: developer
ms.assetid: 02de13ea-c66c-463f-a54e-e6ae3188a13b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Clear method
- Clear method, PS_VpnS2SInterfaceStatistics class
- PS_VpnS2SInterfaceStatistics class, Clear method
topic_type:
- apiref
api_name:
- PS_VpnS2SInterfaceStatistics.Clear
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Clear method of the PS\_VpnS2SInterfaceStatistics class

Clears statistics of an S2S interface.

## Syntax


```mof
uint32 Clear(
  [in]  string  Name,
  [in]  boolean PassThru,
  [out] boolean cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the connection.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return a value in *cmdletOutput*; otherwise, **false**. The default value is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The cmdlet output.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterfaceStatistics**](ps-vpns2sinterfacestatistics.md)
</dt> </dl>

 

 





