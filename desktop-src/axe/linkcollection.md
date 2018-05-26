---
title: LinkCollection class
description: This interface provides containers for Link objects.
ms.assetid: 0DC83602-11C8-4B6C-9773-C09290934164
keywords:
- LinkCollection class Access Execution Engine
- LinkCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- LinkCollection
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LinkCollection class

This interface provides containers for [**Link**](link-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**LinkCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **LinkCollection** class has these methods.



| Method                                                    | Description                                                                                    |
|:----------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**~LinkCollection**](linkcollection--linkcollection.md) | Destructor method.<br/>                                                                  |
| [**AddItem**](linkcollection-additem.md)                 | Creates a [**Link**](link-struct.md) and adds it to the **LinkCollection**.<br/>        |
| [**Clear**](linkcollection-clear.md)                     | Deletes all [**Link**](link-struct.md) objects from the **LinkCollection**.<br/>        |
| [**DeleteItem**](linkcollection-deleteitem.md)           | Deletes a [**Link**](link-struct.md) from the **LinkCollection**.<br/>                  |
| [**GetCount**](linkcollection-getcount.md)               | Returns the count of [**Link**](link-struct.md) objects in the **LinkCollection**.<br/> |
| [**GetItem**](linkcollection-getitem.md)                 | Returns a [**Link**](link-struct.md) from the **LinkCollection**.<br/>                  |



 

## Remarks

A **LinkCollection** holds data from an **Issue/Solution/Links** or **Issue/AnalysisLinks** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





