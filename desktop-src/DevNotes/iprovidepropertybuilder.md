---
description: The IProvidePropertyBuilder interface, when implemented, allows objects to specify property builder objects for properties.
ms.assetid: 26557622-4a97-4db0-85ed-3f77fcb769a0
title: IProvidePropertyBuilder interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IProvidePropertyBuilder:IUnknown
api_type: 
- COM
api_location: 
- Vsp.dll
---

# IProvidePropertyBuilder interface

The **IProvidePropertyBuilder** interface, when implemented, allows objects to specify property builder objects for properties. Builders are invoked by an ellipsis button (\[...\]) on the Microsoft Visual Studio property browser and is invoked through [**ExecuteBuilder**](iprovidepropertybuilder-executebuilder.md) when the button is pressed. To supply a builder for a given property, return a GUID for the property builder that should be invoked for the current property from [**MapPropertyToBuilder**](iprovidepropertybuilder-mappropertytobuilder.md). Builders are generally implemented through modal dialog boxes.

The version for this interface is 1.0. Method calls are received at a dynamically assigned endpoint (as described in the MSMQ binary documentation on endpoint mapping) and use the UUID (universally unique identifier) "33C0C1D8-33CF-11d3-BFF2-00C04F990235".

## Members

The **IProvidePropertyBuilder:IUnknown** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IProvidePropertyBuilder** also has these types of members:

-   [Methods](#methods)

### Methods

The **IProvidePropertyBuilder:IUnknown** interface has these methods.



| Method                                                                       | Description                                                                                  |
|:-----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**ExecuteBuilder**](iprovidepropertybuilder-executebuilder.md)             | Notifies an object that it should display its builder for the specified property.<br/> |
| [**MapPropertyToBuilder**](iprovidepropertybuilder-mappropertytobuilder.md) | Checks whether a builder should be associated with a particular property.<br/>         |



 

## Requirements



| Requirement | Value |
|----------------|------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Vsp.dll</dt> </dl> |



 

 
