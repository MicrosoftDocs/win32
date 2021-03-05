---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 8169b74f-13e0-4f6b-81e2-1824d932ee50
title: Important Property Instances
ms.topic: article
ms.date: 05/31/2018
---

# Important Property Instances

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

In order for a PrintCapabilities client to be able to construct a reasonable PrintTicket, the PrintCapabilities document must provide certain properties of Feature instances as well as Option instances within the Feature. A generic user interface (UI) module requires such information to construct a UI. This in turn requires that the Print Schema Keywords define a few Property instances that appear as children of Feature and Option elements.

Feature elements can contain the following Property.



| Property                  | Values                                 | Purpose                                                                                                                                                                                                                                                                                                       |
|---------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SelectionType <br/> | PickOne<br/> PickMany<br/> | Specifies the number of Options that can be selected for this Feature at a given time, either one (PickOne), or more than one (PickMany). The client can use this information to construct a PrintTicket. This information affects UI behavior, as well as PrintTicket validation by the provider.<br/> |



 

Option elements can contain the following Property.



| Property                   | Values                           | Purpose                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IdentityOption <br/> | True<br/> False<br/> | Selecting the IdentityOption Property is interpreted to mean "disable this feature". A Feature that contains a SelectionType Property whose value is PickMany must also contain an Option that has an IdentityOption Property. The UI code (or client constructing a PrintTicket) must deselect any other Option if the IdentityOption Property is selected.<br/> |



 

Feature, Option, and ParameterDef elements can contain the following Property.



| Property              | Values                          | Purpose                                                                                                                                                                                                                                                                                                                                     |
|-----------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DisplayUI <br/> | Show<br/> Hide<br/> | Specifies whether the parent element should be displayed in the UI. Show indicates that the element should be displayed in the UI. Hide indicates that the element should not be displayed in the UI. If this Property is not defined for an element, the default interpretation is Show, meaning that the element is displayed.<br/> |



 

Feature, Option, and ParameterDef elements can contain the following Property.



| Property                | Value             | Purpose                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DisplayName <br/> | String<br/> | Specifies the display string for the parent element, overriding the default display name. Can be used by PrintCapabilities providers to present a localized and user friendly display name. The default display name value is the name attribute for the parent element. <br/> In the case of Option elements, if the name attribute is not provided, then the DisplayName Property must be present.<br/> |



 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




