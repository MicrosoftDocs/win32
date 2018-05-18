---
Description: Working With DVD Menus
ms.assetid: '8c5f8072-b74f-4e15-8991-73bcc4145fd2'
title: Working With DVD Menus
---

# Working With DVD Menus

The DVD Navigator might show a menu when the user activates a button, or when the Navigator enters the First Play domain. To show a menu programmatically, call the [**IDvdControl2::ShowMenu**](idvdcontrol2-showmenu.md) method.

There are several ways to select menu buttons programmatically:

-   To select a button by number, call [**IDvdControl2::SelectButton**](idvdcontrol2-selectbutton.md). Buttons are numbered 1 to 36. The [**IDvdInfo2::GetCurrentButton**](idvdinfo2-getcurrentbutton.md) method returns the number of available buttons.
-   To select a button relative to the position of the currently selected button, call [**IDvdControl2::SelectRelativeButton**](idvdcontrol2-selectrelativebutton.md). You can select a button in the up, down, left, or right direction.
-   To select a button by its coordinates within the window, call [**IDvdControl2::SelectAtPosition**](idvdcontrol2-selectatposition.md). This method takes (x,y) coordinates relative to the client area of the video window. (For windowless mode, this is the application window.) If there is no button at that location, the method returns VFW\_E\_DVD\_NO\_BUTTON.

In addition, there are several ways to activate a button:

-   To activate a button by number, call [**IDvdControl2::SelectAndActivateButton**](idvdcontrol2-selectandactivatebutton.md).
-   To activate a button by its coordinates, call [**IDvdControl2::ActivateAtPosition**](idvdcontrol2-activateatposition.md).
-   To activate the button that is currently selected, call [**IDvdControl2::ActivateButton**](idvdcontrol2-activatebutton.md). If no button is selected, the method returns VFW\_E\_DVD\_NO\_BUTTON.

Keep in mind that selecting a button merely highlights its borders. To cause the associated command to be fired, the button must be activated. Activating a button programmatically can be done in various ways, but the button must always be selected before it can be activated.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



