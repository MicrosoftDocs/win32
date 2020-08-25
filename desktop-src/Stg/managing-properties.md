---
title: Managing Properties
description: Every property consists of a property identifier (unique within its property set), a variant type (VT or VarType) tag that represents the type of a value, and the value itself.
ms.assetid: d220ecb4-b014-4ac9-a636-9a493187cc87
keywords:
- Structured Storage Strctd Stg ,using,managing properties
ms.topic: article
ms.date: 05/31/2018
---

# Managing Properties

Every property consists of a *property identifier* (unique within its property set), a *variant type (VT or VarType) tag* that represents the type of a value, and the *value* itself. The variant type tag describes the representation of the data in the value. In addition, a property may also be assigned a *string name* that can be used to identify the property, rather than using the required numerical property identifier (ID). To create and manage properties, COM defines the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface.

The [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface includes methods to read and write arrays of either properties or property names. The interface includes [**Commit**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-commit) and [**Revert**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-revert) methods that are similar to [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) methods of the same name. There are utility methods that allow you to set the class identifier (CLSID) of the property set, set the times associated with the set, and get statistics about the property set. Finally, the [**Enum**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-enum) method creates an enumerator and returns a pointer to its [**IEnumSTATPROPSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) interface. You can call the methods of this interface to enumerate [**STATPROPSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) structures on your object, which will provide information about all of the properties in the current property set.

The following is an example of how properties are represented. If a specific property in a property set holds an animal's scientific name, that name could be stored as a zero-terminated string. Stored along with the name would be a type indicator to indicate that the value is a zero-terminated string. These properties might have the following characteristics:



| Property ID | String identifier | Type indicator | Value represented              |
|-------------|-------------------|----------------|--------------------------------|
| 02          | PID\_ANIMALNAME   | VT\_LPWSTR     | Zero-terminated Unicode string |
| 03          | PID\_LEGCOUNT     | VT\_I2         | WORD                           |



 

Any application that recognizes the property set format—identifying it through its format identifier (FMTID)—can look at the property with an identifier of PID\_ANIMALNAME, determine that it is a zero-terminated string, and read and write the value. Although the application can call [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple) to read any or all of a property set (having first obtained a pointer), the application must know how to interpret the property set.

A property value is passed through property interfaces as an instance of the type [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

It is important to distinguish between these stored (persistent) properties, and run-time properties. Variant-type value constants have names beginning with VT\_. The set of valid PROPVARIANTs is, however, not entirely equivalent to the set of VARIANTs used in Automation and ActiveX controls.

The only difference between the two structures is the allowable set of VT\_ (Variant Type / VarType) tags in each. Where a certain property type can be used in both a VARIANT and a PROPVARIANT, the type tag (the VT\_ value) always has an identical value. Further, for a given VT\_ value, the in-memory representation used in VARIANTs and PROPVARIANTs is identical. Taken all together, this approach allows the type system to catch disallowed type tags, while at the same time allowing a knowledgeable client to implement a pointer cast when appropriate.

For more information, see the following section, [Property Storage Considerations](property-storage-considerations.md).

 

 