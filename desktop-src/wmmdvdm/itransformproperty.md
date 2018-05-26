---
title: ITransformProperty interface
description: The ITransformProperty interface describes an effect or transition property.
ms.assetid: d82d8782-b5ef-43d4-b037-1e3c173454d3
keywords:
- ITransformProperty interface Windows Movie Maker and DVD Maker
- ITransformProperty interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- ITransformProperty
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITransformProperty interface

The **ITransformProperty** interface describes an effect or transition property. It wraps a **param** XML element (or equivalent custom parameter element) in the XML initialization file. To add a new property to the collection, call [**ITransformPropertiesConfig::CreateProperty**](itransformpropertiesconfig-createproperty.md).

To examine any child properties, you can query this interface for [**ITransformProperties**](itransformproperties.md). If the property has no children, the retrieved interface will report no elements.

## Members

The **ITransformProperty** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITransformProperty** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITransformProperty** interface has these methods.



| Method                                                                       | Description                                                                                                                            |
|:-----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**AddPoint**](itransformproperty-addpoint.md)                              | Adds a data point to the property.<br/>                                                                                          |
| [**CalcValueAtTime**](itransformproperty-calcvalueattime.md)                | Calculates the property value at a particular time, using the evaluation function type that was specified for the property.<br/> |
| [**Clone**](itransformproperty-clone.md)                                    | Creates a duplicate **ITransformProperty** interface.<br/>                                                                       |
| [**get\_EvaluationFunction**](itransformproperty-get-evaluationfunction.md) | Retrieves the evaluation function used for a transform.<br/>                                                                     |
| [**get\_Name**](itransformproperty-get-name.md)                             | Retrieves the name of a property.<br/>                                                                                           |
| [**get\_Point**](itransformproperty-get-point.md)                           | Retrieves a point by index.<br/>                                                                                                 |
| [**get\_PointCount**](itransformproperty-get-pointcount.md)                 | Retrieves a count of time points in the current property.<br/>                                                                   |
| [**get\_Type**](itransformproperty-get-type.md)                             | Retrieves the data type of the property value, as a **VARTYPE**.<br/>                                                            |
| [**put\_EvaluationFunction**](itransformproperty-put-evaluationfunction.md) | Specifies the evaluation function that is used to calculate intermediary data between property points.<br/>                      |
| [**SetValueAtTime**](itransformproperty-setvalueattime.md)                  | Specifies a property value at a particular time.<br/>                                                                            |



 

## See also

<dl> <dt>

[**Property Management Interfaces**](property-management-interfaces.md)
</dt> </dl>

 

 





