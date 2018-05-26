---
Description: Using an Object Constructor String to Construct a Component
ms.assetid: 57d66988-2a65-4309-957a-36a5972233b5
title: Using an Object Constructor String to Construct a Component
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using an Object Constructor String to Construct a Component

The following example illustrates how to programmatically retrieve and use an object constructor string when a component is instantiated. It shows an implementation of the [**IObjectConstruct**](/windows/win32/ComSvcs/nn-comsvcs-iobjectconstruct?branch=master) interface that retrieves an object constructor string. The string can then be parsed to set initial values or influence the behavior of the component.

## Visual Basic


```VB
Implements IObjectConstruct
Private Sub IObjectConstruct_Construct( ByVal pCtorObj As Object )
    Dim strConstructorString As String
    strConstructorString = pCtorObj.ConstructString
     Parse and use strConstructorString here. 
End Sub
```



## Related topics

<dl> <dt>

[COM+ Object Constructor Strings Concepts](com--object-constructor-strings-concepts.md)
</dt> <dt>

[Specifying an Object Constructor String for a Component](specifying-an-object-constructor-string-for-a-component.md)
</dt> </dl>

 

 



