---
title: Angle Blocks
description: Angle Blocks
ms.assetid: 5a12cda5-b4dd-44da-9ce5-6e08e2751a75
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Angle Blocks

This topic applies to Windows XP Service Pack 1 or later.

An angle block usually denotes a video segment that was shot from more than one camera angle. There can be up to nine angles in an angle block, numbered from 1 through 9. When the DVD Navigator filter first enters an angle block, it sends your application an **EC\_DVD\_ANGLES\_AVAILABLE** event notification with the number of angles in *lParam1*. A disc can be authored to automatically show a menu for available angles when it enters an angle block, but generally an application must determine the number of angles available and offer the user a way to select one.

The [**AnglesAvailable**](mstv-msvidwebdvd_anglesavailable_property) property lists the total number of angles available within the whole title, not the number of angles available at the time of the call. Thus, a call to **AnglesAvailable** might return a value of 9, when in fact there may only be 6 angles available in the current angle block, and 3 different angles available in the next angle block.

Angle numbers are not unique, but ordinal, so in a title of 9 angles, if block A has 6 angles and block B has 3 different angles, block A angles will be numbered 1–6, and block B angles will be numbered 1–3 (not 7–9).

Setting [**CurrentAngle**](mstv-msvidwebdvd_currentangle_property) to a number higher than the currently available highest angle will not cause an error, but merely set the currently viewed angle to the highest currently available angle. However, the angle number you set will be retained in the **CurrentAngle** property, and when (if) that angle does become available, the player will switch to that angle. Setting **CurrentAngle** to a number higher than the number of angles in the current title (returned by **AnglesAvailable**) will cause an error.

The following code shows how to populate the list box *lboAngles* with currently available angles, and how to enable or disable it as appropriate. It occurs within the [**DVDNotify**](mstv-msvidwebdvdevent_dvdnotify) event's **SelectCase** block. For more information on handling disc events, see [MSVidWebDVD Events](mstv-msvidwebdvd_events).


```C++
Case EC_DVD_ANGLE_CHANGE
   lboAngles.Clear
   For i = 1 To oVidWebDVD.AnglesAvailable
      lboAngles.AddItem "Angle " & i
   Next i
Case EC_DVD_ANGLES_AVAILABLE
   lboAngles.Enabled = lParam1
```



The following text shows how to handle a click on the *lboAngles* list box to change the viewing angle:


```C++
Private Sub lboAngles_Click()
   ' Angle list is 1-based!
   oVidWebDVD.CurrentAngle = lboAngles.ListIndex + 1
End Sub
```



## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




