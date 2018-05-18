---
title: Vector.BinaryData property
description: Sets or retrieves the Vector of bytes as an array of bytes.
ms.assetid: 'a817984e-e297-4840-b486-756a73d8ee03'
keywords: ["BinaryData property WIA Automation", "BinaryData property WIA Automation , Vector object", "Vector object WIA Automation , BinaryData property"]
topic_type:
- apiref
api_name:
- Vector.BinaryData
api_location:
- Wiaaut.h
api_type:
- COM
---

# Vector.BinaryData property

Sets or retrieves the [**Vector**](-wiaaut-vector.md) of bytes as an array of bytes.

This property is read/write.

## Syntax


```VB
Property BinaryData( _
)
```



## Property value

**Variant** value.

## Remarks

The **BinaryData** property provides interoperability between the Windows Image Acquisition (WIA) Automation Library and objects in other libraries that handle binary data as **Variant** arrays of unsigned one-byte characters. The most common examples are the **Read** and **Write** methods of the [Stream Object](http://msdn.microsoft.com/library/Aa173781(SQL.80).aspx) in Microsoft ActiveX Data Objects (ADO), and the [**BinaryRead**](c84b1f88-1a8a-4370-95de-e907f7fdd5e7) method of the [**Request Object**](54d9972a-b6cd-4672-b62a-8793ce8ad335), and the [**BinaryWrite**](04d5f44f-cc63-4465-b45f-634b95130b4a) method of the [**Response Object**](990e9575-5600-4469-bf17-1680191a462b) in an Active Server Pages (ASP) page.

For example code that uses an ASP page, see [Implement a Web Camera ASP Page](-wiaaut-shared-samples.md#implement-a-web-camera-asp-page) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> </dl>

 

 





