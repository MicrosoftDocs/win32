---
title: Item.WiaItem property
description: Retrieves the underlying IWiaItem interface for this Item.
ms.assetid: '19385dbe-6f4c-4669-8f2c-556a251a21ab'
keywords: ["WiaItem property WIA Automation", "WiaItem property WIA Automation , Item object", "Item object WIA Automation , WiaItem property"]
topic_type:
- apiref
api_name:
- Item.WiaItem
api_location:
- Wiaaut.h
api_type:
- COM
---

# Item.WiaItem property

Retrieves the underlying [IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface for this [**Item**](-wiaaut-item.md).

This property is read-only.

## Syntax


```VB
Property WiaItem( _
)
```



## Property value

[IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface.

## Remarks

The **WiaItem (Item)** method is provided for the C++ developer who wants to use the Windows Image Acquisition (WIA) Automation Library from C++ and needs to get to the underlying [IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface. This property is not useful to the Microsoft Visual Basic developer.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Item**](-wiaaut-item.md)
</dt> <dt>

[**WiaItem (Device)**](-wiaaut-idevice-wiaitem.md)
</dt> </dl>

 

 





