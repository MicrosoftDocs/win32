---
description: Sets the sub-sample mapping for the sample indicating the clear and encrypted bytes in the sample data.
ms.assetid: E672F53D-2083-430B-90D2-A1DA482EF9E1
title: MFSampleExtension_Encryption_SubSampleMappingSplit attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_Encryption\_SubSampleMappingSplit attribute

Sets the sub-sample mapping for the sample indicating the clear and encrypted bytes in the sample data.

## Data type

**BLOB**

## Remarks

The **BLOB** should contain an array of byte ranges as DWORDs where every two DWORDs makes a set. The first DWORD in each set is the number of clear bytes and the second DWORD of the set is the number of encrypted bytes. Note that a pair of 0s is not a valid set (either value can be 0, but not both). The array of byte ranges indicate which ranges to decrypt, including the possibility that the entire sample should not be decrypted. It is recommended that this should not be set on clear samples, though it is possible to achieve the same result by setting it with the appropriate values.

## Examples

The following example shows how to set MFSampleExtension\_Encryption\_SubSampleMappingSplit.


```C++
// m_spSample is a IMFSample
// pdwSubSampleMap is a DWORD*
// dwSubSampleMapSize is a DWORD

m_spSample->SetBlob( MFSampleExtension_Encryption_SubSampleMappingSplit,
                    (BYTE*)pdwSubSampleMap, 
                    dwSubSampleMapSize * sizeof(DWORD) );
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)
</dt> <dt>

[MFSampleExtension\_Content\_KeyID](mfsampleextension-content-keyid.md)
</dt> </dl>

 

 




