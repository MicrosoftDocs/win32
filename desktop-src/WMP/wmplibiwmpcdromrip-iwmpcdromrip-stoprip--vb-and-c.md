---
title: IWMPCdromRip stopRip method
description: The stopRip method stops the CD ripping process.
ms.assetid: c2565d0d-1203-4bd3-9d43-58e971e6ec88
keywords:
- stopRip method Windows Media Player
- stopRip method Windows Media Player , IWMPCdromRip interface
- IWMPCdromRip interface Windows Media Player , stopRip method
topic_type:
- apiref
api_name:
- IWMPCdromRip.stopRip
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromRip::stopRip method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **stopRip** method stops the CD ripping process.

## Syntax


```CSharp
public void stopRip();
```


```VB

Public Sub stopRip()
Implements IWMPCdromRip.stopRip
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
</dt> <dt>

[**IWMPCdromRip.startRip**](wmplibiwmpcdromrip-iwmpcdromrip-startrip--vb-and-c.md)
</dt> <dt>

[**Ripping a CD**](ripping-a-cd.md)
</dt> </dl>

 

 





