---
title: Verifier Complex Type
description: Specifies the verifier script to run.
ms.assetid: 2e0b8357-fcde-447c-87cc-bca262c47cfe
keywords:
- Verifier complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Verifier
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Verifier Complex Type

Specifies the verifier script to run.

``` syntax
<xs:complexType name="Verifier">
    <xs:sequence>
        <xs:element name="Script"
            type="dcmPS:Script"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="ExtensionPoint"
            type="dcmPS:ExtensionPoint"
            minOccurs="0"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element        | Type                                                               | Description                                                                                                                                         |
|----------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtensionPoint | [**dcmPS:ExtensionPoint**](package-extensionpoint-complextype.md) | Used by the client to extend the functionality of the Verifier node. The MSDT client does not support extensions for the Verifier node. <br/> |
| Script         | [**dcmPS:Script**](package-script-complextype.md)                 | The verifier script to run.<br/>                                                                                                              |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**GlobalRootcause Complex Type**](package-globalrootcause-complextype.md)
</dt> <dt>

[**LocalRootcause Complex Type**](package-localrootcause-complextype.md)
</dt> <dt>

[**Verifier (GlobalRootcause) Element**](package-verifier-globalrootcause-element.md)
</dt> <dt>

[**Verifier (LocalRootcause) Element**](package-verifier-localrootcause-element.md)
</dt> </dl>

 

 





