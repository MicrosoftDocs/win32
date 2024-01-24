---
title: IMsRdpClientNonScriptable7 Clipboard property
description: Gets the Clipboard controller used to synchronize the local and remote clipboards if manual clipboard sync is enabled.
ms.tgt_platform: multiple
keywords:
- Clipboard property Remote Desktop Services
- Clipboard property Remote Desktop Services , IMsRdpClientNonScriptable7 interface
- IMsRdpClientNonScriptable7 interface Remote Desktop Services , Clipboard property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable7.Clipboard
- IMsRdpClientNonScriptable7.get_Clipboard
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClientNonScriptable7::Clipboard property

Gets the Clipboard controller used to synchronize the local and remote clipboards if manual clipboard sync is enabled.

This property is read-only.

## Syntax

```C++
HRESULT get_Clipboard(
  [out, retval] IMsRdpClipboard** ppClipboard
);
```

## Property value

An [IMsRdpClipboard](imsrdpclipboard.md) that represents the Clipboard controller used to synchronize the local and remote clipboards if manual clipboard sync is enabled (that is, the [ManualClipboardSyncEnabled](imsrdpextendedsettings-property.md) property value is set to **True**).

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