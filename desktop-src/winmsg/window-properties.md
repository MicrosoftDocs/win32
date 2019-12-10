---
Description: This section discusses window properties. A window property is any data assigned to a window.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\windowing\windowproperties.htm'
title: Window Properties
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
| [**EnumProps**](https://msdn.microsoft.com/library/ms633562(v=VS.85).aspx)         | Enumerates all entries in the property list of a window by passing them, one by one, to the specified callback function. [**EnumProps**](https://msdn.microsoft.com/library/ms633562(v=VS.85).aspx) continues until the last entry is enumerated or the callback function returns**FALSE**.<br/>                                                                                                        |
| [**EnumPropsEx**](https://msdn.microsoft.com/library/ms633563(v=VS.85).aspx)     | Enumerates all entries in the property list of a window by passing them, one by one, to the specified callback function. [**EnumPropsEx**](https://msdn.microsoft.com/library/ms633563(v=VS.85).aspx) continues until the last entry is enumerated or the callback function returns **FALSE**. <br/>                                                                                                  |
| [**GetProp**](https://msdn.microsoft.com/library/ms633564(v=VS.85).aspx)             | Retrieves a data handle from the property list of the specified window. The character string identifies the handle to be retrieved. The string and handle must have been added to the property list by a previous call to the [**SetProp**](https://msdn.microsoft.com/library/ms633568(v=VS.85).aspx) function. <br/>                                                                                    |
| [*PropEnumProc*](https://msdn.microsoft.com/library/ms633565(v=VS.85).aspx)     | An application-defined callback function used with the [**EnumProps**](https://msdn.microsoft.com/library/ms633562(v=VS.85).aspx) function. The function receives property entries from a window's property list. The **PROPENUMPROC** type defines a pointer to this callback function. [*PropEnumProc*](https://msdn.microsoft.com/library/ms633565(v=VS.85).aspx) is a placeholder for the application-defined function name. <br/>           |
| [*PropEnumProcEx*](https://msdn.microsoft.com/library/ms633566(v=VS.85).aspx) | An application-defined callback function used with the [**EnumPropsEx**](https://msdn.microsoft.com/library/ms633563(v=VS.85).aspx) function. The function receives property entries from a window's property list. The **PROPENUMPROCEX** type defines a pointer to this callback function. [*PropEnumProcEx*](https://msdn.microsoft.com/library/ms633566(v=VS.85).aspx) is a placeholder for the application-defined function name. <br/> |
| [**RemoveProp**](https://msdn.microsoft.com/library/ms633567(v=VS.85).aspx)       | Removes an entry from the property list of the specified window. The specified character string identifies the entry to be removed.<br/>                                                                                                                                                                                                                    |
| [**SetProp**](https://msdn.microsoft.com/library/ms633568(v=VS.85).aspx)             | Adds a new entry or changes an existing entry in the property list of the specified window. The function adds a new entry to the list if the specified character string does not exist already in the list. The new entry contains the string and the handle. Otherwise, the function replaces the string's current handle with the specified handle. <br/> |



 

 

 




