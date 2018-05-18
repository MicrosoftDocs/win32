---
title: IKeywordCollection interface
description: Collection of IKeyword interfaces
ms.assetid: '6e61654a-1983-4c8e-b182-76ea0dd52326'
keywords: ["IKeywordCollection interface HelpAPI", "IKeywordCollection interface HelpAPI , described"]
topic_type:
- apiref
api_name:
- IKeywordCollection
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeywordCollection interface

Collection of IKeyword interfaces

## Members

The **IKeywordCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IKeywordCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IKeywordCollection** interface has these methods.



| Method                                                    | Description                                                                                                 |
|:----------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**GetEnumerator**](ikeywordcollection-getenumerator.md) | Returns an enumerator that iterates through a collection<br/>                                         |
| [**Load**](ikeywordcollection-load.md)                   | Loads the keyword index from the provided filename<br/>                                               |
| [**MoveNext**](ikeywordcollection-movenext.md)           | Advances the enumerator to the next element of the collection<br/>                                    |
| [**MoveTo**](ikeywordcollection-moveto.md)               | Sets current element in the collection the specified index<br/>                                       |
| [**MoveToKeyword**](ikeywordcollection-movetokeyword.md) | Sets current element in the collection the first occurrence of the supplied string<br/>               |
| [**Reset**](ikeywordcollection-reset.md)                 | Sets the enumerator to its initial position, which is before the first element in the collection<br/> |
| [**Save**](ikeywordcollection-save.md)                   | Saves the keyword index to the provided filename<br/>                                                 |



 

### Properties

The **IKeywordCollection** interface has these properties.



| Property                                                   | Access type          | Description                                                    |
|:-----------------------------------------------------------|:---------------------|:---------------------------------------------------------------|
| [**Count**](ikeywordcollection-count.md)<br/>       | Read-only<br/> | Returns the number of elements in the collection<br/>    |
| [**Current**](ikeywordcollection-current.md)<br/>   | Read-only<br/> | Gets the current IKeyword element in the collection<br/> |
| [**pageSize**](ikeywordcollection-pagesize.md)<br/> | Read-only<br/> | Returns the page size of the collection<br/>             |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





