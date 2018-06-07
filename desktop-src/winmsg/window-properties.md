---
Description: This section discusses window properties. A window property is any data assigned to a window.
ms.assetid: 67ca264e-af8e-41bf-b9d1-d3db8cf1cdc3
title: Window Properties
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Window Properties

A window property is any data assigned to a window. A window property is usually a handle of the window-specific data, but it may be any value. Each window property is identified by a string name.

### In This Section



| Name                                                       | Description                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [About Window Properties](about-window-properties.md)     | Discusses window properties.<br/>                                                   |
| [Using Window Properties](using-window-properties.md)     | Explains how to perform the following tasks associated with window properties.<br/> |
| [Window Property Reference](window-property-reference.md) | Contains the API reference.<br/>                                                    |



 

### Window Property Functions



| Name                                   | Description                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumProps**](/windows/desktop/api/Winuser/nf-winuser-enumpropsa)         | Enumerates all entries in the property list of a window by passing them, one by one, to the specified callback function. [**EnumProps**](/windows/desktop/api/Winuser/nf-winuser-enumpropsa) continues until the last entry is enumerated or the callback function returns**FALSE**.<br/>                                                                                                        |
| [**EnumPropsEx**](/windows/desktop/api/Winuser/nf-winuser-enumpropsexa)     | Enumerates all entries in the property list of a window by passing them, one by one, to the specified callback function. [**EnumPropsEx**](/windows/desktop/api/Winuser/nf-winuser-enumpropsexa) continues until the last entry is enumerated or the callback function returns **FALSE**. <br/>                                                                                                  |
| [**GetProp**](/windows/desktop/api/Winuser/nf-winuser-getpropa)             | Retrieves a data handle from the property list of the specified window. The character string identifies the handle to be retrieved. The string and handle must have been added to the property list by a previous call to the [**SetProp**](/windows/desktop/api/Winuser/nf-winuser-setpropa) function. <br/>                                                                                    |
| [*PropEnumProc*](/windows/desktop/api/Winuser/nc-winuser-propenumproca)     | An application-defined callback function used with the [**EnumProps**](/windows/desktop/api/Winuser/nf-winuser-enumpropsa) function. The function receives property entries from a window's property list. The **PROPENUMPROC** type defines a pointer to this callback function. [*PropEnumProc*](/windows/desktop/api/Winuser/nc-winuser-propenumproca) is a placeholder for the application-defined function name. <br/>           |
| [*PropEnumProcEx*](/windows/desktop/api/Winuser/nc-winuser-propenumprocexa) | An application-defined callback function used with the [**EnumPropsEx**](/windows/desktop/api/Winuser/nf-winuser-enumpropsexa) function. The function receives property entries from a window's property list. The **PROPENUMPROCEX** type defines a pointer to this callback function. [*PropEnumProcEx*](/windows/desktop/api/Winuser/nc-winuser-propenumprocexa) is a placeholder for the application-defined function name. <br/> |
| [**RemoveProp**](/windows/desktop/api/Winuser/nf-winuser-removepropa)       | Removes an entry from the property list of the specified window. The specified character string identifies the entry to be removed.<br/>                                                                                                                                                                                                                    |
| [**SetProp**](/windows/desktop/api/Winuser/nf-winuser-setpropa)             | Adds a new entry or changes an existing entry in the property list of the specified window. The function adds a new entry to the list if the specified character string does not exist already in the list. The new entry contains the string and the handle. Otherwise, the function replaces the string's current handle with the specified handle. <br/> |



 

 

 




