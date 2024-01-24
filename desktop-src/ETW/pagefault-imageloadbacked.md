---
description: This class is the event type class for image load in page file events. The following syntax is simplified from MOF code.
ms.assetid: 7d2f08e8-ec1f-4630-922a-548b55eadfda
title: PageFault_ImageLoadBacked class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PageFault_ImageLoadBacked
- PageFault_ImageLoadBacked.FileObject
- PageFault_ImageLoadBacked.DeviceChar
- PageFault_ImageLoadBacked.FileChar
- PageFault_ImageLoadBacked.LoadFlags
api_type: 
- NA
api_location: 
---

# PageFault\_ImageLoadBacked class

This class is the event type class for image load in page file events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{105}, EventTypeName{"ImageLoadBacked"}]
class PageFault_ImageLoadBacked : PageFault_V2
{
  uint32 FileObject;
  uint32 DeviceChar;
  uint16 FileChar;
  uint16 LoadFlags;
};
```

## Members

The **PageFault\_ImageLoadBacked** class has these types of members:

-   [Properties](#properties)

### Properties

The **PageFault\_ImageLoadBacked** class has these properties.

<dl> <dt>

**DeviceChar**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Format("x")
</dt> </dl>

Reserved.

</dd> <dt>

**FileChar**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Format("x")
</dt> </dl>

Reserved.

</dd> <dt>

**FileObject**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Match the value of this pointer to the **FileObject** pointer value in a [**FileIo\_Name**](fileio-name.md) event to determine the name of the file.

</dd> <dt>

**LoadFlags**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), Format("x")
</dt> </dl>

Reserved.

</dd> </dl>

## Remarks

The event is logged during an image section creation (for example, a DLL load) when the memory manager determines that the image needs to be copied into and run from the page file. Typically, images are run from the source file but pagefile-backing can occur when the memory manager determines that the source file may be modified asynchronously by existing writers or when the source file is on a removable media or a remote device.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**PageFault\_V2**](pagefault-v2.md)
</dt> </dl>

 

 




