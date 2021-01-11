---
description: A structure that describes a single color value.
ms.assetid: 710f3ef1-bbc3-416d-9faf-aa4a716007c2
title: XPS_COLOR (Xpsobjectmodel.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XPS\_COLOR

A structure that describes a single color value.

``` syntax
typedef union switch (XPS_COLOR_TYPE colorType) value
{
    case XPS_COLOR_TYPE_SRGB:
        struct {
            byte alpha, red, green, blue;
        } sRGB;
    case XPS_COLOR_TYPE_SCRGB:
        struct {
            FLOAT alpha, red, green, blue;
        } scRGB;
    case XPS_COLOR_TYPE_CONTEXT:
        struct {
            byte channelCount;
            FLOAT channels[9];
        } context;
} XPS_COLOR;
```

## Remarks

The structure's format depends on the value of *colorType*.

<dl>

[**XPS\_COLOR\_TYPE\_SRGB**](/previous-versions/windows/desktop/dd372944(v=vs.85))  
[**XPS\_COLOR\_TYPE\_SCRGB**](/previous-versions/windows/desktop/dd372943(v=vs.85))  
[**XPS\_COLOR\_TYPE\_CONTEXT**](/windows/win32/api/xpsobjectmodel/ns-xpsobjectmodel-xps_color)  
</dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |
| Header<br/>                   | <dl> <dt>Xpsobjectmodel.h</dt> </dl>                                              |
| IDL<br/>                      | <dl> <dt>XpsObjectModel.idl</dt> </dl>                                            |



## See also

<dl> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

