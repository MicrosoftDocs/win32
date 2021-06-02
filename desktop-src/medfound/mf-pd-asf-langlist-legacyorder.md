---
description: Contains a list of RFC 1766 languages used in the current presentation.
ms.assetid: 8853bd88-d51a-478c-8c78-cf69a260e295
title: MF_PD_ASF_LANGLIST_LEGACYORDER attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_LANGLIST\_LEGACYORDER attribute

Contains a list of RFC 1766 languages used in the current presentation.

## Data type

**BYTE \[\]**

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob).

To set this attribute, call [**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob).

## Applies to

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)

## Remarks

This attribute applies to presentation descriptors that were generated from the [ASF ContentInfo Object](asf-contentinfo-object.md) by a call to [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor). The format of the byte array is as follows:



| Language List Object field | Data type    | Size    | Description                            |
|----------------------------|--------------|---------|----------------------------------------|
| Language ID Records Count  | **DWORD**    | 4 bytes | Number of languages                    |
| Language ID Records        | **BYTE**\[\] | Varies  | Array of language strings (see below). |



 

The first **DWORD** is the number of languages, followed by an array of language identifier strings. Each string has the following format:



| Language List Object field | Data type     | Size    | Description                                                                               |
|----------------------------|---------------|---------|-------------------------------------------------------------------------------------------|
| Language ID Length         | **DWORD**     | 4 bytes | The length of the string in bytes, including the size of the trailing **NULL** character. |
| Language ID                | **WCHAR**\[\] | Varies  | A null-terminated string containing the RFC 1766 language name.                           |



 

Each string is a language tag compliant with RFC 1766.

Use this attribute only for backward compatibility with the enumeration order of the [**IWMReaderAdvanced4**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4) interface in the Windows Media Format SDK. The language strings are stored in a different order in the [**MF\_PD\_ASF\_LANGLIST**](mf-pd-asf-langlist-attribute.md) attribute.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 
