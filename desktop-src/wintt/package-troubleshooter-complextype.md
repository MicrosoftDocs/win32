---
title: Troubleshooter Complex Type
description: Specifies the troubleshooting script to run.
ms.assetid: 812d6ffb-78d6-4e6b-b008-f5ec8086528c
keywords:
- Troubleshooter complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Troubleshooter
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooter Complex Type

Specifies the troubleshooting script to run.

``` syntax
<xs:complexType name="Troubleshooter">
    <xs:sequence>
        <xs:element name="Script"
            type="dcmPS:Script"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="ExtensionPoint"
            type="dcmPS:ExtensionPoint"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element        | Type                                                               | Description                                                                                                                                                     |
|----------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtensionPoint | [**dcmPS:ExtensionPoint**](package-extensionpoint-complextype.md) | Used by the client to extend the functionality of the Troubleshooter node. The MSDT client does not support extensions for the Troubleshooter node. <br/> |
| Script         | [**dcmPS:Script**](package-script-complextype.md)                 | The name of the troubleshooting script to run. <br/>                                                                                                      |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**GlobalDiagnosticPackage Complex Type**](package-globaldiagnosticpackage-complextype.md)
</dt> <dt>

[**LocalRootcause Complex Type**](package-localrootcause-complextype.md)
</dt> <dt>

[**Troubleshooter (GlobalDiagnosticPackage) Element**](package-troubleshooter-globaldiagnosticpackage-element.md)
</dt> <dt>

[**Troubleshooter (LocalRootcause) Element**](package-troubleshooter-localrootcause-element.md)
</dt> </dl>

 

 





