---
title: IResultType interface (WdsSharedIDL.h)
description: Exposes property type information.
ms.assetid: 68abd470-2505-4836-a17f-f1c14157f8e7
keywords:
- IResultType interface Legacy Windows Environment Features
- IResultType interface Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- IResultType
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultType interface

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Exposes property type information.

## Members

The **IResultType** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IResultType** also has these types of members:

-   [Properties](#properties)

### Properties

The **IResultType** interface has these properties.



| Property                                                                 | Access type           | Description                                                                           |
|:-------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------|
| [**DisplayName**](-search-2x-iresulttype-displayname.md)<br/>     | Read-only<br/>  | Localized display name of the type:<br/>                                        |
| [**GetProperty**](-search-2x-iresulttype-getproperty.md)<br/>     | Read/write<br/> | This property contains specified property information. <br/>                    |
| [**PreceivedType**](-search-2x-iresulttype-preceivedtype.md)<br/> | Read-only<br/>  | This property contains the string used to identify the type in the index. <br/> |
| [**PropertyCount**](-search-2x-iresulttype-propertycount.md)<br/> | Read-only<br/>  | This property contains the number of properties exposed by the type. <br/>      |
| [**UID**](-search-2x-iresulttype-uid.md)<br/>                     | Read-only<br/>  | This property contains the unique identifier for the type. <br/>                |



 

## Remarks

These methods expose the types of information returned.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>                                               |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

