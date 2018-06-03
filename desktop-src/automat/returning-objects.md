---
title: Returning Objects
description: To return an object from a property or method, the application should return a pointer to the object's implementation of the IDispatch interface.
ms.assetid: 13ffb02a-e702-4f02-aba1-b77efa9cc3b4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Returning Objects

To return an object from a property or method, the application should return a pointer to the object's implementation of the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface. The data type of the return value should be VT\_DISPATCH, or if the object does not support [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch), VT\_UNKNOWN. The .odl file for the object should specify the name of the interface, rather than **IDispatch**\*, as follows:


```C++
ICustom * MyMember(...) {...};
```



The example declares a member that returns a pointer to a custom interface named **ICustom**.

 

 




