---
title: IMsRdpClientSecuredSettings2 PCB property
description: Specifies the preconnection BLOB (PCB) setting to use prior to connecting for transmission to the server. | IMsRdpClientSecuredSettings2 PCB property
ms.assetid: e2ddd9fd-d868-4fc5-835d-0f4db5da71e3
ms.tgt_platform: multiple
keywords:
- PCB property Remote Desktop Services
- PCB property Remote Desktop Services , IMsRdpClientSecuredSettings2 interface
- IMsRdpClientSecuredSettings2 interface Remote Desktop Services , PCB property
topic_type:
- apiref
api_name:
- IMsRdpClientSecuredSettings2.PCB
- IMsRdpClientSecuredSettings2.get_PCB
- IMsRdpClientSecuredSettings2.put_PCB
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientSecuredSettings2::PCB property

Specifies the preconnection BLOB (PCB) setting to use prior to connecting for transmission to the server.

This property is read/write.

## Syntax


```C++
HRESULT put_PCB(
  [in]          BSTR bstrPCB
);

HRESULT get_PCB(
  [out, retval] BSTR *bstrPCB
);
```



## Property value

The PCB setting.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClientSecuredSettings2**](imsrdpclientsecuredsettings2.md)
</dt> </dl>

 

 





