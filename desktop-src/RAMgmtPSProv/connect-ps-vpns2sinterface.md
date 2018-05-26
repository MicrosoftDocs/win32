---
title: Connect method of the PS\_VpnS2SInterface class
description: Connects an S2S Interface that is currently not connected.
audience: developer
ms.assetid: 2ecd16e8-555b-4bc3-b1be-5db3db17b8a1
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Connect method
- Connect method, PS_VpnS2SInterface class
- PS_VpnS2SInterface class, Connect method
topic_type:
- apiref
api_name:
- PS_VpnS2SInterface.Connect
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Connect method of the PS\_VpnS2SInterface class

Connects an S2S Interface that is currently not connected.

## Syntax


```mof
uint32 Connect(
  [in]  string          Name,
  [in]  boolean         PassThru,
  [out] VpnS2SInterface cmdletOutput
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

A [**VpnS2SInterface**](ps-vpns2sinterface.md) that contains the cmdlet output.

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

[**PS\_VpnS2SInterface**](ps-vpns2sinterface.md)
</dt> </dl>

 

 





