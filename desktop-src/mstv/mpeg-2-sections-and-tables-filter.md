---
title: MPEG-2 Sections and Tables Filter
description: This filter is no longer available for use as of Windows 7.
ms.assetid: '03027748-03da-485c-8787-3cf171fff1e0'
keywords: ["MPEG-2 Sections and Tables Filter Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- MPEG-2 Sections and Tables Filter
api_location:
- Mpeg2data.h
api_type:
- HeaderDef
---

# MPEG-2 Sections and Tables Filter

\[This filter is no longer available for use as of Windows 7. Instead, use the [**IPSITables**](ipsitables.md) interface to get program specific information (PSI) tables from an MPEG-2 transport stream.\]

The MPEG-2 Sections and Tables filter receives PSI tables from an MPEG-2 transport stream.



|                                            |                                                                                                                             |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                          | [**IBaseFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389526), [**IMpeg2Data**](impeg2data.md)                                                      |
| Input Pin Media Types                      | Major Type: MEDIATYPE\_MPEG2\_SECTIONS<br/> Subtype: MEDIASUBTYPE\_MPEG2DATA<br/> Format block: None<br/> |
| Input Pin Interfaces                       | [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912)                                                        |
| Output Pin Media Types                     | Not applicable                                                                                                              |
| Output Pin Interfaces                      | Not applicable                                                                                                              |
| Filter CLSID                               | CLSID\_Mpeg2Data                                                                                                            |
| [Merit](https://msdn.microsoft.com/library/windows/desktop/dd390674)                       | MERIT\_NORMAL                                                                                                               |
| [Filter Category](https://msdn.microsoft.com/library/windows/desktop/dd375655) | KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION                                                                                     |



 

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| Header<br/>                | <dl> <dt>Mpeg2data.h</dt> </dl> |



## See also

<dl> <dt>

[BDA Filters](bda-filters.md)
</dt> <dt>

[Getting MPEG-2 PSI Tables](getting-mpeg2-psi-tables.md)
</dt> <dt>

[Microsoft TV Technologies](microsoft-tv-technologies-portal.md)
</dt> </dl>

 

 





