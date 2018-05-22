---
title: Property Sheet
description: This section contains information about programming elements used with property sheets.
ms.assetid: 'f4fa9815-eab8-4b0b-ae5f-0bce4374223a'
---

# Property Sheet

This section contains information about programming elements used with property sheets.

### Overviews



| Topic                                              | Contents                                                                                                                    |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [About Property Sheets](property-sheets.md)       | A *property sheet* is a window that allows the user to view and edit the properties of an item.<br/>                  |
| [Creating Wizards](wizards.md)                    | A wizard is a type of property sheet that provides a simple and powerful way to guide users through a procedure.<br/> |
| [Using Property Sheets](using-property-sheets.md) | This section gives implementation details and example code for working with property sheets.<br/>                     |



 

### Functions



| Topic                                                        | Contents                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*AddPropSheetPageProc*](addpropsheetpageproc.md)           | Specifies an application-defined callback function that a property sheet extension uses to add a page to a property sheet.<br/>                                                                                                                      |
| [**CreatePropertySheetPage**](createpropertysheetpage.md)   | Creates a new page for a property sheet.<br/>                                                                                                                                                                                                        |
| [**DestroyPropertySheetPage**](destroypropertysheetpage.md) | Destroys a property sheet page. An application must call this function for pages that have not been passed to the [**PropertySheet**](propertysheet.md) function.<br/>                                                                              |
| [**PropertySheet**](propertysheet.md)                       | Creates a property sheet and adds the pages defined in the specified property sheet header structure.<br/>                                                                                                                                           |
| [*PropSheetPageProc*](propsheetpageproc.md)                 | Specifies an application-defined callback function that a property sheet calls when a page is created and when it is about to be destroyed. An application can use this function to perform initialization and cleanup operations for the page.<br/> |
| [*PropSheetProc*](propsheetproc.md)                         | An application-defined callback function that the system calls when the property sheet is being created and initialized.<br/>                                                                                                                        |



 

### Messages



| Topic                                                               | Contents                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PSM\_ADDPAGE**](psm-addpage.md)                                 | Adds a new page to the end of an existing property sheet. You can send this message explicitly or by using the [**PropSheet\_AddPage**](propsheet-addpage.md) macro.<br/>                                                                                                |
| [**PSM\_APPLY**](psm-apply.md)                                     | Simulates the selection of the **Apply** button, indicating that one or more pages have changed and the changes need to be validated and recorded.<br/>                                                                                                                   |
| [**PSM\_CANCELTOCLOSE**](psm-canceltoclose.md)                     | Sent by an application when it has performed changes since the most recent [PSN\_APPLY](psn-apply.md) notification that cannot be canceled. You can send this message explicitly or by using the [**PropSheet\_CancelToClose**](propsheet-canceltoclose.md) macro.<br/> |
| [**PSM\_CHANGED**](psm-changed.md)                                 | Informs a property sheet that information in a page has changed. You can send this message explicitly or by using the [**PropSheet\_Changed**](propsheet-changed.md) macro.<br/>                                                                                         |
| [**PSM\_ENABLEWIZBUTTONS**](psm-enablewizbuttons.md)               | Enables or disables any of the standard buttons in an Aero wizard. You can send this message explicitly or use the [**PropSheet\_EnableWizButtons**](propsheet-enablewizbuttons.md) macro.<br/>                                                                          |
| [**PSM\_GETCURRENTPAGEHWND**](psm-getcurrentpagehwnd.md)           | Retrieves a handle to the window of the current page of a property sheet. You can send this message explicitly or by using the [**PropSheet\_GetCurrentPageHwnd**](propsheet-getcurrentpagehwnd.md) macro.<br/>                                                          |
| [**PSM\_GETRESULT**](psm-getresult.md)                             | Used by modeless property sheets to retrieve the information returned to modal property sheets by [**PropertySheet**](propertysheet.md). You can send this message explicitly or use the [**PropSheet\_GetResult**](propsheet-getresult.md) macro.<br/>                 |
| [**PSM\_GETTABCONTROL**](psm-gettabcontrol.md)                     | Retrieves the handle to the tab control of a property sheet. You can send this message explicitly or by using the [**PropSheet\_GetTabControl**](propsheet-gettabcontrol.md) macro.<br/>                                                                                 |
| [**PSM\_HWNDTOINDEX**](psm-hwndtoindex.md)                         | Takes the window handle of the property sheet page and returns its zero-based index. You can send this message explicitly or use the [**PropSheet\_HwndToIndex**](propsheet-hwndtoindex.md) macro.<br/>                                                                  |
| [**PSM\_IDTOINDEX**](psm-idtoindex.md)                             | Takes the resource ID of a property sheet page and returns its zero-based index. You can send this message explicitly or use the [**PropSheet\_IdToIndex**](propsheet-idtoindex.md) macro.<br/>                                                                          |
| [**PSM\_INDEXTOHWND**](psm-indextohwnd.md)                         | Takes the index of a property sheet page and returns its window handle. You can send this message explicitly or use the [**PropSheet\_IndexToHwnd**](propsheet-indextohwnd.md) macro.<br/>                                                                               |
| [**PSM\_INDEXTOID**](psm-indextoid.md)                             | Takes the index of a property sheet page and returns its resource ID. You can send this message explicitly or use the [**PropSheet\_IndexToId**](propsheet-indextoid.md) macro.<br/>                                                                                     |
| [**PSM\_INDEXTOPAGE**](psm-indextopage.md)                         | Takes the index of a property sheet page and returns its HPROPSHEETPAGE handle. You can send this message explicitly or use the [**PropSheet\_IndexToPage**](propsheet-indextopage.md) macro.<br/>                                                                       |
| [**PSM\_INSERTPAGE**](psm-insertpage.md)                           | Inserts a new page into an existing property sheet. The page can be inserted either at a specified index or after a specified page. You can send this message explicitly or by using the [**PropSheet\_InsertPage**](propsheet-insertpage.md) macro.<br/>                |
| [**PSM\_ISDIALOGMESSAGE**](psm-isdialogmessage.md)                 | Passes a message to a property sheet dialog box and indicates whether the dialog box processed the message. You can send this message explicitly or by using the [**PropSheet\_IsDialogMessage**](propsheet-isdialogmessage.md) macro.<br/>                              |
| [**PSM\_PAGETOINDEX**](psm-pagetoindex.md)                         | Takes the HPROPSHEETPAGE handle of the property sheet page and returns its zero-based index. You can send this message explicitly or use the [**PropSheet\_PageToIndex**](propsheet-pagetoindex.md) macro.<br/>                                                          |
| [**PSM\_PRESSBUTTON**](psm-pressbutton.md)                         | Simulates the selection of a property sheet button. You can send this message explicitly or by using the [**PropSheet\_PressButton**](propsheet-pressbutton.md) macro.<br/>                                                                                              |
| [**PSM\_QUERYSIBLINGS**](psm-querysiblings.md)                     | Sent to a property sheet, which then forwards the message to each of its pages. You can send this message explicitly or by using the [**PropSheet\_QuerySiblings**](propsheet-querysiblings.md) macro.<br/>                                                              |
| [**PSM\_REBOOTSYSTEM**](psm-rebootsystem.md)                       | Indicates the system needs to be restarted for the changes to take effect. You can send the [**PSM\_REBOOTSYSTEM**](psm-rebootsystem.md) message explicitly or by using the [**PropSheet\_RebootSystem**](propsheet-rebootsystem.md) macro.<br/>                        |
| [**PSM\_RECALCPAGESIZES**](psm-recalcpagesizes.md)                 | Recalculates the page size of a standard or wizard property sheet after pages have been added or removed. You can send this message explicitly or use the [**PropSheet\_RecalcPageSizes**](propsheet-recalcpagesizes.md) macro.<br/>                                     |
| [**PSM\_REMOVEPAGE**](psm-removepage.md)                           | Removes a page from a property sheet. You can send this message explicitly or by using the [**PropSheet\_RemovePage**](propsheet-removepage.md) macro.<br/>                                                                                                              |
| [**PSM\_RESTARTWINDOWS**](psm-restartwindows.md)                   | Indicates that Windows needs to be restarted for the changes to take effect.<br/>                                                                                                                                                                                         |
| [**PSM\_SETBUTTONTEXT**](psm-setbuttontext.md)                     | Sets the text on a button in an Aero wizard. You can send this message explicitly or by using the [**PropSheet\_SetButtonText**](propsheet-setbuttontext.md) macro.<br/>                                                                                                 |
| [**PSM\_SETCURSEL**](psm-setcursel.md)                             | Activates the specified page in a property sheet. You can send this message explicitly or by using the [**PropSheet\_SetCurSel**](propsheet-setcursel.md) macro.<br/>                                                                                                    |
| [**PSM\_SETCURSELID**](psm-setcurselid.md)                         | Activates the given page in a property sheet based on the resource identifier of the page. You can send this message explicitly or by using the [**PropSheet\_SetCurSelByID**](propsheet-setcurselbyid.md) macro.<br/>                                                   |
| [**PSM\_SETFINISHTEXT**](psm-setfinishtext.md)                     | Sets the text of the **Finish** button in a wizard, shows and enables the button, and hides the **Next** and **Back** buttons. You can send this message explicitly or by using the [**PropSheet\_SetFinishText**](propsheet-setfinishtext.md) macro.<br/>               |
| [**PSM\_SETHEADERBITMAP**](psm-setheaderbitmap.md)                 | This message is not implemented.<br/>                                                                                                                                                                                                                                     |
| [**PSM\_SETHEADERBITMAPRESOURCE**](psm-setheaderbitmapresource.md) | This message is not implemented.<br/>                                                                                                                                                                                                                                     |
| [**PSM\_SETHEADERSUBTITLE**](psm-setheadersubtitle.md)             | Sets the subtitle text for the header of a wizard's interior page. You can send this message explicitly or use the [**PropSheet\_SetHeaderSubTitle**](propsheet-setheadersubtitle.md) macro.<br/>                                                                        |
| [**PSM\_SETHEADERTITLE**](psm-setheadertitle.md)                   | Sets the title text for the header of a wizard's interior page. You can send this message explicitly or use the [**PropSheet\_SetHeaderTitle**](propsheet-setheadertitle.md) macro.<br/>                                                                                 |
| [**PSM\_SETNEXTTEXT**](psm-setnexttext.md)                         | Sets the text of the **Next** button in a wizard. You can send this message explicitly or by using the [**PropSheet\_SetNextText**](propsheet-setnexttext.md) macro.<br/>                                                                                                |
| [**PSM\_SETTITLE**](psm-settitle.md)                               | Sets the title of a property sheet. You can send this message explicitly or by using the [**PropSheet\_SetTitle**](propsheet-settitle.md) macro.<br/>                                                                                                                    |
| [**PSM\_SETWIZBUTTONS**](psm-setwizbuttons.md)                     | Enables or disables the **Back**, **Next**, and **Finish** buttons in a wizard. You can also use the [**PropSheet\_SetWizButtons**](propsheet-setwizbuttons.md) macro to post the message.<br/>                                                                          |
| [**PSM\_SHOWWIZBUTTONS**](psm-showwizbuttons.md)                   | Shows or hides buttons in a wizard. You can send this message explicitly or by using the [**PropSheet\_ShowWizButtons**](propsheet-showwizbuttons.md) macro.<br/>                                                                                                        |
| [**PSM\_UNCHANGED**](psm-unchanged.md)                             | Informs a property sheet that information in a page has reverted to the previously saved state. You can send this message explicitly or by using the [**PropSheet\_UnChanged**](propsheet-unchanged.md) macro.<br/>                                                      |



 

### Notifications



| Topic                                                     | Contents                                                                                                                                                                                                                                                |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PSN\_APPLY](psn-apply.md)                               | Sent to every page in the property sheet to indicate that the user has clicked the OK, Close, or Apply button and wants all changes to take effect. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>      |
| [PSN\_GETOBJECT](psn-getobject.md)                       | Sent by a property sheet to request a drop target object when the cursor passes over one of the tab control's buttons.<br/>                                                                                                                       |
| [PSN\_HELP](psn-help.md)                                 | Notifies a page that the user has clicked the Help button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                                          |
| [PSN\_KILLACTIVE](psn-killactive.md)                     | Notifies a page that it is about to lose activation either because another page is being activated or the user has clicked the **OK** button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>       |
| [PSN\_QUERYCANCEL](psn-querycancel.md)                   | Indicates that the user has canceled the property sheet. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                                            |
| [PSN\_QUERYINITIALFOCUS](psn-queryinitialfocus.md)       | Sent by a property sheet to provide a property sheet page an opportunity to specify which dialog box control should receive the initial focus. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>           |
| [PSN\_RESET](psn-reset.md)                               | Notifies a page that the property sheet is about to be destroyed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                                   |
| [PSN\_SETACTIVE](psn-setactive.md)                       | Notifies a page that it is about to be activated. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                                                   |
| [PSN\_TRANSLATEACCELERATOR](psn-translateaccelerator.md) | Notifies a property sheet that a keyboard message has been received. It provides the page an opportunity to do private keyboard accelerator translation. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/> |
| [PSN\_WIZBACK](psn-wizback.md)                           | Notifies a page that the user has clicked the **Back** button in a wizard. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                          |
| [PSN\_WIZFINISH](psn-wizfinish.md)                       | Notifies a page that the user has clicked the **Finish** button in a wizard. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                        |
| [PSN\_WIZNEXT](psn-wiznext.md)                           | Notifies a page that the user has clicked the **Next** button in a wizard. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                          |



 

### Structures



| Topic                                      | Contents                                                                   |
|--------------------------------------------|----------------------------------------------------------------------------|
| [**PROPSHEETHEADER**](propsheetheader.md) | Defines the frame and pages of a property sheet.<br/>                |
| [**PROPSHEETPAGE**](propsheetpage.md)     | Defines a page in a property sheet.<br/>                             |
| [**PSHNOTIFY**](pshnotify.md)             | Contains information for the property sheet notification codes.<br/> |



 

 

 





