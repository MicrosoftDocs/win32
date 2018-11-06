---
title: MONTHDAYSTATE
description: The MONTHDAYSTATE data type is a bitfield that holds the state of each day in a month.
ms.assetid: eb3dd6cb-738e-424b-945b-1485798a444c
ms.topic: article
ms.date: 05/31/2018
---

# MONTHDAYSTATE

The MONTHDAYSTATE data type is a bitfield that holds the state of each day in a month. The data type is defined in Commctrl.h as follows:


```
typedef DWORD MONTHDAYSTATE, *LPMONTHDAYSTATE;
```



Each bit (0 through 30) represents the state of a day in a month. If a bit is on, the corresponding day will be displayed in bold; otherwise it will be displayed with no emphasis.

This data type is used with the [**MCM\_SETDAYSTATE**](mcm-setdaystate.md) message and the corresponding macro, [**MonthCal\_SetDayState**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_setdaystate). When MONTHDAYSTATE values are used in reference to months shorter than 31 days, only the needed bits will be accessed.

This data type was first defined in [Version 4.70](common-control-versions.md) of Comctl32.dll.

 

 




