---
Description: Assigns enumeration text to a range of values. Each enumRange element specifies a minimum value, and extends until the next element minimum value, or until there are no more enumRange elements.
ms.assetid: 00c56c2d-6693-4b09-b28a-21d69930bf35
title: enumRange
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# enumRange

Assigns enumeration text to a range of values. Each [enumRange](https://www.bing.com/search?q=enumRange) element specifies a minimum value, and extends until the next element minimum value, or until there are no more enumRange elements.

## Syntax

``` syntax
<!-- enumRange -->
<xs:element name="enumRange" minOccurs="0" maxOccurs="unbounded">
    <xs:complexType>
        <xs:sequence>
            <xs:element ref="image" minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
            <xs:attribute name="minValue" type="xs:integer" use="required"/>
            <xs:attribute name="setValue" type="xs:integer"/>
            <xs:attribute name="text" type="xs:string"/>
            <xs:attribute name="name" type="canonical-name"/> <!--Maximum of 64 characters-->
            <xs:attribute name="mnemonics" type="xs:string"/> 
    </xs:complexType>
</xs:element>
```

## Element Information



| Parent Element                                         | Child Elements |
|--------------------------------------------------------|----------------|
| [enumeratedList](https://www.bing.com/search?q=enumeratedList) | none           |



 

## Attributes



| Attribute | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| minValue  | Public. Required. The minimum value in the range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| setValue  | Public. Optional. When a user selects this enumeration from a listbox property control, this discrete value is assigned as the property value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| text      | Public. Optional. The text used to display the enumerated value. The syntax allows for a direct display string or an indirect display string reference; use the indirect display string so that it can be localized.                                                                                                                                                                                                                                                                                                                                                                                                   |
| mnemonics | **Windows 7 and later.** Public. Optional. A list of mnemonic values that can be used to refer to the property in search queries. The list is delimited with the '\|' character.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| name      | Required. The canonical property name, unique to the system; for example, System.Rating. This attribute is limited to 64 characters. The name is case sensitive and should use the following syntax: Publisher.Application.PropertyName. The following methods return this value: [**IExplorerCommand::GetCanonicalName**](https://msdn.microsoft.com/c0f2fc66-98f5-404f-9d82-0290ed235ac0), [**IPropertyDescription::GetCanonicalName**](https://www.bing.com/search?q=**IPropertyDescription::GetCanonicalName**), [**IPropertyDescription2::GetCanonicalName**](/windows/desktop/api/Propsys/nn-propsys-ipropertydescription2), and [**IPropertyUI::GetCanonicalName**](https://www.bing.com/search?q=**IPropertyUI::GetCanonicalName**). |



 

 

 



