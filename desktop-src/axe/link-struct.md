---
title: Link class
description: This interface provides access to Link objects.
ms.assetid: CA8D4E49-6A35-42F1-ACF1-AA4C21665D44
keywords:
- Link class Access Execution Engine
- Link class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Link
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Link class

This interface provides access to **Link** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**Link** has these types of members:

-   [Methods](#methods)

### Methods

The **Link** class has these methods.



| Method                                        | Description                                            |
|:----------------------------------------------|:-------------------------------------------------------|
| [**~Link**](link--link.md)                   | Destructor method.<br/>                          |
| [**GetLinkTitle**](link-getlinktitle.md)     | Returns the link title from the **Link**.<br/>   |
| [**GetLinkToolTip**](link-getlinktooltip.md) | Returns the link tooltip from the **Link**.<br/> |
| [**GetLinkValue**](link-getlinkvalue.md)     | Returns the link value from the **Link**.<br/>   |
| [**SetLinkTitle**](link-setlinktitle.md)     | Sets the link title of the **Link**.<br/>        |
| [**SetLinkToolTip**](link-setlinktooltip.md) | Sets the link tooltip of the **Link**.<br/>      |
| [**SetLinkValue**](link-setlinkvalue.md)     | Sets the link value of the **Link**.<br/>        |



 

## Remarks

A **Link** holds data from an **Issue/Solution/Links/Link** or **Issue/AnalysisLinks/Link** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





