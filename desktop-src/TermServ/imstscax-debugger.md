---
title: IMsTscAx Debugger property
description: Gets a pointer to an instance of IMsTscDebug.
ms.assetid: 5d9a2048-5f5d-43ca-a8b8-400dac7d7472
ms.tgt_platform: multiple
keywords:
- Debugger property Remote Desktop Services
topic_type:
- apiref
api_name:
- IMsTscAx.Debugger
- IMsTscAx.get_Debugger
- IMsTscAx.put_Debugger
- IMsRdpClient.Debugger
- IMsRdpClient.get_Debugger
- IMsRdpClient.put_Debugger
- IMsRdpClient2.Debugger
- IMsRdpClient2.get_Debugger
- IMsRdpClient2.put_Debugger
- IMsRdpClient3.Debugger
- IMsRdpClient3.get_Debugger
- IMsRdpClient3.put_Debugger
- IMsRdpClient4.Debugger
- IMsRdpClient4.get_Debugger
- IMsRdpClient4.put_Debugger
- IMsRdpClient5.Debugger
- IMsRdpClient5.get_Debugger
- IMsRdpClient5.put_Debugger
- IMsRdpClient6.Debugger
- IMsRdpClient6.get_Debugger
- IMsRdpClient6.put_Debugger
- IMsRdpClient7.Debugger
- IMsRdpClient7.get_Debugger
- IMsRdpClient7.put_Debugger
- IMsRdpClient8.Debugger
- IMsRdpClient8.get_Debugger
- IMsRdpClient8.put_Debugger
- IMsRdpClient9.Debugger
- IMsRdpClient9.get_Debugger
- IMsRdpClient9.put_Debugger
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/13/2023
---

# IMsTscAx::Debugger property

Gets a pointer to an instance of **IMsTscDebug**. This interface is used by Microsoft to test the Remote Desktop ActiveX control. It is subject to change and removal in future versions of Windows. Do not use this interface.

This property is read-only.

## Syntax


```C++
HRESULT get_Debugger(
  [out] IMsTscDebug *pDebugger
);
```



## Property value

A pointer to an instance of **IMsTscDebug**.

## Error codes

Return **S\_OK** if successful.

## Remarks



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsTscAx is defined as 8C11EFAE-92C3-11D1-BC1E-00C04FA31489<br/>            |



## See also

<dl> <dt>

[**IMsRdpClient**](imsrdpclient-interface.md)
</dt> <dt>

[**IMsRdpClient2**](imsrdpclient2.md)
</dt> <dt>

[**IMsRdpClient3**](imsrdpclient3.md)
</dt> <dt>

[**IMsRdpClient4**](imsrdpclient4.md)
</dt> <dt>

[**IMsRdpClient5**](imsrdpclient5.md)
</dt> <dt>

[**IMsRdpClient6**](imsrdpclient6.md)
</dt> <dt>

[**IMsRdpClient7**](imsrdpclient7.md)
</dt> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**Connected**](imstscax-connected.md)
</dt> <dt>

[**IMsTscAx**](imstscax-interface.md)
</dt> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

