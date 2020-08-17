---
title: Realms Processing and Attribute Manipulation
description: Realms processing, which is also known as attribute manipulation, refers to transforming the name of the user requesting access.
ms.assetid: 52963eda-ea95-4307-8924-d4143bc1f53d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Realms Processing and Attribute Manipulation

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

Realms processing, which is also known as attribute manipulation, refers to transforming the name of the user requesting access. The calling-station ID and called-station ID can also be manipulated. The realms-processing rules are part of the Proxy profile attributes collection.

For each manipulation, you need to create two [Manipulation-Rule](/windows/desktop/Nps/sdo-manipulation-rule) attributes. Each of these attributes is a string value. The first rule contains a regular expression representing the pattern to match. The second rule contains a regular expression representing the replacement text. You must also create a [Manipulation-Target](/windows/desktop/Nps/sdo-manipulation-target) attribute. This attribute is an enumeration that specifies which part of the user's information to manipulate.

The order in which the attributes are created is important. NPS processes the attributes in the order in which they were created.

The following table shows an example of a set of manipulation attributes.



| Name                 | Type         | String Value     |
|----------------------|--------------|------------------|
| msManipulationRule   | **VT\_BSTR** | "@company.com"   |
| msManipulationRule   | **VT\_BSTR** | "@microsoft.com" |
| msManipulationRule   | **VT\_BSTR** | "^.+@"           |
| msManipulationRule   | **VT\_BSTR** | "guest@"         |
| msManipulationTarget | **VT\_I4**   | "1"              |



 

## Related topics

<dl> <dt>

[Object Model Hierarchy](/windows/desktop/Nps/sdo-object-model-hierarchy)
</dt> <dt>

[SDO Supported Attributes](/windows/desktop/Nps/sdo-sdo-supported-attributes)
</dt> <dt>

[Creating a Connection Request Policy](/windows/desktop/Nps/sdo-creating-a-connection-request-policy)
</dt> <dt>

[**ISdoCollection**](/windows/desktop/api/sdoias/nn-sdoias-isdocollection)
</dt> <dt>

[**ISdoDictionaryOld**](/windows/desktop/api/sdoias/nn-sdoias-isdodictionaryold)
</dt> <dt>

[**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties)
</dt> </dl>

 

 