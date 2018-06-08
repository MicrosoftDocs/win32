---
title: Programming Considerations
description: When developing applications that use the Task Scheduler 1.0, keep the following programming issues in mind.Your application must ensure the Task Scheduler service is running before attempting to make any calls using the Task Scheduler API.When retrieving strings, make sure that you call CoTaskMemFree to release each string after it is no longer needed. When retrieving arrays of strings, make sure you first release each string in the array and then release the array itself.When creating or modifying a work item, including triggers associated with a work item, make sure you call IPersistFile Save to save the work item to disk.After using any of the interfaces that are provided by the Task Scheduler API, make sure you call IUnknown Release to release the interface. IUnknown is supported by each Task Scheduler object.
ms.assetid: b9e1806c-acfa-4d44-a371-91bad788648c
keywords:
- starting Task Scheduler
- programming considerations Task Scheduler
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Programming Considerations

When developing applications that use the Task Scheduler 1.0, keep the following programming issues in mind.

-   Your application must ensure the Task Scheduler service is running before attempting to make any calls using the Task Scheduler API.
-   When retrieving strings, make sure that you call [**CoTaskMemFree**](https://msdn.microsoft.com/windows/desktop/3d0af12e-fc74-4ef7-b2dd-e9da5d0483c7) to release each string after it is no longer needed. When retrieving arrays of strings, make sure you first release each string in the array and then release the array itself.
-   When creating or modifying a work item, including triggers associated with a work item, make sure you call [**IPersistFile::Save**](https://msdn.microsoft.com/windows/desktop/da9581e8-98c7-4592-8ee1-a1bc8232635b) to save the work item to disk.
-   After using any of the interfaces that are provided by the Task Scheduler API, make sure you call [**IUnknown::Release**](https://msdn.microsoft.com/windows/desktop/4b494c6f-f0ee-4c35-ae45-ed956f40dc7a) to release the interface. [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) is supported by each Task Scheduler object.

The Using section of the Task Scheduler documentation provides numerous examples that follow these guidelines. The table below provides jumps to some of these examples.

| For an example of         | See                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------|
| Releasing strings         | [Retrieving Work Item Property Examples](retrieving-work-item-property-examples.md)       |
| Saving work items to disk | [Setting Work Item Property Examples](setting-work-item-property-examples.md)             |
| Releasing interfaces      | [Creating a Task Using NewWorkItem Example](creating-a-task-using-newworkitem-example.md) |



 

 

 




