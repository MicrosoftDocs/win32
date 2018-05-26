---
Description: Gets the characteristics of the media source from the Source Reader.
ms.assetid: 4cd48b69-6f7b-4b13-86f3-b38969025f70
title: MF\_SOURCE\_READER\_MEDIASOURCE\_CHARACTERISTICS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SOURCE\_READER\_MEDIASOURCE\_CHARACTERISTICS attribute

Gets the characteristics of the media source from the [Source Reader](source-reader.md).

## Data type

**UINT32**

The value is a bitwise **OR** of flags from the [**MFMEDIASOURCE\_CHARACTERISTICS**](/windows/win32/mfidl/ne-mfidl-_mfmediasource_characteristics?branch=master) enumeration.

## Remarks

To get this attribute, call the [**IMFSourceReader::GetPresentationAttribute**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-getpresentationattribute?branch=master) method on the source reader. Set the *dwStreamIndex* parameter to **MF\_SOURCE\_READER\_MEDIASOURCE** and the *guidAttribute* parameter to MF\_SOURCE\_READER\_MEDIASOURCE\_CHARACTERISTICS.

The **PROPVARIANT** type for this attribute is **VT\_UI4**.

## Examples


```C++
HRESULT GetSourceFlags(IMFSourceReader *pReader, ULONG *pulFlags)
{
    ULONG flags = 0;

    PROPVARIANT var;
    PropVariantInit(&amp;var);

    HRESULT hr = pReader->GetPresentationAttribute(
        MF_SOURCE_READER_MEDIASOURCE, 
        MF_SOURCE_READER_MEDIASOURCE_CHARACTERISTICS, 
        &amp;var);

    if (SUCCEEDED(hr))
    {
        hr = PropVariantToUInt32(var, &amp;flags);
    }
    if (SUCCEEDED(hr))
    {
        *pulFlags = flags;
    }

    PropVariantClear(&amp;var);
    return hr;
}
```



## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> </dl>

 

 




