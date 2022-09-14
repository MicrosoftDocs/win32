---
title: Trackbar
description: This section contains information about the programming elements used with trackbar controls.
ms.assetid: 'vs|controls|~\controls\trackbar\reflist.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Trackbar

This section contains information about the programming elements used with trackbar controls.

### Overviews



| Topic                                                  | Contents                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Trackbar Controls](trackbar-controls.md)       | A trackbar is a window that contains a slider (sometimes called a thumb) in a channel, and optional tick marks. When the user moves the slider, using either the mouse or the direction keys, the trackbar sends notification messages to indicate the change.<br/> |
| [Using Trackbar Controls](using-trackbar-controls.md) | This section provides implementation details and examples for trackbar controls.<br/>                                                                                                                                                                               |



 

### Messages



| Topic                                                 | Contents                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TBM\_CLEARSEL**](tbm-clearsel.md)                 | Clears the current selection range in a trackbar. <br/>                                                                                                                                                                                                                                                      |
| [**TBM\_CLEARTICS**](tbm-cleartics.md)               | Removes the current tick marks from a trackbar. This message does not remove the first and last tick marks, which are created automatically by the trackbar. <br/>                                                                                                                                           |
| [**TBM\_GETBUDDY**](tbm-getbuddy.md)                 | Retrieves the handle to a trackbar control buddy window at a given location. The specified location is relative to the control's orientation (horizontal or vertical). <br/>                                                                                                                                 |
| [**TBM\_GETCHANNELRECT**](tbm-getchannelrect.md)     | Retrieves the size and position of the bounding rectangle for a trackbar's channel. (The channel is the area over which the slider moves. It contains the highlight when a range is selected.) <br/>                                                                                                         |
| [**TBM\_GETLINESIZE**](tbm-getlinesize.md)           | Retrieves the number of logical positions the trackbar's slider moves in response to keyboard input from the arrow keys, such as the or keys. The logical positions are the integer increments in the trackbar's range of minimum to maximum slider positions. <br/>                                         |
| [**TBM\_GETNUMTICS**](tbm-getnumtics.md)             | Retrieves the number of tick marks in a trackbar. <br/>                                                                                                                                                                                                                                                      |
| [**TBM\_GETPAGESIZE**](tbm-getpagesize.md)           | Retrieves the number of logical positions the trackbar's slider moves in response to keyboard input, such as the or keys, or mouse input, such as clicks in the trackbar's channel. The logical positions are the integer increments in the trackbar's range of minimum to maximum slider positions. <br/>   |
| [**TBM\_GETPOS**](tbm-getpos.md)                     | Retrieves the current logical position of the slider in a trackbar. The logical positions are the integer values in the trackbar's range of minimum to maximum slider positions. <br/>                                                                                                                       |
| [**TBM\_GETPTICS**](tbm-getptics.md)                 | Retrieves the address of an array that contains the positions of the tick marks for a trackbar. <br/>                                                                                                                                                                                                        |
| [**TBM\_GETRANGEMAX**](tbm-getrangemax.md)           | Retrieves the maximum position for the slider in a trackbar. <br/>                                                                                                                                                                                                                                           |
| [**TBM\_GETRANGEMIN**](tbm-getrangemin.md)           | Retrieves the minimum position for the slider in a trackbar. <br/>                                                                                                                                                                                                                                           |
| [**TBM\_GETSELEND**](tbm-getselend.md)               | Retrieves the ending position of the current selection range in a trackbar. <br/>                                                                                                                                                                                                                            |
| [**TBM\_GETSELSTART**](tbm-getselstart.md)           | Retrieves the starting position of the current selection range in a trackbar. <br/>                                                                                                                                                                                                                          |
| [**TBM\_GETTHUMBLENGTH**](tbm-getthumblength.md)     | Retrieves the length of the slider in a trackbar. <br/>                                                                                                                                                                                                                                                      |
| [**TBM\_GETTHUMBRECT**](tbm-getthumbrect.md)         | Retrieves the size and position of the bounding rectangle for the slider in a trackbar. <br/>                                                                                                                                                                                                                |
| [**TBM\_GETTIC**](tbm-gettic.md)                     | Retrieves the logical position of a tick mark in a trackbar. The logical position can be any of the integer values in the trackbar's range of minimum to maximum slider positions. <br/>                                                                                                                     |
| [**TBM\_GETTICPOS**](tbm-getticpos.md)               | Retrieves the current physical position of a tick mark in a trackbar.<br/>                                                                                                                                                                                                                                   |
| [**TBM\_GETTOOLTIPS**](tbm-gettooltips.md)           | Retrieves the handle to the tooltip control assigned to the trackbar, if any. <br/>                                                                                                                                                                                                                          |
| [**TBM\_GETUNICODEFORMAT**](tbm-getunicodeformat.md) | Retrieves the Unicode character format flag for the control. <br/>                                                                                                                                                                                                                                           |
| [**TBM\_SETBUDDY**](tbm-setbuddy.md)                 | Assigns a window as the buddy window for a trackbar control. Trackbar buddy windows are automatically displayed in a location relative to the control's orientation (horizontal or vertical). <br/>                                                                                                          |
| [**TBM\_SETLINESIZE**](tbm-setlinesize.md)           | Sets the number of logical positions the trackbar's slider moves in response to keyboard input from the arrow keys, such as the or keys. The logical positions are the integer increments in the trackbar's range of minimum to maximum slider positions. <br/>                                              |
| [**TBM\_SETPAGESIZE**](tbm-setpagesize.md)           | Sets the number of logical positions the trackbar's slider moves in response to keyboard input, such as the or keys, or mouse input, such as clicks in the trackbar's channel. The logical positions are the integer increments in the trackbar's range of minimum to maximum slider positions. <br/>        |
| [**TBM\_SETPOS**](tbm-setpos.md)                     | Sets the current logical position of the slider in a trackbar. <br/>                                                                                                                                                                                                                                         |
| [**TBM\_SETPOSNOTIFY**](tbm-setposnotify.md)         | Sets the current logical position of the slider in a trackbar. <br/>                                                                                                                                                                                                                                         |
| [**TBM\_SETRANGE**](tbm-setrange.md)                 | Sets the range of minimum and maximum logical positions for the slider in a trackbar. <br/>                                                                                                                                                                                                                  |
| [**TBM\_SETRANGEMAX**](tbm-setrangemax.md)           | Sets the maximum logical position for the slider in a trackbar. <br/>                                                                                                                                                                                                                                        |
| [**TBM\_SETRANGEMIN**](tbm-setrangemin.md)           | Sets the minimum logical position for the slider in a trackbar. <br/>                                                                                                                                                                                                                                        |
| [**TBM\_SETSEL**](tbm-setsel.md)                     | Sets the starting and ending positions for the available selection range in a trackbar. <br/>                                                                                                                                                                                                                |
| [**TBM\_SETSELEND**](tbm-setselend.md)               | Sets the ending logical position of the current selection range in a trackbar. This message is ignored if the trackbar does not have the [**TBS\_ENABLESELRANGE**](trackbar-control-styles.md) style. <br/>                                                                              |
| [**TBM\_SETSELSTART**](tbm-setselstart.md)           | Sets the starting logical position of the current selection range in a trackbar. This message is ignored if the trackbar does not have the [**TBS\_ENABLESELRANGE**](trackbar-control-styles.md) style. <br/>                                                                            |
| [**TBM\_SETTHUMBLENGTH**](tbm-setthumblength.md)     | Sets the length of the slider in a trackbar. This message is ignored if the trackbar does not have the [**TBS\_FIXEDLENGTH**](trackbar-control-styles.md) style. <br/>                                                                                                                      |
| [**TBM\_SETTIC**](tbm-settic.md)                     | Sets a tick mark in a trackbar at the specified logical position. <br/>                                                                                                                                                                                                                                      |
| [**TBM\_SETTICFREQ**](tbm-setticfreq.md)             | Sets the interval frequency for tick marks in a trackbar. For example, if the frequency is set to two, a tick mark is displayed for every other increment in the trackbar's range. The default setting for the frequency is one; that is, every increment in the range is associated with a tick mark. <br/> |
| [**TBM\_SETTIPSIDE**](tbm-settipside.md)             | Positions a tooltip control used by a trackbar control. Trackbar controls that use the [**TBS\_TOOLTIPS**](trackbar-control-styles.md) style display tooltips. <br/>                                                                                                                           |
| [**TBM\_SETTOOLTIPS**](tbm-settooltips.md)           | Assigns a tooltip control to a trackbar control. <br/>                                                                                                                                                                                                                                                       |
| [**TBM\_SETUNICODEFORMAT**](tbm-setunicodeformat.md) | Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. <br/>                                                                                                               |



 

### Notifications



| Topic                                                              | Contents                                                                                                                                                                                      |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NM\_CUSTOMDRAW (trackbar)](nm-customdraw-trackbar.md)            | Sent by a trackbar control to notify its parent windows about drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>        |
| [NM\_RELEASEDCAPTURE (trackbar)](nm-releasedcapture-trackbar-.md) | Notifies a trackbar control's parent window that the control is releasing mouse capture. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |
| [TRBN\_THUMBPOSCHANGING](trbn-thumbposchanging.md)                | Notifies that the thumb position on a trackbar is changing. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                               |



 

### Constants



| Topic                                                  | Contents                                                                                    |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Custom Draw Values](custom-draw-values.md)           | This section lists the values used to identify a trackbar control's parts. <br/>      |
| [Trackbar Control Styles](trackbar-control-styles.md) | This section contains information about the styles used with trackbar controls. <br/> |



 

 

 





