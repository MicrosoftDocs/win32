---
title: IP Address Control
description: This section contains information about the programming elements used with IP address controls.
ms.assetid: 'vs|controls|~\controls\ipaddress\reflist.htm'
ms.topic: article
ms.date: 05/31/2018
---

# IP Address Control

This section contains information about the programming elements used with IP address controls.

### Overviews



| Topic                                          | Contents                                                                                                                    |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [IP Address Controls](ip-address-controls.md) | An Internet Protocol (IP) address control allows the user to enter an IP address in an easily understood format.<br/> |



 

### Macros



| Topic                                         | Contents                                                                                                                              |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**FIRST\_IPADDRESS**](/windows/desktop/api/Commctrl/nf-commctrl-first_ipaddress)   | Extracts the field 0 value from a packed IP address retrieved with the [**IPM\_GETADDRESS**](ipm-getaddress.md) message. <br/> |
| [**FOURTH\_IPADDRESS**](/windows/desktop/api/Commctrl/nf-commctrl-fourth_ipaddress) | Extracts the field 3 value from a packed IP address retrieved with the [**IPM\_GETADDRESS**](ipm-getaddress.md) message. <br/> |
| [**MAKEIPADDRESS**](/windows/desktop/api/Commctrl/nf-commctrl-makeipaddress)        | Packs four byte-values into a single LPARAM suitable for use with the [**IPM\_SETADDRESS**](ipm-setaddress.md) message. <br/>  |
| [**MAKEIPRANGE**](/windows/desktop/api/Commctrl/nf-commctrl-makeiprange)            | Packs two byte-values into a single LPARAM suitable for use with the [**IPM\_SETRANGE**](ipm-setrange.md) message. <br/>       |
| [**SECOND\_IPADDRESS**](/windows/desktop/api/Commctrl/nf-commctrl-second_ipaddress) | Extracts the field 1 value from a packed IP address retrieved with the [**IPM\_GETADDRESS**](ipm-getaddress.md) message. <br/> |
| [**THIRD\_IPADDRESS**](/windows/desktop/api/Commctrl/nf-commctrl-third_ipaddress)   | Extracts the field 2 value from a packed IP address retrieved with the [**IPM\_GETADDRESS**](ipm-getaddress.md) message. <br/> |



 

### Messages



| Topic                                         | Contents                                                                                                                              |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**IPM\_CLEARADDRESS**](ipm-clearaddress.md) | Clears the contents of the IP address control. <br/>                                                                            |
| [**IPM\_GETADDRESS**](ipm-getaddress.md)     | Gets the address values for all four fields in the IP address control. <br/>                                                    |
| [**IPM\_ISBLANK**](ipm-isblank.md)           | Determines if all fields in the IP address control are blank. <br/>                                                             |
| [**IPM\_SETADDRESS**](ipm-setaddress.md)     | Sets the address values for all four fields in the IP address control. <br/>                                                    |
| [**IPM\_SETFOCUS**](ipm-setfocus.md)         | Sets the keyboard focus to the specified field in the IP address control. All of the text in that field will be selected. <br/> |
| [**IPM\_SETRANGE**](ipm-setrange.md)         | Sets the valid range for the specified field in the IP address control. <br/>                                                   |



 

### Notifications



| Topic                                     | Contents                                                                                                                                                                                   |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IPN\_FIELDCHANGED](ipn-fieldchanged.md) | Sent when the user changes a field in the control or moves from one field to another. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |



 

### Structures



| Topic                              | Contents                                                                                              |
|------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**NMIPADDRESS**](/windows/win32/api/commctrl/ns-commctrl-nmipaddress) | Contains information for the [IPN\_FIELDCHANGED](ipn-fieldchanged.md) notification code. <br/> |



 

 

 





