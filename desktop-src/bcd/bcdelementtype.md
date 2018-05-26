---
title: BcdElementType structure
description: Describes the layout of the BCD element types.
ms.assetid: 1b296608-7866-4fd9-a81d-5b1944b2d78f
keywords:
- BcdElementType structure Boot Config
topic_type:
- apiref
api_name:
- BcdElementType
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BcdElementType structure

Describes the layout of the BCD element types.

## Syntax


```C++
typedef struct {
  union {
    ULONG  PackedValue;
    struct {
      ULONG SubType  :24;
      ULONG Format  :4;
      ULONG Class  :4;
    };
  };
} BcdElementType;
```



## Members

<dl> <dt>

**PackedValue**
</dt> <dd></dd> <dt>

**SubType**
</dt> <dd>

Class-specific subtype for the data. The valid values differ based on class.

</dd> <dt>

**Format**
</dt> <dd>

Describes the data format for elements of this type.



| Value                                                                                                                                                                                                                                         | Meaning                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Device"></span><span id="device"></span><span id="DEVICE"></span><dl> <dt>**Device**</dt> <dt>0x1</dt> </dl>                     | A boot environment device, represented as a **GUID** in string format. For example "{500ec897-0b25-449a-8ecd-8d81628baa9c}".<br/> |
| <span id="String"></span><span id="string"></span><span id="STRING"></span><dl> <dt>**String**</dt> <dt>0x2</dt> </dl>                     | A **NULL**-terminated Unicode string.<br/>                                                                                        |
| <span id="Object"></span><span id="object"></span><span id="OBJECT"></span><dl> <dt>**Object**</dt> <dt>0x3</dt> </dl>                     | A **GUID** in string format.<br/>                                                                                                 |
| <span id="ObjectList"></span><span id="objectlist"></span><span id="OBJECTLIST"></span><dl> <dt>**ObjectList**</dt> <dt>0x4</dt> </dl>     | An array of **GUID**s.<br/>                                                                                                       |
| <span id="Integer"></span><span id="integer"></span><span id="INTEGER"></span><dl> <dt>**Integer**</dt> <dt>0x5</dt> </dl>                 | A 64-bit integer.<br/>                                                                                                            |
| <span id="Boolean"></span><span id="boolean"></span><span id="BOOLEAN"></span><dl> <dt>**Boolean**</dt> <dt>0x6</dt> </dl>                 | A boolean.<br/>                                                                                                                   |
| <span id="IntegerList"></span><span id="integerlist"></span><span id="INTEGERLIST"></span><dl> <dt>**IntegerList**</dt> <dt>0x7</dt> </dl> | An array of 64-bit integers.<br/>                                                                                                 |



 

</dd> <dt>

**Class**
</dt> <dd>

Describes the consumer of the element type.



| Value                                                                                                                                                                                                                                         | Meaning                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Library"></span><span id="library"></span><span id="LIBRARY"></span><dl> <dt>**Library**</dt> <dt>0x1</dt> </dl>                 | Element types that span both applications and devices. Elements of this class can only contain other Library class BCD elements.<br/> |
| <span id="Application"></span><span id="application"></span><span id="APPLICATION"></span><dl> <dt>**Application**</dt> <dt>0x2</dt> </dl> | Element types specific to a boot applications.<br/>                                                                                   |
| <span id="Device"></span><span id="device"></span><span id="DEVICE"></span><dl> <dt>**Device**</dt> <dt>0x3</dt> </dl>                     | Element types specific to a boot device.<br/>                                                                                         |
| <span id="OEM"></span><span id="oem"></span><dl> <dt>**OEM**</dt> <dt>0x5</dt> </dl>                                                       | Element types specific to an Original Equipment Manufacturer (OEM).<br/>                                                              |



 

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
</dt> <dt>

[**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
</dt> <dt>

[**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
</dt> <dt>

[**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
</dt> <dt>

[**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)
</dt> </dl>

 

 





