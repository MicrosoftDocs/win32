---
description: The GetFlags method retrieves the context flags associated with the deferred command.
ms.assetid: 3a96299a-b157-419b-a23e-86241e10566f
title: CDeferredCommand.GetFlags method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDeferredCommand.GetFlags
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDeferredCommand.GetFlags method

The `GetFlags` method retrieves the context flags associated with the deferred command.

## Syntax


```C++
short GetFlags();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the following:



| Return code                                                                                             | Description                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DISPATCH\_METHOD**</dt> </dl>         | Run the member as a method. If a property has the same name, both this and the DISPATCH\_PROPERTYGET flag can be set.<br/>                                               |
| <dl> <dt>**DISPATCH\_PROPERTYGET**</dt> </dl>    | The member is being retrieved as a property or data member.<br/>                                                                                                         |
| <dl> <dt>**DISPATCH\_PROPERTYPUT**</dt> </dl>    | The member is being changed as a property or data member.<br/>                                                                                                           |
| <dl> <dt>**DISPATCH\_PROPERTYPUTREF**</dt> </dl> | The member is being changed via a reference assignment, rather than a value assignment. This flag is valid only when the property accepts a reference to an object.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




