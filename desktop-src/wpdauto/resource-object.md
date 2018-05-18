---
title: Resource object
description: The Resource object represents a resource on a WPDObject. In Windows 7, all resources are read-only.
ms.assetid: '219c7958-1683-4cd5-aaa4-65ebc0bb3a1b'
keywords: ["Resource object WPD Automation", "Resource object WPD Automation , described"]
topic_type:
- apiref
api_name:
- Resource
api_type:
- COM
---

# Resource object

The **Resource** object represents a resource on a **WPDObject**. In Windows 7, all resources are read-only.

## Members

The **Resource** object has these types of members:

-   [Events](#events)
-   [Properties](#properties)

### Events

The **Resource** object has these events.



| Event                                            | Description                                                         |
|:-------------------------------------------------|:--------------------------------------------------------------------|
| [**onTransferProgress**](ontransferprogress.md) | Indicates the progress of a resource-transfer operation.<br/> |



 

### Properties

The **Resource** object has these properties.



| Property                                             | Access type           | Description                                                                    |
|:-----------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------|
| [**Format**](resource-format.md)<br/>         | Read-only<br/>  | Gets the data format of the resource.<br/>                               |
| [**IsReadOnly**](resource-isreadonly.md)<br/> | Read-only<br/>  | Retrieves a value indicating whether the **Resource** is read-only.<br/> |
| [**Size**](resource-size.md)<br/>             | Read-only<br/>  | Gets the size of the **Resource**, in bytes.<br/>                        |
| [**Stream**](resource-stream.md)<br/>         | Read/write<br/> | Gets or sets an **IStream** containing resource data.<br/>               |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Reading and Writing Resource Data](reading-and-writing-resource-data.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





