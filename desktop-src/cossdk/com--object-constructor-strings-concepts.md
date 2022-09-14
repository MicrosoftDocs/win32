---
description: COM+ object constructor strings are initialization strings that are administratively specified for a component.
ms.assetid: b4915dae-c97c-4d36-95ee-bb10dcb40845
title: COM+ Object Constructor Strings Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Object Constructor Strings Concepts

COM+ object constructor strings are initialization strings that are administratively specified for a component. You can use object constructor strings to write a single component with a degree of generality that allows it to be later customized for a particular task; that is, you can perform parameterized object construction.

For example, you might use this feature to write a component that holds a generic ODBC connection and later specify an exact DSN for the component administratively. If the system configuration changes, you can change the constructor string accordingly.

> [!Note]  
> Object constructor strings should not be used to store security-sensitive information.

 

You can use object constructor strings in conjunction with [object pooling](com--object-pooling.md) to achieve a greater degree of granularity in how you pool and reuse resources. For example, you might create several distinct components, identical except for constructor strings and CLSIDs, to maintain distinct pools of objects holding connections usable by distinct groups of clients. This would be useful if connections are opened in a manner that binds them to particular security roles—such as when the connections are opened with some specific authentication at the database—rendering them non-reusable in the general case.

To do this, you can write a single generic component that relies on object constructor strings, using [**IObjectConstruct**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectconstruct), and recompile it to produce several customizable components each with a distinct CLSID. You can then administratively tailor each component to open an appropriate connection with a constructor string, configure them to be pooled, and they will be maintained in distinct pools per CLSID.

You can specify a constructor string when a component has been written specifically to recognize the string that you enter. Components can access these strings programmatically by using [**IObjectConstruct**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectconstruct).

Constructor strings are passed in at object creation time only when object construction is administratively enabled. COM+ calls the [**IObjectConstruct::Construct**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectconstruct-construct) method that it implements. Within that method, you can access the constructor string by using [**IObjectConstructString**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectconstructstring). Empty strings can be valid entries.

## Related topics

<dl> <dt>

[COM+ Object Pooling](com--object-pooling.md)
</dt> <dt>

[Specifying an Object Constructor String for a Component](specifying-an-object-constructor-string-for-a-component.md)
</dt> <dt>

[Using an Object Constructor String to Construct a Component](using-an-object-constructor-string-to-construct-a-component.md)
</dt> </dl>

 

 



