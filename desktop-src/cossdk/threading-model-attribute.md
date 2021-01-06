---
description: COM+ manages threads for you. Every COM component has a ThreadingModel property that you can specify when you develop the component. This property determines how the components objects are assigned to threads for method execution.
ms.assetid: 5fae8475-3d2e-4939-80a7-bc9a677a50b3
title: Threading Model Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Threading Model Attribute

COM+ manages threads for you. Every COM component has a **ThreadingModel** property that you can specify when you develop the component. This property determines how the component's objects are assigned to threads for method execution.

You can use the Component Services administrative tool to view the threading-model property by right-clicking a component in the **Components** folder, clicking **Properties**, and then clicking the **Concurrency** tab. Under **Threading Model**, the possible values are as follows:

-   **Main Thread Apartment**
-   **Single Thread Apartment**
-   **Free Thread Apartment**
-   **Neutral Apartment**
-   **Any Apartment**

The preferred threading model for COM+ is the [neutral apartment](neutral-apartments.md). However, if you do not specify a threading model for your component, COM+ uses the main thread apartment, which is the default.

> [!Note]  
> For more detailed information, see [Choosing the Threading Model](/windows/desktop/com/choosing-the-threading-model).

 

The following table shows the programming model for apartments in COM+.



| Model                     | Apartment                                                 | Free                               | Both                               | Neutral                      | Not Specified                      |
|---------------------------|-----------------------------------------------------------|------------------------------------|------------------------------------|------------------------------|------------------------------------|
| Single-threaded, not main | Created in current apartment                              | Created in multithreaded apartment | Created in current apartment       | Created in neutral apartment | Created in main threaded apartment |
| Single-threaded, main     | Created in current apartment                              | Created in multithreaded apartment | Created in current apartment       | Created in neutral apartment | Created in current apartment       |
| Multithreaded             | Created in host single-threaded apartment                 | Created in multithreaded apartment | Created in multithreaded apartment | Created in neutral apartment | Created in main threaded apartment |
| Neutral (on STA thread)   | Created in host single-threaded apartment for this thread | Created in multithreaded apartment | Created in neutral apartment       | Created in neutral apartment | Created in main threaded apartment |
| Neutral (on MTA thread)   | Created in host single-threaded apartment                 | Created in multithreaded apartment | Created in neutral apartment       | Created in neutral apartment | Created in main threaded apartment |



 

## Related topics

<dl> <dt>

[**ThreadingModel**](components.md)
</dt> </dl>

 

 
