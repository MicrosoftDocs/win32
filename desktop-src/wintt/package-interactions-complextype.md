---
title: Interactions Complex Type
description: Defines the interactions that the troubleshooting pack uses.
ms.assetid: '41d27d13-f481-4d98-a9ce-26804933fb08'
keywords: ["Interactions complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Interactions
api_type:
- Schema
---

# Interactions Complex Type

Defines the interactions that the troubleshooting pack uses.

``` syntax
<xs:complexType name="Interactions">
    <xs:sequence>
        <xs:element name="SingleResponseInteractions"
            type="dcmPS:SingleResponseInteractions"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="MultipleResponseInteractions"
            type="dcmPS:MultipleResponseInteractions"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="TextInteractions"
            type="dcmPS:TextInteractions"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="PauseInteractions"
            type="dcmPS:PauseInteractions"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="LaunchUIInteractions"
            type="dcmPS:LaunchUIInteractions"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                      | Type                                                                                           | Description                                                           |
|------------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| LaunchUIInteractions         | [**dcmPS:LaunchUIInteractions**](package-launchuiinteractions-complextype.md)                 | A collection of interactions that launch UI applications. <br/> |
| MultipleResponseInteractions | [**dcmPS:MultipleResponseInteractions**](package-multipleresponseinteractions-complextype.md) | A collection of multiple response interactions.<br/>            |
| PauseInteractions            | [**dcmPS:PauseInteractions**](package-pauseinteractions-complextype.md)                       | A collection of pause interactions.<br/>                        |
| SingleResponseInteractions   | [**dcmPS:SingleResponseInteractions**](package-singleresponseinteractions-complextype.md)     | A collection of single response interactions.<br/>              |
| TextInteractions             | [**dcmPS:TextInteractions**](package-textinteractions-complextype.md)                         | A collection of text input interactions.<br/>                   |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Interactions (GlobalDiagnosticPackage) Element**](package-interactions-globaldiagnosticpackage-element.md)
</dt> <dt>

[**Interactions (LocalDiagnosticPackage) Element**](package-interactions-localdiagnosticpackage-element.md)
</dt> </dl>

 

 





