---
title: Hit Test Return Values
description: This section lists the hit test code values that are returned in the pwHitTestCode parameter of the HitTestThemeBackground function.
ms.assetid: 95b4fc1a-2f9b-4464-b672-552d36b60c42
ms.topic: article
ms.date: 05/31/2018
---

# Hit Test Return Values

This section lists the hit test code values that are returned in the *pwHitTestCode* parameter of the [**HitTestThemeBackground**](/windows/desktop/api/Uxtheme/nf-uxtheme-hittestthemebackground) function. The code values returned depend on the hit test options specified in the *dwOptions* parameter of the **HitTestThemeBackground** function. For a list of the options, see [Hit Test Options](theme-hit-test-options.md).

## Return Values

The following table lists the hit test options and the corresponding return codes.



| Option                       | Return codes  | Description                                                                                                        |
|------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------|
| HTTB\_BACKGROUNDSEG          | HTBOTTOM      | Hit test succeeded in the bottom border segment.                                                                   |
|                              | HTBOTTOMLEFT  | Hit test succeeded in the bottom and left border intersection.                                                     |
|                              | HTBOTTOMRIGHT | Hit test succeeded in the bottom and right border intersection.                                                    |
|                              | HTCLIENT      | Hit test succeeded in the middle background segment.                                                               |
|                              | HTLEFT        | Hit test succeeded in the left border segment.                                                                     |
|                              | HTNOWHERE     | Hit test succeeded outside the control or on a transparent area.                                                   |
|                              | HTRIGHT       | Hit test succeeded in the right border segment.                                                                    |
|                              | HTTOP         | Hit test succeeded in the top border segment.                                                                      |
|                              | HTTOPLEFT     | Hit test succeeded in top and left border intersection.                                                            |
|                              | HTTOPRIGHT    | Hit test succeeded in the top and right border intersection.                                                       |
| HTTB\_CAPTION                | HTCAPTION     | Hit test succeeded in the top, top left, or top right background segments.                                         |
|                              | HTNOWHERE     | Hit test succeeded outside the control or on a transparent area.                                                   |
| HTTB\_FIXEDBORDER            | HTBORDER      | Hit test succeeded in any background segment except the middle background segment.                                 |
|                              | HTCLIENT      | Hit test succeeded in the middle background segment.                                                               |
| HTTB\_RESIZINGBORDER         | HTBORDER      | Hit test failed in the middle background segment and resizing zones, but succeeded in a background border segment. |
| HTTB\_RESIZINGBORDER\_BOTTOM | HTBOTTOM      | Hit test succeeded in the bottom border segment.                                                                   |
| HTTB\_RESIZINGBORDER\_LEFT   | HTLEFT        | Hit test succeeded in the left border segment.                                                                     |
| HTTB\_RESIZINGBORDER\_RIGHT  | HTRIGHT       | Hit test succeeded in the right border segment.                                                                    |
| HTTB\_RESIZINGBORDER\_TOP    | HTTOP         | Hit test succeeded in the top border segment.                                                                      |



 

 

 




