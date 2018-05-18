---
Description: 'The Microsoft AC-3 Encoder filter encodes stereo PCM audio to a Dolby Digital bitstream.'
ms.assetid: '59d46ee2-d45f-4492-938d-39c55a7368e1'
title: 'Microsoft AC-3 Encoder'
---

# Microsoft AC-3 Encoder

The Microsoft AC-3 Encoder filter encodes stereo PCM audio to a Dolby Digital bitstream.

> [!Note]  
> The Microsoft implementation of the Dolby Digital technology is restricted under terms of the Dolby Digital licensing program to use by Microsoft applications.

 

> [!Note]  
> This filter is not supported on IA-64-based platforms.

 



Filter Information

Filter Interfaces

[**IBaseFilter**](ibasefilter.md)<br/>

Input Pin Media Types

**MEDIATYPE\_Audio**, **MEDIASUBTYPE\_PCM**<br/> The input type must be 48-kHz stereo, 16 bits per sample.<br/>

Input Pin Interfaces

[**IMemInputPin**](imeminputpin.md)<br/> [**IPin**](ipin.md)<br/> [**IQualityControl**](iqualitycontrol.md)<br/>

Output Pin Media Types

**MEDIATYPE\_Audio**, **MEDIASUBTYPE\_DOLBY\_AC3**<br/> **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_DOLBY\_AC3**<br/>

Output Pin Interfaces

[**IMediaSeeking**](imediaseeking.md)<br/> [**IPin**](ipin.md)<br/> [**IQualityControl**](iqualitycontrol.md)<br/>

Filter CLSID

**CLSID\_CMSAC3Enc** (declared in wmcodecdsp.h)

Executable

msac3enc.dll

[Merit](merit.md)

**MERIT\_DO\_NOT\_USE**

[Filter Category](filter-categories.md)

**CLSID\_LegacyAmFilterCategory**



 

## Remarks

This filter is not available for use by third-party applications.

## Requirements



|                                     |                                                                                                                                                                               |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Home Premium, Windows Vista Ultimate, Windows 7 Home Premium, Windows 7 Professional, Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                                     |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl>                                                                                       |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




