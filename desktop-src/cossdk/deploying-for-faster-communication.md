---
description: Deploying for Faster Communication
ms.assetid: 9099f9df-b620-4623-826e-c541202ebc4a
title: Deploying for Faster Communication
ms.topic: article
ms.date: 05/31/2018
---

# Deploying for Faster Communication

Performance is a key consideration when deploying a COM+ application, and component location is the key to getting the best performance from a well-designed application.

It was once widely held that with scalable application architectures, performance could be addressed by simply moving primary components of the application to faster hardware. This has proven not to be true. Performance problems arise not from individual component performance but from the links connecting components.

The primary factor for success is location. Proximity or physical location, time, capacity, and purpose are distinct aspects of location that apply to the deployment of a COM+ application, all of which affect performance.

The best performance comes when the application components and resources are designed and deployed to match the demands placed upon them by the application workload.

In general, you should deploy components to minimize cross-process, and especially cross-computer, communication between components. If your application design is efficient, classes within a component are grouped by use and function to maximize communications within components. In deploying components, you need to ensure that the components are logically located to make use of the relationships between the components and to reduce the amount of messaging between components.

## Related topics

<dl> <dt>

[Designing for Deployment](designing-for-deployment.md)
</dt> </dl>

 

 



