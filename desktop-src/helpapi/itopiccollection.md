---
title: ITopicCollection interface
description: Collection of ITopics
ms.assetid: ac0d5c92-6bf8-4b9f-82e2-72eb37cb1840
keywords:
- ITopicCollection interface HelpAPI
- ITopicCollection interface HelpAPI , described
topic_type:
- apiref
api_name:
- ITopicCollection
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ITopicCollection interface

Collection of ITopics

## Members

The **ITopicCollection** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ITopicCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ITopicCollection** interface has these methods.



| Method                                                  | Description                                                                                                 |
|:--------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**GetEnumerator**](itopiccollection-getenumerator.md) | Returns an enumerator that iterates through a collection<br/>                                         |
| [**MoveNext**](itopiccollection-movenext.md)           | Advances the enumerator to the next element of the collection<br/>                                    |
| [**MoveTo**](itopiccollection-moveto.md)               | Sets current element in the collection the specified index<br/>                                       |
| [**Reset**](itopiccollection-reset.md)                 | Sets the enumerator to its initial position, which is before the first element in the collection<br/> |



 

### Properties

The **ITopicCollection** interface has these properties.



| Property                                               | Access type          | Description                                                  |
|:-------------------------------------------------------|:---------------------|:-------------------------------------------------------------|
| [**Count**](itopiccollection-count.md)<br/>     | Read-only<br/> | Returns the number of elements in the collection<br/>  |
| [**Current**](itopiccollection-current.md)<br/> | Read-only<br/> | Gets the current ITopic element in the collection<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





