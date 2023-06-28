---
title: IWMPCdromBurn refreshStatus method
description: The refreshStatus method updates the status information for the current burn playlist.
ms.assetid: 4dd90e76-92b5-4a00-b027-b54502e56804
keywords:
- refreshStatus method Windows Media Player
- refreshStatus method Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , refreshStatus method
topic_type:
- apiref
api_name:
- IWMPCdromBurn.refreshStatus
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromBurn::refreshStatus method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **refreshStatus** method updates the status information for the current burn playlist.

## Syntax


```CSharp
public void refreshStatus();
```


```VB

Public Sub refreshStatus()
Implements IWMPCdromBurn.refreshStatus
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

You should call this method after you create or change a burn playlist before reading status information or burning the CD. You can test whether a refresh is required by getting the value of **burnState** and checking for wmpbsRefreshStatusPending.

Refreshing the status is a synchronous operation. This means that a lengthy period of time might elapse before this method returns if the current burn playlist is large and contains many changes.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> <dt>

[**IWMPCdromBurn.burnState (VB and C#)**](wmplibiwmpcdromburn-iwmpcdromburn-burnstate--vb-and-c.md)
</dt> <dt>

[**WMPBurnState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnstate)
</dt> </dl>

 

 





