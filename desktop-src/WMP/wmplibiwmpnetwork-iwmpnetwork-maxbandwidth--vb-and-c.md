---
title: IWMPNetwork maxBandwidth property
description: The maxBandwidth property gets or sets the maximum allowed bandwidth.
ms.assetid: ff7548d8-b80f-4cb4-bdd6-86d585fef329
keywords:
- maxBandwidth property Windows Media Player
- maxBandwidth property Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , maxBandwidth property
topic_type:
- apiref
api_name:
- IWMPNetwork.maxBandwidth
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPNetwork::maxBandwidth property

The **maxBandwidth** property gets or sets the maximum allowed bandwidth.

## Syntax


```CSharp
public System.Int32 maxBandwidth {get; set;}
```


```VB

Public Property maxBandwidth As System.Int32
```





## Property value

A **System.Int32** that is the maximum bandwidth.

## Remarks

This property does not have a default value. The value can be specified while Windows Media Player is playing, but the change will not take effect until the current media item is released by opening another one or by calling **AxWindowsMediaPlayer.close**. Windows Media Player attempts to achieve the highest bandwidth possible. No intentional reduction of bandwidth will occur unless this value is set.

This setting is useful for reducing the amount of bandwidth used, particularly in the case of a multiple bit rate (MBR) stream. An MBR stream contains multiple streams with different bit rates. In some cases, it may be desirable to use a stream with a lower bit rate than the client requires. In this case, specifying a lower bit rate with the **IWMPNetwork.maxBandwidth** property will select a lower bit-rate stream. For example, an MBR stream might include streams encoded at 20 kilobits per second (Kbps), 37 Kbps, and 200 Kbps. Using **IWMPNetwork.maxBandwidth** to specify a bit rate of 50,000 (50 Kbps) will select the 37 Kbps stream instead of the 200 Kbps stream.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer.close (VB and C#)**](axwmplib-axwindowsmediaplayer-close.md)
</dt> <dt>

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> </dl>

 

 





