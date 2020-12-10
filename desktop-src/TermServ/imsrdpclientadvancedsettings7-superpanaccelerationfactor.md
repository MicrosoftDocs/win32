---
title: IMsRdpClientAdvancedSettings7 SuperPanAccelerationFactor property
description: Specifies or retrieves a value that indicates the SuperPan acceleration factor. The SuperPan acceleration factor determines how quickly the screen pans when in SuperPan mode.
ms.assetid: ce04f109-8a48-48ee-a553-728f12c09dde
ms.tgt_platform: multiple
keywords:
- SuperPanAccelerationFactor property Remote Desktop Services
- SuperPanAccelerationFactor property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , SuperPanAccelerationFactor property
- SuperPanAccelerationFactor property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , SuperPanAccelerationFactor property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings7.SuperPanAccelerationFactor
- IMsRdpClientAdvancedSettings7.get_SuperPanAccelerationFactor
- IMsRdpClientAdvancedSettings7.put_SuperPanAccelerationFactor
- IMsRdpClientAdvancedSettings8.SuperPanAccelerationFactor
- IMsRdpClientAdvancedSettings8.get_SuperPanAccelerationFactor
- IMsRdpClientAdvancedSettings8.put_SuperPanAccelerationFactor
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings7::SuperPanAccelerationFactor property

Specifies or retrieves a value that indicates the SuperPan acceleration factor. The SuperPan acceleration factor determines how quickly the screen pans when in SuperPan mode. The acceleration factor is the number of pixels that the screen view scrolls in a given direction for every pixel of mouse movement by the client.

This property is read/write.

## Syntax


```C++
HRESULT put_SuperPanAccelerationFactor(
  [in]          ULONG uAccelFactor
);

HRESULT get_SuperPanAccelerationFactor(
  [out, retval] ULONG *puAccelFactor
);
```



## Property value

The SuperPan acceleration factor to set. The SuperPan acceleration factor is the number of pixels that the screen view scrolls in a given direction for every pixel of mouse movement.

## Remarks

For more information about SuperPan, see [**EnableSuperPan**](imsrdpclientadvancedsettings7-enablesuperpan.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                             |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings7 is defined as 26036036-4010-4578-8091-0db9a1edf9c3<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> <dt>

[**EnableSuperPan**](imsrdpclientadvancedsettings7-enablesuperpan.md)
</dt> </dl>

 

 





