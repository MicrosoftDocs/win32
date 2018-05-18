---
title: GUID Management for Automation
description: Describes how to manage GUIDs for automation.
ms.assetid: '61237f96-21e1-4e5e-b488-660636d8127f'
---

# GUID Management for Automation

The problem with managing GUIDs is that they are pervasive, and their length prohibits simple comparisons.

The single most important technique in managing GUIDs is to keep a central list of all the GUIDs that are implemented. For example, use the DEFINE\_GUID macro or the Guidgen.exe tool with the **-n** option to generate the required number of GUIDs, and then enter the resulting strings in the first column of a spreadsheet. Each time a new GUID is used, enter a description of its purpose in the second column of the spreadsheet.

> [!Note]  
> The DEFINE\_GUIDE macro does not generate GUIDs. It defines a 128-bit number to a GUID with a human-readable name.

 

A central spreadsheet of GUIDs has several advantages:

-   Listing all the GUIDs in one location may prevent accidental reuse of a GUID. This often happens when an application is cloned to create another one.

-   The spreadsheet can be used to compare GUIDs. To check the accuracy of a GUID, you can copy it from the location where it is being used (for example, a .reg file), paste it into the spreadsheet, and then compare the two cells with the **=** operator.

-   A record of GUID usage can be helpful in case of future problems, and this single source of information will be available to find the GUID for an object.

 

 




