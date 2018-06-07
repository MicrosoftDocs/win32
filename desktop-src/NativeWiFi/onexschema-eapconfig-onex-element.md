---
Description: specifies the EAPHost configuration.
ms.assetid: 71ec3ed6-3670-46fc-a24b-580d15297437
title: EAPConfig (OneX) Element
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EAPConfig (OneX) Element

The **EAPConfig** (OneX) element specifies the EAPHost configuration.

Unlike most elements in the 802.1X profile schema, this element is in the `http://www.microsoft.com/provisioning/EapHostConfig` namespace. Its child elements are defined in the [eaphostconfig schema](https://msdn.microsoft.com/e1e4dda3-6bf4-4da5-9e14-63548ec86836). The [**EapHostConfig**](https://msdn.microsoft.com/6c42d71e-0c61-48e4-a447-cfd1eae90297) element is a child of the **EAPConfig** element.

``` syntax
<xs:element name="EAPConfig">
    <xs:complexType>
        <xs:sequence>
            <xs:any
                processContents="lax"
                minOccurs="1"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **EAPConfig** element is defined by the [**OneX**](onexschema-onex-element.md) element.

## Requirements



|                                     |                                                                     |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> </dl>

 

 




