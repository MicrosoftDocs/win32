---
title: IWMPMedia2 Error property
description: The Error property gets an IWMPErrorItem interface if the media item has an error condition.
ms.assetid: 57dc8aef-5f22-43da-87bc-fdc0c8ebe49b
keywords:
- Error property Windows Media Player
- Error property Windows Media Player , IWMPMedia2 interface
- IWMPMedia2 interface Windows Media Player , Error property
topic_type:
- apiref
api_name:
- IWMPMedia2.Error
- IWMPMedia2.get_Error
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMedia2::Error property

The **Error** property gets an **IWMPErrorItem** interface if the media item has an error condition.

This property is read-only.

## Syntax


```CSharp
public IWMPErrorItem Error {get;}
```


```VB

Public ReadOnly Property Error As IWMPErrorItem
```





## Property value

A **WMPLib.IWMPErrorItem** interface that provides access to information about the error condition.

## Remarks

If the media item cannot be played, this property gets an **IWMPErrorItem** interface that contains information about the problem encountered.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPErrorItem (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> <dt>

[**IWMPMedia2 Interface (VB and C#)**](iwmpmedia2--vb-and-c.md)
</dt> </dl>

 

 





