---
title: Scroll Bar Control Styles (Winuser.h)
description: To create a scroll bar control using the CreateWindow or CreateWindowEx function specify the SCROLLBAR class, appropriate window style constants, and a combination of the following scroll bar control styles.
ms.assetid: 07195a95-eff8-4a47-926a-9d503fa7b299
topic_type:
- apiref
api_name:
- SBS_BOTTOMALIGN
- SBS_HORZ
- SBS_LEFTALIGN
- SBS_RIGHTALIGN
- SBS_SIZEBOX
- SBS_SIZEBOXBOTTOMRIGHTALIGN
- SBS_SIZEBOXTOPLEFTALIGN
- SBS_SIZEGRIP
- SBS_TOPALIGN
- SBS_VERT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Scroll Bar Control Styles

To create a scroll bar control using the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function specify the SCROLLBAR class, appropriate window style constants, and a combination of the following scroll bar control styles. Some of the styles create a scroll bar control that uses a default width or height. However, you must always specify the x- and y-coordinates and the other dimensions of the scroll bar when you call **CreateWindow** or **CreateWindowEx**.



| Constant                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SBS_BOTTOMALIGN"></span><span id="sbs_bottomalign"></span><dl> <dt>**SBS\_BOTTOMALIGN**</dt> </dl>                                     | Aligns the bottom edge of the scroll bar with the bottom edge of the rectangle defined by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function. The scroll bar has the default height for system scroll bars. Use this style with the SBS\_HORZ style.<br/>                      |
| <span id="SBS_HORZ"></span><span id="sbs_horz"></span><dl> <dt>**SBS\_HORZ**</dt> </dl>                                                          | Designates a horizontal scroll bar. If neither the SBS\_BOTTOMALIGN nor SBS\_TOPALIGN style is specified, the scroll bar has the height, width, and position specified by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa).<br/>                                                      |
| <span id="SBS_LEFTALIGN"></span><span id="sbs_leftalign"></span><dl> <dt>**SBS\_LEFTALIGN**</dt> </dl>                                           | Aligns the left edge of the scroll bar with the left edge of the rectangle defined by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). The scroll bar has the default width for system scroll bars. Use this style with the SBS\_VERT style.<br/>                                    |
| <span id="SBS_RIGHTALIGN"></span><span id="sbs_rightalign"></span><dl> <dt>**SBS\_RIGHTALIGN**</dt> </dl>                                        | Aligns the right edge of the scroll bar with the right edge of the rectangle defined by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). The scroll bar has the default width for system scroll bars. Use this style with the SBS\_VERT style.<br/>                                  |
| <span id="SBS_SIZEBOX"></span><span id="sbs_sizebox"></span><dl> <dt>**SBS\_SIZEBOX**</dt> </dl>                                                 | Designates a size box. If you specify neither the SBS\_SIZEBOXBOTTOMRIGHTALIGN nor the SBS\_SIZEBOXTOPLEFTALIGN style, the size box has the height, width, and position specified by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). <br/>                                          |
| <span id="SBS_SIZEBOXBOTTOMRIGHTALIGN"></span><span id="sbs_sizeboxbottomrightalign"></span><dl> <dt>**SBS\_SIZEBOXBOTTOMRIGHTALIGN**</dt> </dl> | Aligns the lower right corner of the size box with the lower right corner of the rectangle specified by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). The size box has the default size for system size boxes. Use this style with the SBS\_SIZEBOX or SBS\_SIZEGRIP styles.<br/> |
| <span id="SBS_SIZEBOXTOPLEFTALIGN"></span><span id="sbs_sizeboxtopleftalign"></span><dl> <dt>**SBS\_SIZEBOXTOPLEFTALIGN**</dt> </dl>             | Aligns the upper left corner of the size box with the upper left corner of the rectangle specified by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). The size box has the default size for system size boxes. Use this style with the SBS\_SIZEBOX or SBS\_SIZEGRIP styles.<br/>   |
| <span id="SBS_SIZEGRIP"></span><span id="sbs_sizegrip"></span><dl> <dt>**SBS\_SIZEGRIP**</dt> </dl>                                              | Same as SBS\_SIZEBOX, but with a raised edge. <br/>                                                                                                                                                                                                                                                                                  |
| <span id="SBS_TOPALIGN"></span><span id="sbs_topalign"></span><dl> <dt>**SBS\_TOPALIGN**</dt> </dl>                                              | Aligns the top edge of the scroll bar with the top edge of the rectangle defined by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). The scroll bar has the default height for system scroll bars. Use this style with the SBS\_HORZ style.<br/>                                     |
| <span id="SBS_VERT"></span><span id="sbs_vert"></span><dl> <dt>**SBS\_VERT**</dt> </dl>                                                          | Designates a vertical scroll bar. If you specify neither the SBS\_RIGHTALIGN nor the SBS\_LEFTALIGN style, the scroll bar has the height, width, and position specified by the *x*, *y*, *nWidth*, and *nHeight* parameters of [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa).<br/>                                                     |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winuser.h</dt> </dl> |



 

