---
title: IMsRdpClientTransportSettings GatewayUsageMethod property
description: Specifies when to use a Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 0644c413-9ff7-42c1-a38e-e1ce546972ff
ms.tgt_platform: multiple
keywords:
- GatewayUsageMethod property Remote Desktop Services
- GatewayUsageMethod property Remote Desktop Services , IMsRdpClientTransportSettings interface
- IMsRdpClientTransportSettings interface Remote Desktop Services , GatewayUsageMethod property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings.GatewayUsageMethod
- IMsRdpClientTransportSettings.get_GatewayUsageMethod
- IMsRdpClientTransportSettings.put_GatewayUsageMethod
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings::GatewayUsageMethod property

Specifies when to use a Remote Desktop Gateway (RD Gateway) server.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayUsageMethod(
  [in]  ULONG ulProxyMethod
);

HRESULT get_GatewayUsageMethod(
  [out] ULONG *pulProxyUsageMethod
);
```



## Property value

A **ULONG** variable that specifies the RD Gateway server usage method. This parameter can be one of the following values.

<dt>

<span id="TSC_PROXY_MODE_NONE_DIRECT"></span><span id="tsc_proxy_mode_none_direct"></span>

<span id="TSC_PROXY_MODE_NONE_DIRECT"></span><span id="tsc_proxy_mode_none_direct"></span>**TSC\_PROXY\_MODE\_NONE\_DIRECT** (0 (0x0))


</dt> <dd>

Do not use an RD Gateway server. In the Remote Desktop Connection (RDC) client UI, the **Bypass RD Gateway server for local addresses** check box is cleared.

</dd> <dt>

<span id="TSC_PROXY_MODE_DIRECT"></span><span id="tsc_proxy_mode_direct"></span>

<span id="TSC_PROXY_MODE_DIRECT"></span><span id="tsc_proxy_mode_direct"></span>**TSC\_PROXY\_MODE\_DIRECT** (1 (0x1))


</dt> <dd>

Always use an RD Gateway server. In the RDC client UI, the **Bypass RD Gateway server for local addresses** check box is cleared.

</dd> <dt>

<span id="TSC_PROXY_MODE_DETECT"></span><span id="tsc_proxy_mode_detect"></span>

<span id="TSC_PROXY_MODE_DETECT"></span><span id="tsc_proxy_mode_detect"></span>**TSC\_PROXY\_MODE\_DETECT** (2 (0x2))


</dt> <dd>

Use an RD Gateway server if a direct connection cannot be made to the RD Session Host server. In the RDC client UI, the **Bypass RD Gateway server for local addresses** check box is selected.

</dd> <dt>

<span id="TSC_PROXY_MODE_DEFAULT"></span><span id="tsc_proxy_mode_default"></span>

<span id="TSC_PROXY_MODE_DEFAULT"></span><span id="tsc_proxy_mode_default"></span>**TSC\_PROXY\_MODE\_DEFAULT** (3 (0x3))


</dt> <dd>

Use the default RD Gateway server settings.

</dd> <dt>

<span id="TSC_PROXY_MODE_NONE_DETECT"></span><span id="tsc_proxy_mode_none_detect"></span>

<span id="TSC_PROXY_MODE_NONE_DETECT"></span><span id="tsc_proxy_mode_none_detect"></span>**TSC\_PROXY\_MODE\_NONE\_DETECT** (4 (0x4))


</dt> <dd>

Do not use an RD Gateway server. In the RDC client UI, the **Bypass RD Gateway server for local addresses** check box is selected.

</dd> </dl>

## Error codes

Returns **S\_OK** if successful.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientTransportSettings is defined as 720298C0-A099-46f5-9F82-96921BAE4701<br/> |



## See also

<dl> <dt>

[**IMsRdpClientTransportSettings**](imsrdpclienttransportsettings.md)
</dt> </dl>

 

 





