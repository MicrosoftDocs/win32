---
title: Using Tab Controls
description: This topic contains two examples that use tab controls.
ms.assetid: 29cc2f47-5667-4b03-8af8-51995a90a3dc
ms.topic: article
ms.date: 05/31/2018
---

# Using Tab Controls

This topic contains two examples that use tab controls. The first example demonstrates how to use a tab control to switch between multiple pages of text in an application's main window. The second example demonstrates how to use a tab control to switch between multiple pages of controls in a dialog box.

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="create-a-tab-control-in-the-main-window.md">How to Create a Tab Control in the Main Window</a><br /> | The example in this section demonstrates how to create a tab control and display it in the client area of the application's main window. The application displays a third window (a static control) in the display area of the tab control. The parent window positions and sizes the tab control and static control when it processes the <a href="/windows/desktop/winmsg/wm-size"><strong>WM_SIZE</strong></a> message. <br /> There are seven tabs in this example, one for each day of the week. When the user selects a tab, the application displays the name of the corresponding day in the static control. <br /> | 
| <a href="create-a-tabbed-dialog-box.md">How to Create a Tabbed Dialog Box</a><br /> | The example in this section demonstrates how to create a dialog box that uses tabs to provide multiple pages of controls. The main dialog box is a modal dialog box. Each page of controls is defined by a dialog box template that has the <a href="/windows/desktop/winmsg/window-styles"><strong>WS_CHILD</strong></a> style. When a tab is selected, a modeless dialog box is created for the incoming page and the dialog box for the outgoing page is destroyed. <br /><blockquote>[!Note]<br />In many cases, you can implement multiple-page dialog boxes more easily by using property sheets. For more information about property sheets, see <a href="property-sheets.md">About Property Sheets</a>.</blockquote><br /> The template for the main dialog box simply defines two button controls. When processing the <a href="/windows/desktop/dlgbox/wm-initdialog"><strong>WM_INITDIALOG</strong></a> message, the dialog box procedure creates a tab control and loads the dialog box template resources for each of the child dialog boxes. <br /> | 




 

