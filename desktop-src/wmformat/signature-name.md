---
title: Signature_Name
description: The Signature\_Name attribute contains the name on the certificate used to sign the file. This attribute is valid only if the Is\_Trusted attribute is set to True.
ms.assetid: 3f3ab10c-731b-4075-8f73-3c2e62e010b9
keywords:
- Signature_Name windows Media Format
topic_type:
- apiref
api_name:
- Signature_Name
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Signature\_Name

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Signature\_Name** attribute contains the name on the certificate used to sign the file. This attribute is valid only if the [**Is\_Trusted**](is-trusted.md) attribute is set to True.

## Global Constant

g\_wszWMSignature\_Name

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

This is a coded attribute.

This attribute cannot be duplicated at the file level. If this attribute is used for an individual stream, it will be treated as custom metadata and will not convey its normal meaning to the objects of the Windows Media Format SDK.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




