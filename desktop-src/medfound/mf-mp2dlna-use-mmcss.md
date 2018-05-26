---
Description: Specifies whether the Digital Living Network Alliance (DLNA) media sink uses the Multimedia Class Scheduler Service (MMCSS).
ms.assetid: 4c27e2ec-624a-4b1f-bea9-3aaad1534c9b
title: MF\_MP2DLNA\_USE\_MMCSS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MP2DLNA\_USE\_MMCSS attribute

Specifies whether the Digital Living Network Alliance (DLNA) media sink uses the Multimedia Class Scheduler Service (MMCSS).

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

To set this attribute on the DLNA media sink, query the media sink for the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) interface. Set the attribute before streaming begins.

If this attribute is **TRUE**, the DLNA media sink registers itself with MMCSS.

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

 

 




