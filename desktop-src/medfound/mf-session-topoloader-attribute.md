---
Description: 'Contains the CLSID of a topology loader for the Media Session.'
ms.assetid: '672274fb-71fc-49ca-bab6-1fc4de21d17c'
title: 'MF\_SESSION\_TOPOLOADER attribute'
---

# MF\_SESSION\_TOPOLOADER attribute

Contains the CLSID of a topology loader for the Media Session.

## Data type

**GUID**

## Remarks

You can use this attribute to provide a custom topology loader for the Media Session.

Set this attribute using the *pConfiguration* parameter of the [**MFCreateMediaSession**](mfcreatemediasession.md) function or the [**MFCreatePMPMediaSession**](mfcreatepmpmediasession.md) function.

If this attribute is set, the Media Session calls **CoCreateInstance** with the specified CLSID when it creates the topology loader. The object created by this CLSID must expose the [**IMFTopoLoader**](imftopoloader.md) interface.

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

[**IMFAttributes::GetGUID**](imfattributes-getguid.md)
</dt> <dt>

[**IMFAttributes::SetGUID**](imfattributes-setguid.md)
</dt> <dt>

[Media Session Attributes](media-session-attributes.md)
</dt> <dt>

[Custom Topology Loaders](custom-topology-loaders.md)
</dt> </dl>

 

 




