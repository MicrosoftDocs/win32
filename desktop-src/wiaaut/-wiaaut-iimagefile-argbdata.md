---
title: ImageFile.ARGBData property
description: Retrieves the raw image bits as a Vector of Long values.
ms.assetid: 2eb9d583-b804-4255-b7ee-c2f58923ceb8
keywords:
- ARGBData property WIA Automation
- ARGBData property WIA Automation , ImageFile object
- ImageFile object WIA Automation , ARGBData property
topic_type:
- apiref
api_name:
- ImageFile.ARGBData
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ImageFile.ARGBData property

Retrieves the raw image bits as a [**Vector**](-wiaaut-vector.md) of **Long** values.

This property is read-only.

## Syntax


```VB
Property ARGBData( _
)
```



## Property value

[**Vector**](-wiaaut-vector.md) value of image bits.

## Remarks

The **ARGBData** property returns a [**Vector**](-wiaaut-vector.md) of **Long** values that contain raw ARGB bitmap data. Each **Long** value represents a pixel. The first value corresponds to the pixel at the upper left and proceeds to the right, then down. When organized this way, the count of **Long** values in the **Vector** will be the product of the image's width and height.

You can use the following function to calculate the index of a specific pixel by its (x,y) coordinate and return the value of the [**Vector**](-wiaaut-vector.md) at that location.


```
Function GetPixel(v, x, y, width, height) 
    If x > width Or x < 1 Or _ 
        y > height Or y < 1 Or _ 
        v.Count <> width * height Then 
        GetPixel = 0 
        Exit Function 
    End If 
    
    GetPixel = v(x + (y - 1) * width) 
End Function 
```



Each **Long** value contains 4 bytes, the first byte (or high-order byte) represents the Alpha value. An Alpha value of 255 is completely opaque. An Alpha value of 0 is completely transparent (for Image types that support tranparency). Each subsequent byte corresponds to the Red, Green, and Blue value respectively.

The following example includes functions that show how to acquire the individual Alpha, Red, Green, and Blue values from a **Long** ARGB value.


```
Function Get4ByteHex(val)
    Dim s As String
    s = Hex(val)
    Do While Len(s) < 8
        s = "0" & s
    Loop
    Get4ByteHex = Right(s, 8)
End Function

Function Get1ByteHex(val)
    Dim s As String
    s = Hex(val)
    Do While Len(s) < 2
        s = "0" & s
    Loop
    Get1ByteHex = Right(s, 2)
End Function

Function GetAlpha(val)
    Dim s As String
    s = Get4ByteHex(val)
    GetAlpha = CLng("&amp;h" & Left(s, 2))
End Function

Function GetRed(val)
    Dim s As String
    s = Get4ByteHex(val)
    GetRed = CLng("&amp;h" & Mid(s, 3, 2))
End Function

Function GetGreen(val)
    Dim s As String
    s = Get4ByteHex(val)
    GetGreen = CLng("&amp;h" & Mid(s, 5, 2))
End Function

Function GetBlue(val)
    Dim s As String
    s = Get4ByteHex(val)
    GetBlue = CLng("&amp;h" & Right(s, 2))
End Function

Function GetARGB(a, r, g, b)
    Dim s As String
    s = "&amp;h" & Get1ByteHex(a) & Get1ByteHex(r) & Get1ByteHex(g) & Get1ByteHex(b)
    GetARGB = CLng(s)
End Function
```



For additional example code, see [ARGB Filter: Create a Modified Version of an Image](-wiaaut-howto-use-filters.md#argb-filter-create-a-modified-version-of-an-image).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ImageFile**](-wiaaut-imagefile.md)
</dt> <dt>

[**FileData**](-wiaaut-iimagefile-filedata.md)
</dt> <dt>

[**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md)
</dt> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> </dl>

 

 





