---
error-parsing-yaml: 
---

# WM/WMRVContentProtectedPercent

Specifies the percentage of a DVR-MS file that is protected.

## Data Type

**DWORD** (STREAMBUFFER\_TYPE\_DWORD)

## Remarks

Windows Media Center sets this attribute if the file contains any protected content. The value of this attribute is a number from 0 to 100, indicating the percentage of the file that is protected.

> [!Note]  
> The value might exceed 100. Treat any values over 100 as equivalent to 100 percent.

 

## See also

<dl> <dt>

[Detecting Content Protection in Recorded TV Files](detecting-content-protection-in-recorded-tv-files.md)
</dt> <dt>

[Stream Buffer Engine Attributes](stream-buffer-engine-attributes.md)
</dt> </dl>

 

 




