---
title: IHelpFilter interface
description: Collection of filter criteria name/value pairs
ms.assetid: 48a3a835-37e5-4af6-9cf3-9f66c3447a72
keywords:
- IHelpFilter interface HelpAPI
- IHelpFilter interface HelpAPI , described
topic_type:
- apiref
api_name:
- IHelpFilter
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IHelpFilter interface

Collection of filter criteria name/value pairs

## Members

The **IHelpFilter** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IHelpFilter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IHelpFilter** interface has these methods.



| Method                                         | Description                                                                                      |
|:-----------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**Add**](ihelpfilter-add.md)                 | method Add - Adds a filter key/value pair to the filter list<br/>                          |
| [**AddRange**](ihelpfilter-addrange.md)       | method AddRange - Adds a criteria key and matching range of values to the filter list<br/> |
| [**ContainsKey**](ihelpfilter-containskey.md) | method ContainsKey - Check to see if a filter key is in the filter list<br/>               |
| [**Count**](ihelpfilter-count.md)             | method Count - returns the number of filter elements in the collection<br/>                |
| [**ElementAt**](ihelpfilter-elementat.md)     | method ElementAt - returns filter value at a particular index in the collection<br/>       |
| [**Item**](ihelpfilter-item.md)               | method Item - returns the filter value of a provided filter key<br/>                       |
| [**Remove**](ihelpfilter-remove.md)           | method Remove - Remove a criteria key/value pair from the filter list<br/>                 |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





