---
description: This class is the event type class for image events. The following syntax is simplified from MOF code.
ms.assetid: 70ec0542-16d3-4186-a346-7f3c44dedf67
title: Image_Load class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Image_Load
- Image_Load.ImageBase
- Image_Load.ImageSize
- Image_Load.ProcessId
- Image_Load.ImageCheckSum
- Image_Load.TimeDateStamp
- Image_Load.Reserved0
- Image_Load.DefaultBase
- Image_Load.Reserved1
- Image_Load.Reserved2
- Image_Load.Reserved3
- Image_Load.Reserved4
- Image_Load.FileName
api_type: 
- NA
api_location: 
---

# Image\_Load class

This class is the event type class for image events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(10, 2, 3, 4), EventTypeName("Load", "Unload", "DCStart", "DCEnd")]
class Image_Load : Image
{
  uint32 ImageBase;
  uint32 ImageSize;
  uint32 ProcessId;
  uint32 ImageCheckSum;
  uint32 TimeDateStamp;
  uint32 Reserved0;
  uint32 DefaultBase;
  uint32 Reserved1;
  uint32 Reserved2;
  uint32 Reserved3;
  uint32 Reserved4;
  string FileName;
};
```

## Members

The **Image\_Load** class has these types of members:

-   [Properties](#properties)

### Properties

The **Image\_Load** class has these properties.

<dl> <dt>

DefaultBase
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7), Pointer
</dt> </dl>

Default base address.

</dd> <dt>

FileName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(12), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

File name and extension of the DLL or executable image.

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

ImageCheckSum
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Image check sum.

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

</dd> <dt>

Reserved0
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6)
</dt> </dl>

Reserved.

</dd> <dt>

Reserved1
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8)
</dt> </dl>

Reserved.

</dd> <dt>

Reserved2
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(9)
</dt> </dl>

Reserved.

</dd> <dt>

Reserved3
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(10)
</dt> </dl>

Reserved.

</dd> <dt>

Reserved4
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(11)
</dt> </dl>

Reserved.

</dd> <dt>

TimeDateStamp
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

Time and date that the image was loaded or unloaded.

</dd> </dl>

## Remarks

The DCStart and DCEnd events enumerate all loaded images at the beginning and end of the trace, respectively.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Image**](image.md)
</dt> <dt>

[**Image\_V0**](image-v0.md)
</dt> <dt>

[**Image\_V1**](image-v1.md)
</dt> </dl>

 

 




