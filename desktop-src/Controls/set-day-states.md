---
title: How to Set Day States
description: This topic demonstrates how to set day state information. The month calendar control uses day state information to determine how it draws specific days within the control.
ms.assetid: EA92D858-BC80-4D08-9768-29A2BBDF900C
ms.topic: article
ms.date: 05/31/2018
---

# How to Set Day States

This topic demonstrates how to set day state information. The month calendar control uses day state information to determine how it draws specific days within the control.

Month calendar controls that use the [**MCS\_DAYSTATE**](month-calendar-control-styles.md) style support day states. Day state information is expressed as a 32-bit data type, [**MONTHDAYSTATE**](monthdaystate.md). Each bit in a **MONTHDAYSTATE** bitfield (0 through 30) specifies the state of a day in a month. If a bit is on, the corresponding day is displayed in bold.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


An application can explicitly set day state information by sending the [**MCM\_SETDAYSTATE**](mcm-setdaystate.md) message or by using the corresponding macro, [**MonthCal\_SetDayState**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_setdaystate). However, day state information is usually set in response to the [MCN\_GETDAYSTATE](mcn-getdaystate.md) notification code, which is sent whenever the control needs to be refreshed because, for example, a different month has scrolled into view.

The following example code shows how to process the [MCN\_GETDAYSTATE](mcn-getdaystate.md) notification code in a [**WM\_NOTIFY**](wm-notify.md) message handler. It processes MCN\_GETDAYSTATE by specifying that the first and fifteenth day of each visible month should be highlighted. The **cDayState** member of the [**NMDAYSTATE**](/windows/win32/api/commctrl/ns-commctrl-nmdaystate) structure specifies the number of [**MONTHDAYSTATE**](monthdaystate.md) values that are needed in the array, which is given an arbitrary maximum size. The code then loops to set the appropriate bits in each valid element of the array, using the application-defined **BOLDDAY** macro.



```C++
    #define BOLDDAY(ds, iDay)  \
        if (iDay > 0 && iDay < 32)(ds) |= (0x00000001 << (iDay - 1))

    case WM_NOTIFY:
            if (((LPNMHDR)lParam)->code == MCN_GETDAYSTATE)
            {
                MONTHDAYSTATE rgMonths[12] = { 0 };
                int cMonths = ((NMDAYSTATE*)lParam)->cDayState;
                for (int i = 0; i < cMonths; i++)
                {
                    BOLDDAY(rgMonths[i], 1);
                    BOLDDAY(rgMonths[i], 15);
                }
                ((NMDAYSTATE*)lParam)->prgDayState = rgMonths;
                return TRUE;
            }
            break;
```



## Related topics

<dl> <dt>

[Month Calendar Control Reference](bumper-month-calendar-month-calendar-control-reference.md)
</dt> <dt>

[About Month Calendar Controls](month-calendar-controls.md)
</dt> <dt>

[Using Month Calendar Controls](using-month-calendar-controls.md)
</dt> </dl>

 

 




