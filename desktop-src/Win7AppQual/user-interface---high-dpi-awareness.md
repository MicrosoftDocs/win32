---
description: User Interface - High DPI Awareness
ms.assetid: 5b753340-366c-44b3-87e9-19c580f1c5d5
title: User Interface - High DPI Awareness
ms.topic: article
ms.date: 05/31/2018
---

# User Interface - High DPI Awareness

## Affected Platforms

 **Clients** - Windows XP \| Windows Vista \| Windows 7  

## Feature Impact

**Severity** - Medium  
**Frequency** - Medium  

## Description

The goal is to encourage end users to set their displays to native resolution and use DPI rather than screen resolution to change the size of displayed text and images. Windows 7 can auto-detect and configure a default DPI on clean installs on machines configured by their OEMs using DPI settings. There are tools you can use to help design applications that are high DPI aware in order to ensure the most readable results.

We have added two new High DPI features to Windows 7:

-   Per-user DPI setting (previously per machine)
-   Change DPI without rebooting (logoff/logon is still required)

## Manifestation of Impact

Applications that do not handle the high DPI case are likely to exhibit visual artifacts, including:

-   Clipping of UI or text by other UI elements
-   Inconsistent font sizes
-   Off-screen UIs
-   Blurring of text or UI
-   Broken drag-and-drop or other inputs
-   Rendering of full-screen DX applications partially off screen

## Solution

To make your applications DPI-aware:

1.  Do a high-level functional test pass, including install and uninstall at the following settings:

    | Setting                                              | What to look for                                                                                                                                                      |
    |------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | 1024x768 @ 120 DPI (125% scaling)                    | This is an effective resolution of ~800x600, so look for UI clipped off the screen or layout issues. Also look for pixilated bitmaps & icons.                         |
    | 1600x1200 @144 DPI (150% scaling)                    | Blurry UI. Verify that all mouse operations work, especially drag & drop operations. Also verify full-screen modes work properly.                                     |
    | 1600x1200 @ 144 DPI with DPI Virtualization Disabled | Often buttons and UI won't scale in relation to larger text & there will be significant text clipping. Look for layout issues in general & pixilated bitmats & icons. |

    

     

2.  Write down all the issues found, including location, screen resolution, and DPI settings, as well as how the application behaves in the other DPI/Resolution configurations for completeness
3.  Check each issue against the Common DPI Coding Issues
4.  Assess the cost of making the application fully DPI aware
5.  Make a list of the High DPI assets required (for example, buttons, icons)
6.  Work through and fix the list of DPI issues found in Step 1
7.  Integrate the new assets from Step 5
8.  Declare your application DPI Aware

## Compatibility, Performance, Reliability, and Usability Testing

Re-run the DPI Awareness assessment and verify the issues are fixed.

## Links to Other Resources

-   [High DPI Desktop Application Development on Windows](../hidpi/high-dpi-desktop-application-development-on-windows.md)
-   **Contact for technical questions:** <disup@microsoft.com>

 

 
