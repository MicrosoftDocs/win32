---
description: COM+ Services Without Components
ms.assetid: 5ef67411-334b-476e-b9b7-3677b24ab7df
title: COM+ Services Without Components
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Services Without Components

With COM+ 1.5, you can use the services provided by COM+ without needing to build a component to contain the methods that call those services. This greatly benefits developers who do not normally use components but want to use COM+ services such as transactions or the COM+ Tracker. By using COM+ services without components, developers can avoid the overhead of creating a component that is used to access only the COM+ services they need.

For example, script environments traditionally have been the largest consumers of COM+ services but they were never able to use those services efficiently because the services needed to be bundled within a COM+ component. This bundling requirement increased performance costs because of the increased communication and duplication of data necessary for the scripting environment to interact with the component. By using services without components, such costs are minimized.

The topics described in the following table provide background and task information about using COM+ services without components. This feature is intended for advanced Visual C++ developers who are concerned about performance.



| Topic                                                                                                 | Description                                                                                    |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [COM+ Services Without Components Concepts](com--services-without-components-concepts.md)<br/> | Provides an overview of using COM+ services without components.<br/>                     |
| [COM+ Services Without Components Tasks](com--services-without-components-tasks.md)<br/>       | Provides instructions for using COM+ to create and use services without components.<br/> |



 

 

 




