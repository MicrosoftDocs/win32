---
title: Rebar
description: This section contains information about programming elements used with rebar controls.
ms.assetid: 'vs|controls|~\controls\rebar\reflist.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Rebar

This section contains information about programming elements used with rebar controls.

### Overviews



| Topic                                            | Contents                                                                               |
|--------------------------------------------------|----------------------------------------------------------------------------------------|
| [Rebar Controls](rebar-controls.md)             | *Rebar controls* act as containers for child windows.<br/>                       |
| [Using Rebar Controls](using-rebar-controls.md) | This section contains example code showing how to implement rebar controls.<br/> |



 

### Messages



| Topic                                               | Contents                                                                                                                                                                                             |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RB\_BEGINDRAG**](rb-begindrag.md)               | Puts the rebar control in drag-and-drop mode. This message does not cause a [RBN\_BEGINDRAG](rbn-begindrag.md) notification to be sent. <br/>                                                 |
| [**RB\_DELETEBAND**](rb-deleteband.md)             | Deletes a band from a rebar control. <br/>                                                                                                                                                     |
| [**RB\_DRAGMOVE**](rb-dragmove.md)                 | Updates the drag position in the rebar control after a previous [**RB\_BEGINDRAG**](rb-begindrag.md) message. <br/>                                                                           |
| [**RB\_ENDDRAG**](rb-enddrag.md)                   | Terminates the rebar control's drag-and-drop operation. This message does not cause an [RBN\_ENDDRAG](rbn-enddrag.md) notification to be sent. <br/>                                          |
| [**RB\_GETBANDBORDERS**](rb-getbandborders.md)     | Retrieves the borders of a band. The result of this message can be used to calculate the usable area in a band. <br/>                                                                          |
| [**RB\_GETBANDCOUNT**](rb-getbandcount.md)         | Retrieves the count of bands currently in the rebar control. <br/>                                                                                                                             |
| [**RB\_GETBANDINFO**](rb-getbandinfo.md)           | Retrieves information about a specified band in a rebar control. <br/>                                                                                                                         |
| [**RB\_GETBANDMARGINS**](rb-getbandmargins.md)     | Retrieves the margins of a band.<br/>                                                                                                                                                          |
| [**RB\_GETBARHEIGHT**](rb-getbarheight.md)         | Retrieves the height of the rebar control. <br/>                                                                                                                                               |
| [**RB\_GETBARINFO**](rb-getbarinfo.md)             | Retrieves information about the rebar control and the image list it uses. <br/>                                                                                                                |
| [**RB\_GETBKCOLOR**](rb-getbkcolor.md)             | Retrieves a rebar control's default background color. <br/>                                                                                                                                    |
| [**RB\_GETCOLORSCHEME**](rb-getcolorscheme.md)     | Retrieves the color scheme information from the rebar control. <br/>                                                                                                                           |
| [**RB\_GETDROPTARGET**](rb-getdroptarget.md)       | Retrieves a rebar control's [**IDropTarget**](/windows/desktop/api/oleidl/nn-oleidl-idroptarget) interface pointer. <br/>                                                                                                        |
| [**RB\_GETEXTENDEDSTYLE**](rb-getextendedstyle.md) | Gets the extended style. <br/>                                                                                                                                                                 |
| [**RB\_GETPALETTE**](rb-getpalette.md)             | Retrieves the rebar control's current palette. <br/>                                                                                                                                           |
| [**RB\_GETRECT**](rb-getrect.md)                   | Retrieves the bounding rectangle for a given band in a rebar control. <br/>                                                                                                                    |
| [**RB\_GETROWCOUNT**](rb-getrowcount.md)           | Retrieves the number of rows of bands in a rebar control. <br/>                                                                                                                                |
| [**RB\_GETROWHEIGHT**](rb-getrowheight.md)         | Retrieves the height of a specified row in a rebar control. <br/>                                                                                                                              |
| [**RB\_GETTEXTCOLOR**](rb-gettextcolor.md)         | Retrieves a rebar control's default text color. <br/>                                                                                                                                          |
| [**RB\_GETTOOLTIPS**](rb-gettooltips.md)           | Retrieves the handle to any tooltip control associated with the rebar control. <br/>                                                                                                           |
| [**RB\_GETUNICODEFORMAT**](rb-getunicodeformat.md) | Retrieves the Unicode character format flag for the control. <br/>                                                                                                                             |
| [**RB\_HITTEST**](rb-hittest.md)                   | Determines which portion of a rebar band is at a given point on the screen, if a rebar band exists at that point. <br/>                                                                        |
| [**RB\_IDTOINDEX**](rb-idtoindex.md)               | Converts a band identifier to a band index in a rebar control. <br/>                                                                                                                           |
| [**RB\_INSERTBAND**](rb-insertband.md)             | Inserts a new band in a rebar control. <br/>                                                                                                                                                   |
| [**RB\_MAXIMIZEBAND**](rb-maximizeband.md)         | Resizes a band in a rebar control to either its ideal or largest size. <br/>                                                                                                                   |
| [**RB\_MINIMIZEBAND**](rb-minimizeband.md)         | Resizes a band in a rebar control to its smallest size. <br/>                                                                                                                                  |
| [**RB\_MOVEBAND**](rb-moveband.md)                 | Moves a band from one index to another. <br/>                                                                                                                                                  |
| [**RB\_PUSHCHEVRON**](rb-pushchevron.md)           | Sent to a rebar control to programmatically push a chevron.<br/>                                                                                                                               |
| [**RB\_SETBANDINFO**](rb-setbandinfo.md)           | Sets characteristics of an existing band in a rebar control. <br/>                                                                                                                             |
| [**RB\_SETBANDWIDTH**](rb-setbandwidth.md)         | Sets the width for a docked band.<br/>                                                                                                                                                         |
| [**RB\_SETBARINFO**](rb-setbarinfo.md)             | Sets the characteristics of a rebar control. <br/>                                                                                                                                             |
| [**RB\_SETBKCOLOR**](rb-setbkcolor.md)             | Sets a rebar control's default background color. <br/>                                                                                                                                         |
| [**RB\_SETCOLORSCHEME**](rb-setcolorscheme.md)     | Sets the color scheme information for the rebar control. <br/>                                                                                                                                 |
| [**RB\_SETEXTENDEDSTYLE**](rb-setextendedstyle.md) | Sets the extended style. This message is not implemented.<br/>                                                                                                                                 |
| [**RB\_SETPALETTE**](rb-setpalette.md)             | Sets the rebar control's current palette. <br/>                                                                                                                                                |
| [**RB\_SETPARENT**](rb-setparent.md)               | Sets a rebar control's parent window. <br/>                                                                                                                                                    |
| [**RB\_SETTEXTCOLOR**](rb-settextcolor.md)         | Sets a rebar control's default text color. <br/>                                                                                                                                               |
| [**RB\_SETTOOLTIPS**](rb-settooltips.md)           | Associates a tooltip control with the rebar control. <br/>                                                                                                                                     |
| [**RB\_SETUNICODEFORMAT**](rb-setunicodeformat.md) | Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. <br/> |
| [**RB\_SETWINDOWTHEME**](rb-setwindowtheme.md)     | Sets the visual style of a rebar control.<br/>                                                                                                                                                 |
| [**RB\_SHOWBAND**](rb-showband.md)                 | Shows or hides a given band in a rebar control. <br/>                                                                                                                                          |
| [**RB\_SIZETORECT**](rb-sizetorect.md)             | Attempts to find the best layout of the bands for the given rectangle. <br/>                                                                                                                   |



 

### Notifications



| Topic                                                        | Contents                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NM\_CUSTOMDRAW (rebar)](nm-customdraw-rebar.md)            | Sent by the rebar control to notify its parent window about drawing operations. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                                               |
| [NM\_NCHITTEST (rebar)](nm-nchittest-rebar.md)              | Sent by a rebar control when the control receives a [**WM\_NCHITTEST**](/windows/desktop/inputdev/wm-nchittest) message. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                 |
| [NM\_RELEASEDCAPTURE (rebar)](nm-releasedcapture-rebar-.md) | Notifies a rebar control's parent window that the control is releasing mouse capture. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                        |
| [RBN\_AUTOBREAK](rbn-autobreak.md)                          | Notifies a [rebar's](rebar-controls.md) parent that a break will appear in the bar. The parent determines whether to make the break. <br/>                                                                                                                            |
| [RBN\_AUTOSIZE](rbn-autosize.md)                            | Sent by a rebar control created with the [**RBS\_AUTOSIZE**](rebar-control-styles.md) style when the rebar automatically resizes itself. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                  |
| [RBN\_BEGINDRAG](rbn-begindrag.md)                          | Sent by a rebar control when the user begins dragging a band. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                           |
| [RBN\_CHEVRONPUSHED](rbn-chevronpushed.md)                  | Sent by a rebar control when a chevron is pushed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                                                                        |
| [RBN\_CHILDSIZE](rbn-childsize.md)                          | Sent by a rebar control when a band's child window is resized. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                          |
| [RBN\_DELETEDBAND](rbn-deletedband.md)                      | Sent by a rebar control after a band has been deleted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                  |
| [RBN\_DELETINGBAND](rbn-deletingband.md)                    | Sent by a rebar control when a band is about to be deleted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                             |
| [RBN\_ENDDRAG](rbn-enddrag.md)                              | Sent by a rebar control when the user stops dragging a band. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                            |
| [RBN\_GETOBJECT](rbn-getobject.md)                          | Sent by a rebar control created with the [**RBS\_REGISTERDROP**](rebar-control-styles.md) style when an object is dragged over a band in the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |
| [RBN\_HEIGHTCHANGE](rbn-heightchange.md)                    | Sent by a rebar control when its height has changed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                    |
| [RBN\_LAYOUTCHANGED](rbn-layoutchanged.md)                  | Sent by a rebar control when the user changes the layout of the control's bands. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                        |
| [RBN\_MINMAX](rbn-minmax.md)                                | Sent by a rebar control prior to maximizing or minimizing a band. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                       |
| [RBN\_SPLITTERDRAG](rbn-splitterdrag.md)                    | Sent by a rebar control when the user drags a splitter. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                 |



 

### Structures



| Topic                                        | Contents                                                                                                                                      |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**NMRBAUTOSIZE**](/windows/win32/api/commctrl/ns-commctrl-nmrbautosize)         | Contains information used in handling the [RBN\_AUTOSIZE](rbn-autosize.md) notification codes. <br/>                                   |
| [**NMREBAR**](/windows/win32/api/commctrl/ns-commctrl-nmrebar)                   | Contains information used in handling various rebar notification codes. <br/>                                                           |
| [**NMREBARAUTOBREAK**](/windows/win32/api/commctrl/ns-commctrl-nmrebarautobreak) | Contains information used with the [RBN\_AUTOBREAK](rbn-autobreak.md) notification.<br/>                                               |
| [**NMREBARCHEVRON**](/windows/win32/api/commctrl/ns-commctrl-nmrebarchevron)     | Contains information used in handling the [RBN\_CHEVRONPUSHED](rbn-chevronpushed.md) notification code. <br/>                          |
| [**NMREBARCHILDSIZE**](/windows/win32/api/commctrl/ns-commctrl-nmrebarchildsize) | Contains information used in handling the [RBN\_CHILDSIZE](rbn-childsize.md) notification code. <br/>                                  |
| [**NMREBARSPLITTER**](/windows/win32/api/commctrl/ns-commctrl-nmrebarsplitter)   | Contains information used to handle an [RBN\_SPLITTERDRAG](rbn-splitterdrag.md) notification code.<br/>                                |
| [**RBHITTESTINFO**](/windows/win32/api/commctrl/ns-commctrl-rbhittestinfo)       | Contains information specific to a hit test operation. This structure is used with the [**RB\_HITTEST**](rb-hittest.md) message. <br/> |
| [**REBARBANDINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa)       | Contains information that defines a band in a rebar control. <br/>                                                                      |
| [**REBARINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarinfo)               | Contains information that describes rebar control characteristics. <br/>                                                                |



 

### Constants



| Topic                                            | Contents                                                                                              |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [Rebar Control Styles](rebar-control-styles.md) | Rebar controls support a variety of control styles in addition to standard window styles. <br/> |



 

 

