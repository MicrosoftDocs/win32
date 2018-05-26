---
title: DISPID Constants
description: Identifies methods, properties, and arguments.
ms.assetid: 56037091-5761-40ad-8b25-72f85d41466f
keywords:
- DISPID data type
topic_type:
- apiref
api_name:
- DISPID_COLLECT
- DISPID_CONSTRUCTOR
- DISPID_DESTRUCTOR
- DISPID_EVALUATE
- DISPID_NEWENUM
- DISPID_PROPERTYPUT
- DISPID_UNKNOWN
- DISPID_VALUE
api_location:
- OaIdl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DISPID Constants

Identifies methods, properties, and arguments.



| Constant/value                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                             |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DISPID_COLLECT"></span><span id="dispid_collect"></span><dl> <dt>**DISPID\_COLLECT**</dt> <dt>-8</dt> </dl>             | The **Collect** property. You use this property if the method you are calling through Invoke is an accessor function. <br/>                                                                                                                                       |
| <span id="DISPID_CONSTRUCTOR"></span><span id="dispid_constructor"></span><dl> <dt>**DISPID\_CONSTRUCTOR**</dt> <dt>-6</dt> </dl> | The C++ constructor function for the object. <br/>                                                                                                                                                                                                                |
| <span id="DISPID_DESTRUCTOR"></span><span id="dispid_destructor"></span><dl> <dt>**DISPID\_DESTRUCTOR**</dt> <dt>-7</dt> </dl>    | The C++ destructor function for the object. <br/>                                                                                                                                                                                                                 |
| <span id="DISPID_EVALUATE"></span><span id="dispid_evaluate"></span><dl> <dt>**DISPID\_EVALUATE**</dt> <dt>-5</dt> </dl>          | The Evaluate method. This method is implicitly invoked when the ActiveX client encloses the arguments in square brackets. For example, the following two lines are equivalent: <br/> x.\[A1:C1\].value = 10<br/> x.Evaluate("A1:C1").value = 10 <br/> |
| <span id="DISPID_NEWENUM"></span><span id="dispid_newenum"></span><dl> <dt>**DISPID\_NEWENUM**</dt> <dt>-4</dt> </dl>             | The **\_NewEnum** property. This special, restricted property is required for collection objects. It returns an enumerator object that supports [**IEnumVARIANT**](/windows/previous-versions/oaidl/nn-oaidl-ienumvariant?branch=master), and should have the **restricted** attribute specified.<br/>                |
| <span id="DISPID_PROPERTYPUT"></span><span id="dispid_propertyput"></span><dl> <dt>**DISPID\_PROPERTYPUT**</dt> <dt>-3</dt> </dl> | The parameter that receives the value of an assignment in a PROPERTYPUT. <br/>                                                                                                                                                                                    |
| <span id="DISPID_UNKNOWN"></span><span id="dispid_unknown"></span><dl> <dt>**DISPID\_UNKNOWN**</dt> <dt>-1</dt> </dl>             | The value returned by [**IDispatch::GetIDsOfNames**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-getidsofnames?branch=master) to indicate that a member or parameter name was not found. <br/>                                                                                                                |
| <span id="DISPID_VALUE"></span><span id="dispid_value"></span><dl> <dt>**DISPID\_VALUE**</dt> <dt>0</dt> </dl>                    | The default member for the object. This property or method is invoked when an ActiveX client specifies the object name without a property or method. <br/>                                                                                                        |



## Remarks

Use these values with the DISPID type. The DISPID type is defined as follows.

``` syntax
typedef LONG DISPID;
```

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>OaIdl.h</dt> </dl> |



 

 





