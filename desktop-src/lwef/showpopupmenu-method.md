---
title: ShowPopupMenu Method
description: ShowPopupMenu Method
ms.assetid: 7f964d53-2594-41b1-9450-1ba7e9f85882
ms.topic: article
ms.date: 05/31/2018
---

# ShowPopupMenu Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Displays the character's pop-up menu at the specified location.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").ShowPopupMenu***x, y*



| Part | Description                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| *x*  | Required. An integer value that indicates the horizontal (*x*) screen coordinate to display the menu. These coordinates must be specified in pixels. |
| *y*  | Required. An integer value that indicates the vertical (*y*) screen coordinate to display the menu. These coordinates must be specified in pixels.   |



 

</dd> </dl>

## Remarks

Agent automatically displays the character's pop-up menu when the user right-clicks the character. If you set [**AutoPopupMenu**](autopopupmenu-property.md) to **False**, you can use this method to display the menu.

The menu remains displayed until the user selects a command or displays another menu. Only one pop-up menu can be displayed at a time; therefore, calls to this method will cancel (remove) the former menu.

This method should be called only when your client application is the active client of the character; otherwise it fails. To determine the success of this method you can call it as a function and it will return a Boolean value indicating whether the method succeeded.


```
   If Genie.ShowPopupMenu (10,10) = True Then
      ' The menu will be displayed

   Else 
      ' The menu will not be displayed

   End If
```



## See Also

[**AutoPopupMenu property**](autopopupmenu-property.md)


 

 




