---
Description: 'Sets the average &\#0034;leaky bucket&\#0034; parameters (see Remarks) for encoding a Windows Media file. Set this attribute by using the IMFASFStreamConfig interface.'
ms.assetid: '5aa570eb-1004-4942-9a63-b8f6373d4e53'
title: 'MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1 attribute'
---

# MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1 attribute

Sets the average "leaky bucket" parameters (see Remarks) for encoding a Windows Media file. Set this attribute by using the [**IMFASFStreamConfig**](imfasfstreamconfig.md) interface.

## Data type

Byte array

## Remarks

The value of this attribute is an array of three **DWORD**s, in the following order:

-   Bit rate, in bits per second.
-   Buffer window, in milliseconds.
-   Initial buffer fullness, in bytes.

For more information about the leaky bucket concept, see the topic [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md) in the Windows Media Format SDK documentation.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[ASF Attributes](asf-attributes.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](imfattributes-getblob.md)
</dt> <dt>

[**IMFAttributes::SetBlob**](imfattributes-setblob.md)
</dt> <dt>

[**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md)
</dt> </dl>

 

 




