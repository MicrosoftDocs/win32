---
Description: Exposes methods that are used to initialize a most recently used (MRU) list for an autocompletion object.
title: IACLCustomMRU interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IACLCustomMRU interface

Exposes methods that are used to initialize a most recently used (MRU) list for an autocompletion object.

## Members

The **IACLCustomMRU** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IACLCustomMRU** also has these types of members:

-   [Methods](#methods)

### Methods

The **IACLCustomMRU** interface has these methods.



| Method                                             | Description                                                             |
|:---------------------------------------------------|:------------------------------------------------------------------------|
| [**AddMRUString**](iaclcustommru-addmrustring.md) | Adds an entry to the MRU list.<br/>                               |
| [**Initialize**](iaclcustommru-initialize.md)     | Loads a list of strings into the MRU list from the registry.<br/> |



 

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 




