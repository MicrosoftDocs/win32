---
Description: Sets the Key ID for the sample.
ms.assetid: 75339350-05AA-486E-9C28-11070C0DA61D
title: MFSampleExtension\_Content\_KeyID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_Content\_KeyID attribute

Sets the Key ID for the sample.

## Data type

**GUID**

## Examples

The following example shows how to set the Key ID for the sample.


```C++
// m_spSample is a IMFSample
// guidKID is a GUID

m_spSample->SetGUID( MFSampleExtension_Content_KeyID, guidKID );
```



## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)
</dt> <dt>

[MFSampleExtension\_Encryption\_SubSampleMappingSplit](mfsampleextension-encryption-subsamplemappingsplit.md)
</dt> </dl>

 

 




