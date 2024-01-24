---
title: Return Values (Windows Accessibility features)
description: This topic describes the most common return values, and other return values that you might see less frequently.
ms.assetid: 'e6deca92-42da-41ab-bfdb-75cbce3022bb'
ms.topic: article
ms.date: 05/31/2018
---

# Return Values (Windows Accessibility features)

This topic describes the most common return values, and other return values that you might see less frequently.

## Common Return Values

The [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods return one of the following values, defined in winerror.h, or another standard Component Object Model (COM) error code:



|   Value                      |   Description                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S\_OK                   | The method succeeded.                                                                                                                                                                                                                                                                                                                                                                     |
| S\_FALSE                | The method succeeded in part. This happens when the method succeeds, but the requested information is not available. For example, Microsoft Active Accessibility returns S\_FALSE if you call [**IAccessible::accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest) to retrieve a child object at a given point, and the specified point is not within the object or the object's child. |
| DISP\_E\_MEMBERNOTFOUND | The object does not support the requested property or action. For example, a push button returns this value if you request its [Value property](value-property.md), because it does not have a Value property.                                                                                                                                                                           |
| E\_NOTIMPL              | The method is not implemented. This value occurs when a client calls a method that is not yet supported in that operating system.                                                                                                                                                                                                                                                         |
| E\_INVALIDARG           | One or more arguments were not valid. This error occurs when the caller attempts to identify a child object using an identifier that the server does not recognize. This error also results when a client attempts to identify a child object within an object that has no children.                                                                                                      |
| E\_OUTOFMEMORY          | The method was unable to allocate memory required to complete an operation crucial to its success.                                                                                                                                                                                                                                                                                        |
| E\_FAIL                 | An unknown or generic error occurred.                                                                                                                                                                                                                                                                                                                                                     |



 

## Additional Return Values

The following are return values that [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods might return. These return values are not as common as the previous ones, but you should be aware of them.



|    Value                    |    Description                                                                                  |
|------------------------|--------------------------------------------------------------------------------------|
| E\_ACCESSDENIED        | This is returned when you call get\_accValue to get the value of a password control. |
| DISP\_E\_EXCEPTION     |                                                                                      |
| CO\_E\_OBJNOTCONNECTED |                                                                                      |



 

 

 




