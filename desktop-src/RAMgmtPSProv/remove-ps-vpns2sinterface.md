---
title: Remove method of the PS\_VpnS2SInterface class
description: Removes an S2S interface.
audience: developer
ms.assetid: 5e5628d3-0ae1-4cc8-b05b-1011f2af1f67
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_VpnS2SInterface class
- PS_VpnS2SInterface class, Remove method
topic_type:
- apiref
api_name:
- PS_VpnS2SInterface.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_VpnS2SInterface class

Removes an S2S interface.

## Syntax


```mof
uint32 Remove(
  [in]  string          Name[],
  [in]  boolean         PassThru,
  [in]  boolean         Force,
  [out] VpnS2SInterface cmdletOutput[]
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterface**](ps-vpns2sinterface.md)
</dt> </dl>

 

 





