---
title: How to Process Date and Time Picker Notifications
description: This section demonstrates how to process date and time picker notifications.
ms.assetid: DBF624F0-89E0-435B-BE96-60B7A4CEDA61
ms.topic: article
ms.date: 05/31/2018
---

# How to Process Date and Time Picker Notifications

This section demonstrates how to process date and time picker notifications.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


A date and time picker (DTP) control sends notification messages to the parent window when events, usually triggered by input from the user, occur in the control. Your application must include code to determine the type of notification message and respond appropriately.

If you plan to use callback fields with the DTP controls in your application, you must be prepared to handle [DTN\_FORMATQUERY](dtn-formatquery.md), [DTN\_FORMAT](dtn-format.md), and [DTN\_WMKEYDOWN](dtn-wmkeydown.md) notification codes. For additional information about callback fields, see [Callback fields](date-and-time-picker-controls.md).

The following C++ code example identifies the notification message sent by a DTP control and calls the appropriate application-defined function. Refer to the following topics for code examples that illustrate how to process the notifications that appear in this example.

|   Topics                                                                                                     |
|--------------------------------------------------------------------------------------------------------|
| [How to Process the DTN\_DATETIMECHANGE Notification](process-the-dtn-datetimechange-notification.md) |
| [How to Process the DTN\_FORMATQUERY Notification](process-the-dtn-formatquery-notification.md)       |
| [How to Process the DTN\_FORMAT Notification](process-the-dtn-format-notfication.md)                  |
| [How to Process the DTN\_WMKEYDOWN Notification](process-the-dtn-wmkeydown-notification.md)           |



 



```C++
BOOL WINAPI DoNotify(HWND hwnd, WPARAM wParam, LPARAM lParam)
{
    LPNMHDR hdr = (LPNMHDR)lParam;

    switch(hdr->code){

        case DTN_DATETIMECHANGE:{
            LPNMDATETIMECHANGE lpChange = (LPNMDATETIMECHANGE)lParam;
            DoDateTimeChange(lpChange);
        }
        break;

        case DTN_FORMATQUERY:{
            LPNMDATETIMEFORMATQUERY lpDTFQuery = (LPNMDATETIMEFORMATQUERY)lParam;

            // Process DTN_FORMATQUERY to ensure that the control
            // displays callback information properly.
            DoFormatQuery(hdr->hwndFrom, lpDTFQuery);
        }
        break;

        case DTN_FORMAT:{
            LPNMDATETIMEFORMAT lpNMFormat = (LPNMDATETIMEFORMAT) lParam;

            // Process DTN_FORMAT to supply information about callback
            // fields (fields) in the DTP control.
            DoFormat(hdr->hwndFrom, lpNMFormat);
        }
        break;

        case DTN_WMKEYDOWN:{
            LPNMDATETIMEWMKEYDOWN lpDTKeystroke = 
                            (LPNMDATETIMEWMKEYDOWN)lParam;

            // Process DTN_WMKEYDOWN to respond to a user's keystroke in
            // a callback field.
            DoWMKeydown(hdr->hwndFrom, lpDTKeystroke);
        }
        break;
    }

    // All of the above notifications require the owner to return zero.
    return FALSE;
}
```



## Related topics

<dl> <dt>

[Date and Time Picker Notifications](bumper-date-and-time-picker-control-reference-notifications.md)
</dt> <dt>

[Date and Time Picker Control Reference](bumper-date-and-time-picker-date-and-time-picker-control-reference.md)
</dt> <dt>

[Using Date and Time Picker Controls](using-date-and-time-picker.md)
</dt> <dt>

[Date and Time Picker](date-and-time-picker-control-reference.md)
</dt> </dl>

 

 




