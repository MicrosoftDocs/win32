---
description: The ELS transliteration services map UTF-16 text from one writing system to another writing system.
ms.assetid: 32e46c52-5c3c-4e22-8f4e-05286ee213ba
title: Transliteration Services
ms.topic: article
ms.date: 05/31/2018
---

# Transliteration Services

The ELS transliteration services map UTF-16 text from one writing system to another writing system. Each service is really data applying to a specific set of input and output Unicode scripts, and the actual transliteration is internal to the ELS platform. The application can optionally enumerate the available services for specific input and output scripts and select the service that it requires.

The platform maintains metadata for the ELS transliteration services. Metadata for each service provides a description of the service and lists the input and output scripts that the service supports. The metadata is represented by a [**MAPPING\_SERVICE\_INFO**](/windows/desktop/api/Elscore/ns-elscore-mapping_service_info) structure retrieved by the [**MappingGetServices**](/windows/desktop/api/Elscore/nf-elscore-mappinggetservices) function.

## Input to a Transliteration Service

The input to a transliteration service is UTF-16 text in one writing system.

## Output of a Transliteration Service

The output of a transliteration service is UTF-16 text mapped to a second writing system. If no appropriate transliteration mapping is available for any given chunk of the input text, the chunk remains unchanged.

## Transliteration Service Operation

A transliteration service maps Unicode text from an input script to an output script, character by character or term by term, as appropriate. The application can choose to obtain the specific transliteration service of interest by specifying input and output scripts when calling [**MappingGetServices**](/windows/desktop/api/Elscore/nf-elscore-mappinggetservices), or by providing the service GUID. Another option for the application is to enumerate all available transliteration services by specifying the service category "Transliteration" when calling **MappingGetServices**. In this case, the application calls each service and compares the results with the original text to see if the results have been changed by the operation of a particular service.

The application can request text recognition for an ELS transliteration service with a call to [**MappingRecognizeText**](/windows/desktop/api/Elscore/nf-elscore-mappingrecognizetext). When it receives the request, the transliteration service allocates a buffer to contain the transliterated data, and then performs text recognition for each code point in the input string supplied by the application.

> [!Note]  
> The original text and the transliterated text might have different lengths.

 

## Transliteration Service GUIDs

The GUIDs for the transliteration services are declared in Elssrvc.h, as shown in the following code.


```C++
// {A3A8333B-F4FC-42f6-A0C4-0462FE7317CB}
static const GUID ELS_GUID_TRANSLITERATION_HANT_TO_HANS =
    { 0xA3A8333B, 0xF4FC, 0x42f6, { 0xA0, 0xC4, 0x04, 0x62, 0xFE, 0x73, 0x17, 0xCB } };

// {3CACCDC8-5590-42dc-9A7B-B5A6B5B3B63B}
static const GUID ELS_GUID_TRANSLITERATION_HANS_TO_HANT =
    { 0x3CACCDC8, 0x5590, 0x42dc, { 0x9A, 0x7B, 0xB5, 0xA6, 0xB5, 0xB3, 0xB6, 0x3B } };

// {D8B983B1-F8BF-4a2b-BCD5-5B5EA20613E1}
static const GUID ELS_GUID_TRANSLITERATION_MALAYALAM_TO_LATIN =
    { 0xD8B983B1, 0xF8BF, 0x4a2b, { 0xBC, 0xD5, 0x5B, 0x5E, 0xA2, 0x06, 0x13, 0xE1 } };

// {C4A4DCFE-2661-4d02-9835-F48187109803}
static const GUID ELS_GUID_TRANSLITERATION_DEVANAGARI_TO_LATIN =
    { 0xC4A4DCFE, 0x2661, 0x4d02, { 0x98, 0x35, 0xF4, 0x81, 0x87, 0x10, 0x98, 0x03 } };

// {3DD12A98-5AFD-4903-A13F-E17E6C0BFE01}
static const GUID ELS_GUID_TRANSLITERATION_CYRILLIC_TO_LATIN =
    { 0x3DD12A98, 0x5AFD, 0x4903, { 0xA1, 0x3F, 0xE1, 0x7E, 0x6C, 0x0B, 0xFE, 0x01 } };

// {F4DFD825-91A4-489f-855E-9AD9BEE55727}
static const GUID ELS_GUID_TRANSLITERATION_BENGALI_TO_LATIN =
    { 0xF4DFD825, 0x91A4, 0x489f, { 0x85, 0x5E, 0x9A, 0xD9, 0xBE, 0xE5, 0x57, 0x27 } };
```



## Related topics

<dl> <dt>

[About Extended Linguistic Services](about-extended-linguistic-services.md)
</dt> </dl>

 

 



