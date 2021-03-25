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
ms.date: 05/31/2018
---

# IWMPCdromBurn::refreshStatus method

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

 

 





