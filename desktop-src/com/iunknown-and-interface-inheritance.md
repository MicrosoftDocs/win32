---
title: IUnknown and Interface Inheritance
description: IUnknown and Interface Inheritance
ms.assetid: c45f0947-6020-4aa1-9250-561603a46a68
ms.topic: article
ms.date: 05/31/2018
---

# IUnknown and Interface Inheritance

Inheritance in COM does not mean code reuse. Because no implementations are associated with interfaces, interface inheritance does not mean code inheritance. It means only that the contract associated with an interface is inherited in a C++ pure-virtual base-class fashion and modified — either by adding new methods or by further qualifying the allowed usage of methods. There is no selective inheritance in COM. If one interface inherits from another, it includes all the methods that the other interface defines.

Inheritance is used sparingly in the predefined COM interfaces. All predefined interfaces (and any custom interfaces you define) inherit their definitions from the important interface [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown), which contains three vital methods: [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)), [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref), and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release). All COM objects must implement the **IUnknown** interface because it provides the means, using **QueryInterface**, to move freely between the different interfaces that an object supports as well as the means to manage its lifetime by using **AddRef** and **Release**.

In creating an object that supports [aggregation](aggregation.md), you would need to implement one set of [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) functions for all interfaces as well as a stand-alone **IUnknown** interface. In any case, any object implementor will implement **IUnknown** methods. See the section [Using and Implementing IUnknown](using-and-implementing-iunknown.md) for more information.

While there are a few interfaces that inherit their definitions from a second interface in addition to [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown), the majority simply inherit the **IUnknown** interface methods. This makes most interfaces relatively compact and easy to encapsulate.

## Related topics

<dl> <dt>

[COM Objects and Interfaces](com-objects-and-interfaces.md)
</dt> </dl>

 

 