---
title: Progress Bar
description: This section contains information about the programming elements used with progress bar controls.
ms.assetid: 'vs|controls|~\controls\progbar\reflist.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Progress Bar

This section contains information about the programming elements used with progress bar controls.

### Overviews



| Topic                                            | Contents                                                                                                           |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [Progress Bar Control](progress-bar-control.md) | A progress bar is a window that an application can use to indicate the progress of a lengthy operation.<br/> |



 

### Messages



| Topic                                       | Contents                                                                                                                                                                                                                                                              |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PBM\_DELTAPOS**](pbm-deltapos.md)       | Advances the current position of a progress bar by a specified increment and redraws the bar to reflect the new position. <br/>                                                                                                                                 |
| [**PBM\_GETBARCOLOR**](pbm-getbarcolor.md) | Gets the color of the progress bar.<br/>                                                                                                                                                                                                                        |
| [**PBM\_GETBKCOLOR**](pbm-getbkcolor.md)   | Gets the background color of the progress bar.<br/>                                                                                                                                                                                                             |
| [**PBM\_GETPOS**](pbm-getpos.md)           | Retrieves the current position of the progress bar. <br/>                                                                                                                                                                                                       |
| [**PBM\_GETRANGE**](pbm-getrange.md)       | Retrieves information about the current high and low limits of a given progress bar control. <br/>                                                                                                                                                              |
| [**PBM\_GETSTATE**](pbm-getstate.md)       | Gets the state of the progress bar.<br/>                                                                                                                                                                                                                        |
| [**PBM\_GETSTEP**](pbm-getstep.md)         | Retrieves the step increment for a progress bar. The step increment is the amount by which the progress bar increases its current position whenever it receives a [**PBM\_STEPIT**](pbm-stepit.md) message.<br/>                                               |
| [**PBM\_SETBARCOLOR**](pbm-setbarcolor.md) | Sets the color of the progress indicator bar in the progress bar control. <br/>                                                                                                                                                                                 |
| [**PBM\_SETBKCOLOR**](pbm-setbkcolor.md)   | Sets the background color in the progress bar. <br/>                                                                                                                                                                                                            |
| [**PBM\_SETMARQUEE**](pbm-setmarquee.md)   | Sets the progress bar to marquee mode. This causes the progress bar to move like a marquee.<br/>                                                                                                                                                                |
| [**PBM\_SETPOS**](pbm-setpos.md)           | Sets the current position for a progress bar and redraws the bar to reflect the new position. <br/>                                                                                                                                                             |
| [**PBM\_SETRANGE**](pbm-setrange.md)       | Sets the minimum and maximum values for a progress bar and redraws the bar to reflect the new range.<br/>                                                                                                                                                       |
| [**PBM\_SETRANGE32**](pbm-setrange32.md)   | Sets the range of a progress bar control to a 32-bit value. <br/>                                                                                                                                                                                               |
| [**PBM\_SETSTATE**](pbm-setstate.md)       | Sets the state of the progress bar.<br/>                                                                                                                                                                                                                        |
| [**PBM\_SETSTEP**](pbm-setstep.md)         | Specifies the step increment for a progress bar. The step increment is the amount by which the progress bar increases its current position whenever it receives a [**PBM\_STEPIT**](pbm-stepit.md) message. By default, the step increment is set to 10. <br/> |
| [**PBM\_STEPIT**](pbm-stepit.md)           | Advances the current position for a progress bar by the step increment and redraws the bar to reflect the new position. An application sets the step increment by sending the [**PBM\_SETSTEP**](pbm-setstep.md) message. <br/>                                |



 

### Structures



| Topic                      | Contents                                                                                                                                                                 |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PBRANGE**](/windows/desktop/api/Commctrl/ns-commctrl-pbrange) | Contains information about the high and low limits of a progress bar control. This structure is used with the [**PBM\_GETRANGE**](pbm-getrange.md) message. <br/> |



 

### Constants



| Topic                                                          | Contents                                                                            |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [Progress Bar Control Styles](progress-bar-control-styles.md) | The following control styles are supported by **Progress Bar** controls:<br/> |



 

 

 





