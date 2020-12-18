---
title: IMsRdpClientNonScriptable7 DisableDpiCursorScalingForProcess method
description: Disables local scaling of the mouse cursor received from the server, ensuring that the cursor shape is rendered correctly without modification.
ms.tgt_platform: multiple
keywords:
- DisableDpiCursorScalingForProcess method Remote Desktop Services
- DisableDpiCursorScalingForProcess method Remote Desktop Services, IMsRdpClientNonScriptable7 interface
- IMsRdpClientNonScriptable7 interface Remote Desktop Services, DisableDpiCursorScalingForProcess method
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable7.DisableDpiCursorScalingForProcess
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClientNonScriptable7::DisableDpiCursorScalingForProcess method

Disables local scaling of the mouse cursor received from the server, ensuring that the cursor shape is rendered correctly without modification.

## Syntax

```C++
HRESULT DisableDpiCursorScalingForProcess();
```

## Parameters

This method has no parameters.

## Return value

Return **S\_OK** if successful.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClientNonScriptable7 is defined as 71B4A60A-FE21-46D8-A39B-8E32BA0C5ECC          |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable7**](imsrdpclientnonscriptable7.md)
</dt> </dl>
