---
title: IMsRdpClientNonScriptable5 GetRemoteMonitorsBoundingBox property
description: Specifies the bounding rectangle of the remote monitor.
ms.assetid: 4A8794F7-1DB4-4415-8538-6B2A365B22D3
ms.tgt_platform: multiple
keywords:
- GetRemoteMonitorsBoundingBox property Remote Desktop Services
- GetRemoteMonitorsBoundingBox property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , GetRemoteMonitorsBoundingBox property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable5.GetRemoteMonitorsBoundingBox
- IMsRdpClientNonScriptable5.get_GetRemoteMonitorsBoundingBox
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable5::GetRemoteMonitorsBoundingBox property

Specifies the bounding rectangle of the remote monitor.

This property is read-only.

## Syntax


```C++
HRESULT get_GetRemoteMonitorsBoundingBox(
  [out] LONG *pLeft,
  [out] LONG *pTop,
  [out] LONG *pRight,
  [out] LONG *pBottom
);
```



## Property value

Receives the left edge of the rectangle.

Receives the top edge of the rectangle.

Receives the right edge of the rectangle.

Receives the bottom edge of the rectangle.

## Remarks

All coordinates are in virtual screen coordinates, which are relative to the upper-left corner of the primary monitor. If this is not the primary monitor, some or all of these values may be negative.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                             |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable5 is defined as 4f6996d5-d7b1-412c-b0ff-063718566907<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> </dl>

 

 





