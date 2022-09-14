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
ms.date: 05/31/2018
---

# Signature\_Name

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

 

 




