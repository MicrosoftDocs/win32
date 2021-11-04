---
description: Image_V1_Load class - This class is the event type class for image load events. The following syntax is simplified from MOF code.
ms.assetid: 43bf0b2b-3ab4-4561-b48c-65fbace38a79
title: Image_V1_Load class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Image_V1_Load
- Image_V1_Load.ImageBase
- Image_V1_Load.ImageSize
- Image_V1_Load.ProcessId
- Image_V1_Load.FileName
api_type: 
- NA
api_location: 
---

# Image\_V1\_Load class

This class is the event type class for image load events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(10), EventTypeName("Load")]
class Image_V1_Load : Image_V1
{
  uint32 ImageBase;
  uint32 ImageSize;
  uint32 ProcessId;
  string FileName;
};
```

## Members

The **Image\_V1\_Load** class has these types of members:

-   [Properties](#properties)

### Properties

The **Image\_V1\_Load** class has these properties.

<dl> <dt>

FileName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

File name and extension of the DLL or executable image to load.

</dd> <dt>

ImageBase
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Base address of the application in which the image is loaded.

</dd> <dt>

ImageSize
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Size of the image being loaded.

When consuming this property, the data type for this property is actually size\_t. The Pointer qualifier is used to determine if the size\_t is 4-bytes or 8-bytes.

</dd> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Identifies the process into which the image is loaded.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Image\_V1**](image-v1.md)
</dt> </dl>

 

 




