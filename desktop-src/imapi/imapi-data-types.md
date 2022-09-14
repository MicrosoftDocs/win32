---
title: IMAPI Data Types (Imapi2.h)
description: Specifications for optical media and associated devices define range values for items such as the DVD structure description, disc information description, and feature page size.
ms.assetid: 8797a8d0-5ce5-4b16-9d41-c22fa0d67dcf
keywords:
- ULONG_IMAPI2_DVD_STRUCTURE
- ULONG_IMAPI2_ADAPTER_DESCRIPTOR
- ULONG_IMAPI2_DEVICE_DESCRIPTOR
- ULONG_IMAPI2_DISC_INFORMATION
- ULONG_IMAPI2_TRACK_INFORMATION
- ULONG_IMAPI2_FEATURE_PAGE
- ULONG_IMAPI2_MODE_PAGE
- ULONG_IMAPI2_ALL_FEATURE_PAGES
- ULONG_IMAPI2_ALL_PROFILES
- ULONG_IMAPI2_ALL_MODE_PAGES
- ULONG_IMAPI2_NONZERO
- ULONG_IMAPI2_NOT_NEGATIVE
ms.topic: reference
ms.date: 05/31/2018
---

# IMAPI Data Types

Specifications for optical media and associated devices define range values for items such as the DVD structure description, disc information description, and feature page size. IMAPI defines the following unsigned long integer (ULONG) types that enforce range value limits. These types are defined strictly for optimal IDL validation of parameters and as a documentation aid to callers regarding the upper limits for certain data transfer operations available.


```C++
typedef ULONG ULONG_IMAPI2_DVD_STRUCTURE;
typedef ULONG ULONG_IMAPI2_ADAPTER_DESCRIPTOR;
typedef ULONG ULONG_IMAPI2_DEVICE_DESCRIPTOR;
typedef ULONG ULONG_IMAPI2_DISC_INFORMATION;
typedef ULONG ULONG_IMAPI2_TRACK_INFORMATION;
typedef ULONG ULONG_IMAPI2_FEATURE_PAGE;
typedef ULONG ULONG_IMAPI2_MODE_PAGE;
typedef ULONG ULONG_IMAPI2_ALL_FEATURE_PAGES;
typedef ULONG ULONG_IMAPI2_ALL_PROFILES;
typedef ULONG ULONG_IMAPI2_ALL_MODE_PAGES;
typedef ULONG ULONG_IMAPI2_NONZERO;
typedef ULONG ULONG_IMAPI2_NOT_NEGATIVE;
```





| Data type                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ULONG_IMAPI2_DVD_STRUCTURE"></span><span id="ulong_imapi2_dvd_structure"></span>**ULONG\_IMAPI2\_DVD\_STRUCTURE**                | Range: 0,65535 (0,0x0000FFFF)<br/> The DVD structure is limited to 64KB due to a two-byte allocation field.<br/>                                                                                                                                                                                     |
| <span id="ULONG_IMAPI2_ADAPTER_DESCRIPTOR"></span><span id="ulong_imapi2_adapter_descriptor"></span>**ULONG\_IMAPI2\_ADAPTER\_DESCRIPTOR** | Range: 0,268435455 (0,0x0FFFFFFF)<br/> The adapter descriptor is not implicitly limited in size.<br/>                                                                                                                                                                                                |
| <span id="ULONG_IMAPI2_DEVICE_DESCRIPTOR"></span><span id="ulong_imapi2_device_descriptor"></span>**ULONG\_IMAPI2\_DEVICE\_DESCRIPTOR**    | Range: 0,268435455 (0,0x0FFFFFFF)<br/> The device descriptor is not implicitly limited in size.<br/>                                                                                                                                                                                                 |
| <span id="ULONG_IMAPI2_DISC_INFORMATION"></span><span id="ulong_imapi2_disc_information"></span>**ULONG\_IMAPI2\_DISC\_INFORMATION**       | Range: 0,65538 (0,0x00010002)<br/> Disc information is limited to 64KB plus 2 bytes for the size field.<br/>                                                                                                                                                                                         |
| <span id="ULONG_IMAPI2_TRACK_INFORMATION"></span><span id="ulong_imapi2_track_information"></span>**ULONG\_IMAPI2\_TRACK\_INFORMATION**    | Range: 0,65538 (0,0x00010002)<br/> Track information is limited to 64KB plus 2 bytes for the size field.<br/>                                                                                                                                                                                        |
| <span id="ULONG_IMAPI2_FEATURE_PAGE"></span><span id="ulong_imapi2_feature_page"></span>**ULONG\_IMAPI2\_FEATURE\_PAGE**                   | Range: 0,256 (0,0x00000100)<br/> A single feature page is limited to 256 bytes.<br/>                                                                                                                                                                                                                 |
| <span id="ULONG_IMAPI2_MODE_PAGE"></span><span id="ulong_imapi2_mode_page"></span>**ULONG\_IMAPI2\_MODE\_PAGE**                            | Range: 0,257 (0,0x00000101)<br/> A single mode page is limited to 257 bytes.<br/>                                                                                                                                                                                                                    |
| <span id="ULONG_IMAPI2_ALL_FEATURE_PAGES"></span><span id="ulong_imapi2_all_feature_pages"></span>**ULONG\_IMAPI2\_ALL\_FEATURE\_PAGES**   | Range: 0,65536 (0,0x00010000)<br/> The number of features is limited to a two-byte field.<br/>                                                                                                                                                                                                       |
| <span id="ULONG_IMAPI2_ALL_PROFILES"></span><span id="ulong_imapi2_all_profiles"></span>**ULONG\_IMAPI2\_ALL\_PROFILES**                   | Range: 0,63 (0,0x0000003F)<br/> The number of profiles for a device is the number of profiles that fit in a single feature. Each profile occupies four bytes. A single feature can hold 252 additional bytes of data, enough to store a maximum of 63 profiles.<br/>                                 |
| <span id="ULONG_IMAPI2_ALL_MODE_PAGES"></span><span id="ulong_imapi2_all_mode_pages"></span>**ULONG\_IMAPI2\_ALL\_MODE\_PAGES**            | Range: 0,32763 (0,0x00007FFB)<br/> Count of the mode pages for a device. The count, via MODE\_SENSE10, is limited to a two-byte field.<br/> The mode parameter header is 8 bytes. Each page is at least two bytes. The maximum number of mode pages is 32763: (65535 - 8)/2 rounded down.<br/> |
| <span id="ULONG_IMAPI2_NONZERO"></span><span id="ulong_imapi2_nonzero"></span>**ULONG\_IMAPI2\_NONZERO**                                   | Range: 1,2147483647 (1,0x7FFFFFFF)<br/> Generic nonzero value that can be used to verify that a value is not zero.<br/>                                                                                                                                                                              |
| <span id="ULONG_IMAPI2_NOT_NEGATIVE"></span><span id="ulong_imapi2_not_negative"></span>**ULONG\_IMAPI2\_NOT\_NEGATIVE**                   | Range: 0, 2147483647 (0,0x7FFFFFFF)<br/> A 32-bit integer with non-negative value.<br/>                                                                                                                                                                                                              |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Imapi2.h</dt> </dl> |



 

 





