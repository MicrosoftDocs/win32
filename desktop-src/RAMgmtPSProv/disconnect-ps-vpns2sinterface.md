---
title: Disconnect method of the PS\_VpnS2SInterface class
description: This cmdlet is used to disconnect a S2S Interface that is currently connected.
audience: developer
ms.assetid: '327b87da-6b27-4edb-8d02-27fa1c9a319e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Disconnect method", "Disconnect method, PS_VpnS2SInterface class", "PS_VpnS2SInterface class, Disconnect method"]
topic_type:
- apiref
api_name:
- PS_VpnS2SInterface.Disconnect
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Disconnect method of the PS\_VpnS2SInterface class

This cmdlet is used to disconnect a S2S Interface that is currently connected.

## Syntax


```mof
uint32 Disconnect(
  [in]  string          Name,
  [in]  boolean         PassThru,
  [in]  boolean         Force,
  [out] VpnS2SInterface cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return an object in the *cmdletOutput* parameter; otherwise, **false**. The default value is **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** to not require a confirmation from the user; **false** to require a confirmation. The default value is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**VpnS2SInterface**](ps-vpns2sinterface.md) that contains the cmdlet output.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterface**](ps-vpns2sinterface.md)
</dt> </dl>

 

 





