---
title: IWMPControls2 step method
description: The step method causes the current video media item to step to the next frame or the previous frame and freeze playback.
ms.assetid: c5cb720f-527f-45b6-ae8a-4da0e3e34618
keywords:
- step method Windows Media Player
- step method Windows Media Player , IWMPControls2 interface
- IWMPControls2 interface Windows Media Player , step method
topic_type:
- apiref
api_name:
- IWMPControls2.step
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls2::step method

The **step** method causes the current video media item to step to the next frame or the previous frame and freeze playback.

## Syntax


```CSharp
public void step(
  System.Int32 lStep
);
```


```VB

Public Sub step( _
  ByVal lStep As System.Int32 _
)
Implements IWMPControls2.step
```





## Parameters

<dl> <dt>

*lStep* \[in\]
</dt> <dd>

A **System.Int32** value indicating how many frames to step before freezing. Must be set to 1 or -1.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method currently supports only the parameters 1 or -1, so you can only step one frame at a time.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPControls2 Interface (VB and C#)**](iwmpcontrols2--vb-and-c.md)
</dt> <dt>

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> </dl>

 

 





