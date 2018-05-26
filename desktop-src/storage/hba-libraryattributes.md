---
title: HBA\_LibraryAttributes structure
description: The HBA\_LibraryAttributes structure holds the library attributes.
ms.assetid: 9dc03c5d-5e14-4399-b282-f0385a85a16c
keywords:
- HBA_LibraryAttributes structure Storage Devices
- HBA_LIBRARYATTRIBUTES structure Storage Devices
- PHBA_LIBRARYATTRIBUTES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HBA_LIBRARYATTRIBUTES
api_location:
- hbaapi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBA\_LibraryAttributes structure

The HBA\_LibraryAttributes structure holds the library attributes.

## Syntax


```C++
typedef struct HBA_LibraryAttributes {
  HBA_BOOLEAN final;
  char        LibPath[256];
  char        VName[256];
  char        VVersion[256];
  struct tm  build_date;
} HBA_LIBRARYATTRIBUTES, *PHBA_LIBRARYATTRIBUTES;
```



## Members

<dl> <dt>

**final**
</dt> <dd>

Indicates, when **TRUE**, that the library implements the final and most recent draft of the T11 committee's *Fibre Channel HBA API* specification. When **FALSE** this member indicates that the library is not compliant with the most recent version of the specification.

</dd> <dt>

**LibPath**
</dt> <dd>

Contains the fully qualified path name of the library DLL file.

</dd> <dt>

**VName**
</dt> <dd>

Contains the name of the organization that developed the library code.

</dd> <dt>

**VVersion**
</dt> <dd>

Identifies the code revision of the library.

</dd> <dt>

**build\_date**
</dt> <dd>

Contains a structure of type tm that holds a timestamp that indicates when the library was built. The structure may contain the following members:

-   **tm\_sec** Contains a value between 0 and 59 that indicates the number of seconds.
-   **tm\_min** Contains a value between 0 and 59 that indicates the number of minutes.
-   **tm\_hour** Contains a value between 0 and 23 that indicates the number of hours since midnight.
-   **tm\_mday** Contains a value between 1 and 31 that indicates the day of the month.
-   **tm\_mon** Contains a value between 0 and 11 that indicates the number of months since January.
-   **tm\_year** Indicates the number of years since 1900.
-   **tm\_wday** Contains a value between 0 and 6 that indicates the number of days since Sunday.
-   **tm\_yday** Contains a value between 0 and 365 that indicates the number of days since January 1.
-   **tm\_isdst** Indicates daylight savings time when TRUE and normal time when FALSE.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_LibraryAttributes%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





