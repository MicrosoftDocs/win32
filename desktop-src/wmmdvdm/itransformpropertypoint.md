---
title: ITransformPropertyPoint interface
description: The ITransformPropertyPoint interface specifies a property value at a specific point. To create a property point programmatically, call ITransformProperty AddPoint.
ms.assetid: a99673c2-61cf-4cf7-bfb6-4b9ce8ea5431
keywords:
- ITransformPropertyPoint interface Windows Movie Maker and DVD Maker
- ITransformPropertyPoint interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- ITransformPropertyPoint
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ITransformPropertyPoint interface

The **ITransformPropertyPoint** interface specifies a property value at a specific point. To create a property point programmatically, call [**ITransformProperty::AddPoint**](itransformproperty-addpoint.md).

## Members

The **ITransformPropertyPoint** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITransformPropertyPoint** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITransformPropertyPoint** interface has these methods.



| Method                                                  | Description                                                        |
|:--------------------------------------------------------|:-------------------------------------------------------------------|
| [**get\_Time**](itransformpropertypoint-get-time.md)   | Retrieves the time associated with this property point.<br/> |
| [**get\_Value**](itransformpropertypoint-get-value.md) | Retrieves the value associated with a property point.<br/>   |
| [**put\_Time**](itransformpropertypoint-put-time.md)   | Assigns a time to a property point.<br/>                     |
| [**put\_Value**](itransformpropertypoint-put-value.md) | Assigns a value to a property point.<br/>                    |



 

## See also

<dl> <dt>

[**Property Management Interfaces**](property-management-interfaces.md)
</dt> </dl>

 

 





