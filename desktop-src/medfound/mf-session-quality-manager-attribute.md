---
Description: Contains the CLSID of a quality manager for the Media Session.
ms.assetid: 24b4a5e3-84f1-44d0-a8ac-75c127ec8a8a
title: MF\_SESSION\_QUALITY\_MANAGER attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SESSION\_QUALITY\_MANAGER attribute

Contains the CLSID of a quality manager for the Media Session.

## Data type

**GUID**

## Remarks

You can use this attribute to provide a custom quality manager for the Media Session.

Set this attribute by using the *pConfiguration* parameter of the [**MFCreateMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatemediasession?branch=master) or [**MFCreatePMPMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatepmpmediasession?branch=master) function.

If this attribute is set, the Media Session calls **CoCreateInstance** with the specified CLSID to create the quality manager. The object created by this CLSID must expose the [**IMFQualityManager**](/windows/win32/mfidl/nn-mfidl-imfqualitymanager?branch=master) interface.

If this attribute is not set, the Media Session creates the default quality manager provided in Media Foundation.

If you want to run the Media Session with no quality manager at all, set this attribute to **GUID\_NULL**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master)
</dt> <dt>

[**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master)
</dt> <dt>

[Media Session Attributes](media-session-attributes.md)
</dt> </dl>

 

 




