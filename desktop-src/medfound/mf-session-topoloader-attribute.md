---
Description: Contains the CLSID of a topology loader for the Media Session.
ms.assetid: 672274fb-71fc-49ca-bab6-1fc4de21d17c
title: MF\_SESSION\_TOPOLOADER attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SESSION\_TOPOLOADER attribute

Contains the CLSID of a topology loader for the Media Session.

## Data type

**GUID**

## Remarks

You can use this attribute to provide a custom topology loader for the Media Session.

Set this attribute using the *pConfiguration* parameter of the [**MFCreateMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatemediasession?branch=master) function or the [**MFCreatePMPMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatepmpmediasession?branch=master) function.

If this attribute is set, the Media Session calls **CoCreateInstance** with the specified CLSID when it creates the topology loader. The object created by this CLSID must expose the [**IMFTopoLoader**](/windows/win32/mfidl/nn-mfidl-imftopoloader?branch=master) interface.

If this attribute is not set, the Media Session creates the default topology loader provided in Media Foundation.

A topology loader must support multithreaded apartments. You should register the topology loader as ThreadingModel="Both". Also, if you are using the topology loader inside the protected media path (PMP), the topology loader must be a trusted component. For more information, see [Protected Media Path](protected-media-path.md).

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
</dt> <dt>

[Custom Topology Loaders](custom-topology-loaders.md)
</dt> </dl>

 

 




