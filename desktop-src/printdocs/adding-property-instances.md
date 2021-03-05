---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: dac287a9-77ca-44d8-8019-b05e4c61dc52
title: Adding Property Instances
ms.topic: article
ms.date: 05/31/2018
---

# Adding Property Instances

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The Print Schema allows Property instances to be present in an Option instance. The Property instances defined in the PrintCapabilities document are not propagated to the Option instances saved in the PrintTicket. Property elements do not affect the result of the scoring process when two Option instances are compared, but ScoredProperty instances do affect this process. All device drivers that implement a scoring algorithm should observe this convention. PrintCapabilities providers are permitted to add Property instances to an Option if these instances are specific to that particular Option and no others, or if the provider intends for the value of this Property to appear for every Option in the Feature. For example, suppose that the PrintRate Property is dependent on the Option selected for the PageResolution Feature. If the PrintRate Property were placed at the root level of the PrintCapabilities document, it would be single-valued and would reflect only the print rate for the currently selected resolution. However, if the PrintRate Property were placed within each PageResolution Option, each instance of the PrintRate Property could reflect the print rate for the PageResolution Option that contained it. The PrintCapabilities document would contain multiple definitions for PrintRate, one corresponding to each PageResolution Option. Using a shorthand representation, the PrintCapabilities would contain:

``` syntax
<psf:Feature name="psk:PageResolution">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option>
    <psf:ScoredProperty name="psk:ResolutionX">
      <psf:Value xsi:type="xs:string">800dpi</psf:Value>
    </psf:ScoredProperty>
    <psf:ScoredProperty name="psk:ResolutionY">
      <psf:Value xsi:type="xs:string">600dpi</psf:Value>
    </psf:ScoredProperty>
    <!-- Note: The following Property is not part of the Print Schema Framework -->
    <!-- It is included for illustration purposes. -->
    <!-- It is shown as a privately defined implementation-->
    <Property name="FabrikamES500:PrintRate">
      <Value xsi:type="string">20ppm</Value>
    </psf:Property>
  </psf:Option>
</psf:Feature>
```

In some situations, placing a print rate Property within each resolution Option is more convenient for the client, because the client can determine at a glance the effect that each resolution Option has on the print rate, without the need for obtaining a new PrintCapabilities document for each resolution setting.

Note also that Property instances can also be added as child elements of Feature elements. This is useful if there are Property instances or values of Property instances that are specific to each Feature. For example, there might be a Property that specifies whether only one Option is permitted to be selected at one time for a Feature, or whether multiple Options may be selected. This is the PICK\_ONE, PICK\_MANY property used in PPD and GPD files. Because some Feature instances might be identified as PICK\_ONE, while others might be identified as PICK\_MANY, this Property must be defined for each Feature. Locating the Property as a child element of the Feature produces the association between the Property and the Feature.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



