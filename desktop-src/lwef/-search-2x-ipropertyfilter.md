---
title: IPropertyFilter interface
description: Exposes properties used to filter the query.
ms.assetid: 3760c413-931c-44f2-adaf-eb17df4015c3
keywords:
- IPropertyFilter interface Legacy Windows Environment Features
- IPropertyFilter interface Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- IPropertyFilter
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPropertyFilter interface

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

Exposes properties used to filter the query.

## Members

The **IPropertyFilter** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPropertyFilter** also has these types of members:

-   [Properties](#properties)

### Properties

The **IPropertyFilter** interface has these properties.



| Property                                                                                      | Access type           | Description                                                   |
|:----------------------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------|
| [**IPropertyFilter::IndexColumn**](-search-2x-ipropertyfilter-indexcolumn.md)<br/>     | Read/write<br/> | Indexed column name of the property to filter by. <br/> |
| [**IPropertyFilter::LogicOperator**](-search-2x-ipropertyfilter-logicoperator.md)<br/> | Read/write<br/> | Logic Operator to use when applying filter. <br/>       |
| [**IPropertyFilter::NestingDepth**](-search-2x-ipropertyfilter-nestingdepth.md)<br/>   | Read/write<br/> | Filters depth within a nested set of parentheses. <br/> |
| [**IPropertyFilter::Text**](-search-2x-ipropertyfilter-text.md)<br/>                   | Read/write<br/> | Text of the filter. <br/>                               |
| [**IPropertyFilter::UID**](-search-2x-ipropertyfilter-uid.md)<br/>                     | Read/write<br/> | UID fo the property to filter by. <br/>                 |



 

## Remarks

These properties are used to filter the query.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>                                               |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





