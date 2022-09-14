---
description: Image_V0_Load class - This class is the event type class for image load events. The following syntax is simplified from MOF code.
ms.assetid: e2836153-8e4f-4c7f-9542-9402ed9e4356
title: Image_V0_Load class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Image_V0_Load
- Image_V0_Load.BaseAddress
- Image_V0_Load.ModuleSize
- Image_V0_Load.ImageFileName
api_type: 
- NA
api_location: 
---

# Image\_V0\_Load class

This class is the event type class for image load events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(10), EventTypeName("Load")]
class Image_V0_Load
{
  uint32 BaseAddress;
  uint32 ModuleSize;
  string ImageFileName;
};
```

## Members

The **Image\_V0\_Load** class has these types of members:

-   [Properties](#properties)

### Properties

The **Image\_V0\_Load** class has these properties.

<dl> <dt>

BaseAddress
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Base address of the application in which the image is loaded.

</dd> <dt>

ImageFileName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

File name and extension of the DLL or executable image to load.

</dd> <dt>

ModuleSize
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Size of the image.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**Image\_V0**](image-v0.md)
</dt> </dl>

 

 




