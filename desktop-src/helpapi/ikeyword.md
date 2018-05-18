---
title: IKeyword interface
description: Help Keyword interface, contains methods to retrieve keyword information
ms.assetid: 'f82142fb-e1d8-4db2-8dbe-6037cc35bda4'
keywords: ["IKeyword interface HelpAPI", "IKeyword interface HelpAPI , described"]
topic_type:
- apiref
api_name:
- IKeyword
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeyword interface

Help Keyword interface, contains methods to retrieve keyword information

## Members

The **IKeyword** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IKeyword** also has these types of members:

-   [Properties](#properties)

### Properties

The **IKeyword** interface has these properties.



| Property                                                 | Access type          | Description                                                                                |
|:---------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------|
| [**DisplayValue**](ikeyword-displayvalue.md)<br/> | Read-only<br/> | Display value of the keyword<br/>                                                    |
| [**IsSubkey**](ikeyword-issubkey.md)<br/>         | Read-only<br/> | Returns a Boolean value indicating if the key is a subkey<br/>                       |
| [**Topics**](ikeyword-topics.md)<br/>             | Read-only<br/> | Returns an ITopicCollection containing all ITopics associated with this keyword<br/> |
| [**value**](ikeyword-value.md)<br/>               | Read-only<br/> | Actual value of the keyword<br/>                                                     |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





