---
title: Magnifier Styles
description: This topic describes the styles used with the magnifier control.
ms.assetid: 'B3C575AC-B8D3-40CF-AF09-BAC73E6C7B45'
topic_type:
- apiref
api_name:
- MS_CLIPAROUNDCURSOR
- MS_INVERTCOLORS
- MS_SHOWMAGNIFIEDCURSOR
api_location:
- Magnification.h
api_type:
- HeaderDef
---

# Magnifier Styles

This topic describes the styles used with the magnifier control. To create a magnifier control, use the [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function and specify the WC\_MAGNIFIER window class, along with a combination of the following magnifier styles.

<dl> <dt>

<span id="MS_CLIPAROUNDCURSOR"></span><span id="ms_cliparoundcursor"></span>**MS\_CLIPAROUNDCURSOR**
</dt> <dd> <dl> <dt>

0x0002L
</dt> <dt>



Clips the area of the magnifier window that surrounds the system cursor. This style enables the user to see screen content that is behind the magnifier window.


</dt> </dl> </dd> <dt>

<span id="MS_INVERTCOLORS"></span><span id="ms_invertcolors"></span>**MS\_INVERTCOLORS**
</dt> <dd> <dl> <dt>

0x0004L
</dt> <dt>



Displays the magnified screen content using inverted colors.


</dt> </dl> </dd> <dt>

<span id="MS_SHOWMAGNIFIEDCURSOR"></span><span id="ms_showmagnifiedcursor"></span>**MS\_SHOWMAGNIFIEDCURSOR**
</dt> <dd> <dl> <dt>

0x0001L
</dt> <dt>



Displays the magnified system cursor along with the magnified screen content.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Magnification.h</dt> </dl> |



## See also

<dl> <dt>

[Constants](entry-magapi-constants.md)
</dt> </dl>

 

 





