---
title: Device.WiaItem property
description: Retrieves the underlying IWiaItem interface for this Device object.
ms.assetid: '31ee5a4e-88d1-4af2-85d2-44453baf2402'
keywords: ["WiaItem property WIA Automation", "WiaItem property WIA Automation , Device object", "Device object WIA Automation , WiaItem property"]
topic_type:
- apiref
api_name:
- Device.WiaItem
api_location:
- Wiaaut.h
api_type:
- COM
---

# Device.WiaItem property

Retrieves the underlying [IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface for this [**Device**](-wiaaut-device.md) object.

This property is read-only.

## Syntax


```VB
Property WiaItem( _
)
```



## Property value

[IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface.

## Remarks

The **WiaItem (Device)** method is provided for the C++ developer who wants to use the Windows Image Acquisition (WIA) Automation Library from C++ and needs to get to the underlying [IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface. This property is not useful to the Microsoft Visual Basic developer.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**WiaItem (Item)**](-wiaaut-iitem-wiaitem.md)
</dt> </dl>

 

 





