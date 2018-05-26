---
Description: Specifies the encoding quality for the Digital Living Network Alliance (DLNA) media sink.
ms.assetid: 4cf745ab-66ae-40f2-b5c4-3f72f1b9badb
title: MF\_MP2DLNA\_ENCODE\_QUALITY attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MP2DLNA\_ENCODE\_QUALITY attribute

Specifies the encoding quality for the Digital Living Network Alliance (DLNA) media sink.

## Data type

**UINT32**

Range: 0–18

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

Higher numbers indicate better encoding quality. Lower numbers indicate faster encoding, but lower encoding quality. The default value is 9.

To set this attribute on the DLNA media sink, query the media sink for the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) interface. Set the attribute before streaming begins.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmp2dlna.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




