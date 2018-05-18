---
title: Vector.SetFromString method
description: Stores the String value into the Vector of bytes including the terminating null character. Value might be truncated unless Resizable is True. The string is stored as an ANSI string unless Unicode is True, in which case it is stored as a Unicode string.
ms.assetid: '3ab6230a-e28f-4dc1-945d-7e53502b573b'
keywords: ["SetFromString method WIA Automation", "SetFromString method WIA Automation , Vector object", "Vector object WIA Automation , SetFromString method"]
topic_type:
- apiref
api_name:
- Vector.SetFromString
api_location:
- Wiaaut.h
api_type:
- COM
---

# Vector.SetFromString method

Stores the **String** value into the [**Vector**](-wiaaut-vector.md) of bytes including the terminating null character. Value might be truncated unless *Resizable* is True. The string is stored as an ANSI string unless *Unicode* is True, in which case it is stored as a Unicode string.

## Syntax


```VB
Vector.SetFromString( _
  ByVal Value As BSTR, _
  [ ByVal Resizable As VARIANT_BOOL ], _
  [ ByVal Unicode As VARIANT_BOOL ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*Value* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

*Resizable* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value.



| Value                                                                                                                                  | Meaning                        |
|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Not resizable.<br/>      |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Default. Resizable.<br/> |



 

</dd> <dt>

*Unicode* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value.



| Value                                                                                                                                  | Meaning                      |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Not Unicode.<br/>      |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Default. Unicode.<br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Because vectors of bytes can actually be strings, this method provides a way to set the contents of a [**Vector**](-wiaaut-vector.md) of bytes from a **String** in either Unicode or ANSI form. Note that since all strings are Unicode in Microsoft Visual Basic, you need to specify which way you would like the string stored.

One common point of confusion is how to create a [**Vector**](-wiaaut-vector.md) of bytes. Many Visual Basic developers might be tempted to try the following:


```
'Do not follow this example
Dim v 'As Vector

Set v = CreateObject("WIA.Vector")

v.Add "A"
```



However, the previous example does not work as expected. It actually creates a [**Vector**](-wiaaut-vector.md) of strings where the first element contains the string "A". Instead, to create a **Vector** containing bytes you can use the **SetFromString** method or the **CByte** function in Visual Basic as follows:


```
Dim v 'As Vector
Dim b 'As Byte

Set v = CreateObject("WIA.Vector")

b = Asc("A")
v.Add CByte(b)
```



For example code, see [Exif Filter: Write a New Title Tag to an Image](-wiaaut-howto-use-filters.md#exif-filter-write-a-new-title-tag-to-an-image).

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
</dt> <dt>

**Reference**
</dt> <dt>

[**Value (Property)**](-wiaaut-iproperty-value.md)
</dt> <dt>

[**Value (Rational)**](-wiaaut-irational-value.md)
</dt> <dt>

[**Add (Vector)**](-wiaaut-ivector-add.md)
</dt> </dl>

 

 





