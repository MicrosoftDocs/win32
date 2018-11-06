---
title: Classifying Components
description: Classifying Components
ms.assetid: 4d805532-96c9-400d-b78a-f8d0d9bdbf83
ms.topic: article
ms.date: 05/31/2018
---

# Classifying Components

While a client is able to browse through the list of CLSIDs in the registry and select a component to use, loading each component in the registry and querying it for its supported interfaces is very time-consuming. To determine whether a component supports the interfaces required before creating an instance of the component, a method to classify components into categories was developed.

A component category is a set of interfaces that have been assigned a GUID named CATID. Components that implement all of the interfaces in a component category register themselves as members of that component category. Components that belong to a certain component category can then be selected from the registry. By registering itself as a member of a component category, the component is guaranteeing that it supports all of the member interfaces in the component category.

A component can be a member of many categories. It is not limited to supporting interfaces in a component category. It can support any interface, in addition to those in a component category.

In contrast to the standard registration of components, in which developers must write code that manually registers objects, component categories automates much of this work. The six methods of the [**ICatRegister**](/windows/desktop/api/ComCat/nn-comcat-icatregister) interface define component categories and register objects that implement or require them. The [Component Categories Manager](the-component-categories-manager.md) object implements this interface. See **ICatRegister** and [**ICatInformation**](/windows/desktop/api/ComCat/nn-comcat-icatinformation) for additional information on using component categories.

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 




