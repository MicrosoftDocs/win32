---
Description: Data error rate, in bit errors per second, for a video media type.
ms.assetid: 90433ff4-a563-4751-86d9-caac0cc58194
title: MF\_MT\_AVG\_BIT\_ERROR\_RATE attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_AVG\_BIT\_ERROR\_RATE attribute

Data error rate, in bit errors per second, for a video media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **dwBitErrorRate** member of the [**VIDEOINFOHEADER**](https://msdn.microsoft.com/windows/desktop/a175592b-0dc1-4001-b52f-785407965932) and [**VIDEOINFOHEADER2**](https://msdn.microsoft.com/windows/desktop/5e3d5bf0-435f-45da-8409-a1463b56a7ae) structures.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




