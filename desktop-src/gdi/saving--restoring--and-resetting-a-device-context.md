---
Description: 'The following functions enable an application to save, restore, and reset a device context: SaveDC, RestoreDC, and ResetDC.'
ms.assetid: '22837876-2665-49c6-908e-80e107fc09f4'
title: 'Saving, Restoring, and Resetting a Device Context'
---

# Saving, Restoring, and Resetting a Device Context

The following functions enable an application to save, restore, and reset a device context: [**SaveDC**](savedc.md), [**RestoreDC**](restoredc.md), and [**ResetDC**](resetdc.md). The SaveDC function records on a special GDI stack the current DC's graphic objects and their attributes, and graphic modes. A drawing application can call this function before a user begins drawing and save the application's original state providing a clean slate for the user. To return to this original state, the application calls the RestoreDC function.

[**ResetDC**](resetdc.md) is provided to reset printer DC data. An application calls this function to reset the paper orientation, paper size, output scaling factor, number of copies to be printed, paper source (or bin), duplex mode, and so on. Typically, an application calls this function after a user has changed one of the printer options and the system has issued a [**WM\_DEVMODECHANGE**](wm-devmodechange.md) message.

 

 



