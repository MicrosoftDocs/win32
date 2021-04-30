---
title: IWMPClosedCaption captioningId property
description: The IWMPClosedCaption property gets or sets the name of the HTML element displaying the captioning.
ms.assetid: b09bb7c7-c3b6-4e0d-962f-24b06a04f6d1
keywords:
- captioningId property Windows Media Player
- captioningId property Windows Media Player , IWMPClosedCaption interface
- IWMPClosedCaption interface Windows Media Player , captioningId property
topic_type:
- apiref
api_name:
- IWMPClosedCaption.captioningId
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPClosedCaption::captioningId property

The **IWMPClosedCaption** property gets or sets the name of the HTML element displaying the captioning.

## Syntax


```CSharp
public System.String captioningId {get; set;}
```


```VB

Public Property captioningId As System.String
```





## Property value

The **System.String** that is the ID of the HTML element.

## Remarks

The element name specified can be any HTML element in the webpage as long as it supports the **innerHTML** attribute. If the webpage contains multiple frames, the element name can only refer to an element in the same frame as the Windows Media Player control.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**IWMPClosedCaption Interface (VB and C#)**](iwmpclosedcaption--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption2 Interface (VB and C#)**](iwmpclosedcaption2--vb-and-c.md)
</dt> </dl>

 

 





