---
title: Hit Test Options
description: This section lists the option values that are used with the dwOptions parameter of the HitTestThemeBackground function. For a list of the values returned when you specify one of these options, see Hit Test Return Values.
ms.assetid: a0d5c6c8-bb50-46e1-98ae-2374842344c6
ms.topic: article
ms.date: 05/31/2018
---

# Hit Test Options

This section lists the option values that are used with the *dwOptions* parameter of the [**HitTestThemeBackground**](/windows/desktop/api/Uxtheme/nf-uxtheme-hittestthemebackground) function. For a list of the values returned when you specify one of these options, see [Hit Test Return Values](theme-hit-test-retval.md).

## Option Values

The following table lists the hit test options.



| Option                       | Value                                                                                                                    | Description                                                                                                                                                                         |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTTB\_BACKGROUNDSEG          | 0x00000000                                                                                                               | Theme background segment hit test option.                                                                                                                                           |
| HTTB\_FIXEDBORDER            | 0x00000002                                                                                                               | Fixed border hit test option.                                                                                                                                                       |
| HTTB\_CAPTION                | 0x00000004                                                                                                               | Caption hit test option.                                                                                                                                                            |
| HTTB\_RESIZINGBORDER         | (HTTB\_RESIZINGBORDER\_LEFT \| HTTB\_RESIZINGBORDER\_TOP \| HTTB\_RESIZINGBORDER\_RIGHT \| HTTB\_RESIZINGBORDER\_BOTTOM) | Resizing border hit test options.                                                                                                                                                   |
| HTTB\_RESIZINGBORDER\_LEFT   | 0x00000010                                                                                                               | Resizing left border hit test option.                                                                                                                                               |
| HTTB\_RESIZINGBORDER\_TOP    | 0x00000020                                                                                                               | Resizing top border hit test option.                                                                                                                                                |
| HTTB\_RESIZINGBORDER\_RIGHT  | 0x00000040                                                                                                               | Resizing right border hit test option.                                                                                                                                              |
| HTTB\_RESIZINGBORDER\_BOTTOM | 0x00000080                                                                                                               | Resizing bottom border hit test option.                                                                                                                                             |
| HTTB\_SIZINGTEMPLATE         | 0x00000100                                                                                                               | Resizing border is specified as a template, not just window edges. This option is mutually exclusive with HTTB\_SYSTEMSIZINGMARGINS; HTTB\_SIZINGTEMPLATE takes precedence.         |
| HTTB\_SYSTEMSIZINGMARGINS    | 0x00000200                                                                                                               | Uses the system resizing border width rather than visual style content margins. This option is mutually exclusive with HTTB\_SIZINGTEMPLATE; HTTB\_SIZINGTEMPLATE takes precedence. |



 

 

 




