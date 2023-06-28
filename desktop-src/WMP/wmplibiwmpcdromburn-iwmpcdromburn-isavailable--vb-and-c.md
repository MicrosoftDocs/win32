---
title: IWMPCdromBurn isAvailable method
description: The isAvailable method provides information about the CD drive and media.
ms.assetid: 75e81f5f-5839-4012-b0b9-e77b3ca6f35c
keywords:
- isAvailable method Windows Media Player
- isAvailable method Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , isAvailable method
topic_type:
- apiref
api_name:
- IWMPCdromBurn.isAvailable
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromBurn::isAvailable method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isAvailable** method provides information about the CD drive and media.

## Syntax


```CSharp
public System.Boolean isAvailable(
  System.String bstrItem
);
```


```VB

Public Function isAvailable( _
  ByVal bstrItem As System.String _
) As System.Boolean
Implements IWMPCdromBurn.isAvailable
```





## Parameters

<dl> <dt>

*bstrItem* \[in\]
</dt> <dd>

A **System.String** that contains one of the following values.



| Value | Description                 |
|-------|-----------------------------|
| Burn  | The drive is a CD burner.   |
| Disc  | There is a CD in the drive. |
| Erase | The CD can be erased.       |
| Write | The CD can be written to.   |



 

</dd> </dl>

## Return value

A **System.Boolean** that indicates the result.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> </dl>

 

 





