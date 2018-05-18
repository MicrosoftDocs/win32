---
title: Enable method of the PS\_BgpRouteFlapDampening class
description: Starts performing route dampening for the flapping BGP routes.
audience: developer
ms.assetid: '30cf64cd-6ddf-44c1-a79a-6c4cfd008948'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Enable method", "Enable method, PS_BgpRouteFlapDampening class", "PS_BgpRouteFlapDampening class, Enable method"]
topic_type:
- apiref
api_name:
- PS_BgpRouteFlapDampening.Enable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Enable method of the PS\_BgpRouteFlapDampening class

Starts performing route dampening for the flapping BGP routes.

## Syntax


```mof
uint32 Enable(
  [in]  string                      RoutingDomain,
  [in]  boolean                     PassThru,
  [in]  boolean                     Force,
  [out] BgpRouteFlapDampeningConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

User-defined unique alphanumeric identifier for the Routing domain or tenant.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to indicate that the method returns an output object. The default is **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** for no end-user confirmation prompt when calling this method. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

If *PassThru* is **true**, returns an embedded instance of the current object.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpRouteFlapDampening**](ps-bgprouteflapdampening.md)
</dt> </dl>

 

 





