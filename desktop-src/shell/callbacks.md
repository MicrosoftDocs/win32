---
Description: This section describes the Windows Shell callback functions.
title: Shell Callback Functions
ms.topic: article
ms.date: 05/31/2018
---

# Shell Callback Functions

This section describes the Windows Shell callback functions.

## In this section



| Topic                                                                     | Description                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BFFCALLBACK**](https://msdn.microsoft.com/en-us/library/Bb762598(v=VS.85).aspx)<br/>                      | Specifies an application-defined callback function used to send messages to, and process messages from, a **Browse** dialog box displayed in response to a call to [**SHBrowseForFolder**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shbrowseforfoldera).<br/> |
| [*FMExtensionProc*](fmextensionproc.md)<br/>                       | Specifies an application-defined callback function called by File Manager to communicate with a File Manager extension.<br/>                                                                                            |
| [*MRUCMPPROC*](mrucmpproc.md)<br/>                                 | Used to determine whether an item is present in a most recently used (MRU) list.<br/>                                                                                                                                   |
| [**PAPPSTATE\_CHANGE\_ROUTINE**](/windows/desktop/api/appnotify/nc-appnotify-pappstate_change_routine)<br/> | Specifies an app-defined callback function that notifies the app when the app is entering or leaving a suspended state.<br/>                                                                                            |
| [**SUBCLASSPROC**](https://msdn.microsoft.com/en-us/library/Bb776774(v=VS.85).aspx)<br/>                  | Defines the prototype for the callback function used by [**RemoveWindowSubclass**](/windows/desktop/api/Commctrl/nf-commctrl-removewindowsubclass) and [**SetWindowSubclass**](/windows/desktop/api/Commctrl/nf-commctrl-setwindowsubclass).<br/>                                                   |
| [**FM\_UNDELETE\_PROC**](undeletefile.md)<br/>                     | Specifies an application-defined callback function called by File Manager when the user chooses the **Undelete** command from the **File** menu.<br/>                                                                   |



 

 

 




