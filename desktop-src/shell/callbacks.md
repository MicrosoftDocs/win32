---
description: This section describes the Windows Shell callback functions.
title: Shell Callback Functions
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 617a73d9-e3e6-4def-a5b2-557faa7b03c0
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Shell Callback Functions

This section describes the Windows Shell callback functions.

## In this section



| Topic                                                                     | Description                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BFFCALLBACK**](/previous-versions/windows/desktop/legacy/bb762598(v=vs.85))<br/>                      | Specifies an application-defined callback function used to send messages to, and process messages from, a **Browse** dialog box displayed in response to a call to [**SHBrowseForFolder**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shbrowseforfoldera).<br/> |
| [*FMExtensionProc*](fmextensionproc.md)<br/>                       | Specifies an application-defined callback function called by File Manager to communicate with a File Manager extension.<br/>                                                                                            |
| [*MRUCMPPROC*](mrucmpproc.md)<br/>                                 | Used to determine whether an item is present in a most recently used (MRU) list.<br/>                                                                                                                                   |
| [**PAPPSTATE\_CHANGE\_ROUTINE**](/windows/desktop/api/appnotify/nc-appnotify-pappstate_change_routine)<br/> | Specifies an app-defined callback function that notifies the app when the app is entering or leaving a suspended state.<br/>                                                                                            |
| [**SUBCLASSPROC**](/windows/win32/api/commctrl/nc-commctrl-subclassproc)<br/>                  | Defines the prototype for the callback function used by [**RemoveWindowSubclass**](/windows/desktop/api/Commctrl/nf-commctrl-removewindowsubclass) and [**SetWindowSubclass**](/windows/desktop/api/Commctrl/nf-commctrl-setwindowsubclass).<br/>                                                   |
| [**FM\_UNDELETE\_PROC**](undeletefile.md)<br/>                     | Specifies an application-defined callback function called by File Manager when the user chooses the **Undelete** command from the **File** menu.<br/>                                                                   |



 

 

 
