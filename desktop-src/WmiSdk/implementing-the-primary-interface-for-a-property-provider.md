---
description: A property provider uses the IWbemPropertyProvider methods as the primary interface to WMI. With IWbemPropertyProvider, you can implement the code to retrieve and modify class and instance properties.
ms.assetid: d08c2ca4-9f8a-4a27-80fc-688d7c56f5eb
ms.tgt_platform: multiple
title: Implementing the Primary Interface for a Property Provider
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Primary Interface for a Property Provider

A property provider uses the [**IWbemPropertyProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbempropertyprovider) methods as the primary interface to WMI. With **IWbemPropertyProvider**, you can implement the code to retrieve and modify class and instance properties.

The following table lists the [**IWbemPropertyProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbempropertyprovider) methods that you can implement for a property provider.



| Method                                                   | Feature      |
|----------------------------------------------------------|--------------|
| [**GetProperty**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbempropertyprovider-getproperty) | Retrieval    |
| [**PutProperty**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbempropertyprovider-putproperty) | Modification |



 

> [!Note]  
> You must implement a property provider as an in-process provider. WMI will initialize property providers written as services or executable files but will never call their [**GetProperty**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbempropertyprovider-getproperty) and [**PutProperty**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbempropertyprovider-putproperty) methods.

 

If you choose not to support one of these methods, your provider can supply a stub implementation that returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE**.

A property provider identifies a managed class or instance by a set of three qualifiers: **PropertyContext**, **InstanceContext**, and **ClassContext**. WMI will pass in string constants describing these three qualifiers to your property provider.

Your property provider must be prepared to handle the following types of context qualifiers:

-   The **InstanceContext** qualifier is attached to an instance and contains information that applies to every property in the instance.
-   The **ClassContext** qualifier is attached to a class and contains information that applies to every instance in the class. For example, in a class used to store data supplied by the Registry provider, **ClassContext** can be the path to the registry key that contains the properties to be reported.
-   The **PropertyContext** qualifier specifies context-specific information that pertains to the property. For example, in a class used to store data supplied by the Registry provider, **PropertyContext** specifies the name of the registry value to be stored by the property.

These qualifiers can work together. You can designate both an **InstanceContext** and **PropertyContext** value to tell the provider how to treat particular types of instances. For example, you might want to mark instances the provider will recognize as readable but having only one writeable property.

The most common qualifier used is **PropertyContext**. Therefore, WMI provides the **DynProps** qualifier as a shortcut. WMI considers each property in an instance marked with **DynProps** to also have the **Dynamic**, [**Provider**](/windows/desktop/api/Provider/nl-provider-provider), and **PropertyContext** qualifiers.

 

 



