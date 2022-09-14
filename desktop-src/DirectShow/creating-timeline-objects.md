---
description: Creating Timeline Objects
ms.assetid: fb369b32-a54b-4d8a-8358-5f05aa48f853
title: Creating Timeline Objects
ms.topic: article
ms.date: 05/31/2018
---

# Creating Timeline Objects

\[This API is not supported and may be altered or unavailable in the future.\]

The sample code presented in this article starts with an empty timeline, but the same steps apply if you load an existing project and want to add objects to it.

To create any type of object in the timeline, call the [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) method. For example, the following code creates a new group:


```C++
IAMTimelineObj *pGroupObj = NULL;
pTL->CreateEmptyNode(&pGroupObj, TIMELINE_MAJOR_TYPE_GROUP);
```



The second parameter is a member of the [**TIMELINE\_MAJOR\_TYPE**](timeline-major-type.md) enumeration. It specifies the type of timeline object to create, such as a group or a track.

The **CreateEmptyNode** method creates the object and returns a pointer to the object's [**IAMTimelineObj**](iamtimelineobj.md) interface. It also increments the reference count on the **IAMTimelineObj** interface, so you must release the interface when you finish using it. Do not call the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function. Instead, always use **CreateEmptyNode** to create a timeline object, because it initializes the new object for use in a timeline.

The [**IAMTimelineObj**](iamtimelineobj.md) interface is a generic interface. It provides methods that are common to all types of timeline object. Each type of object exposes other interfaces as well. For example, groups expose the [**IAMTimelineGroup**](iamtimelinegroup.md) interface, among others. You can obtain pointers to the other interfaces by calling **QueryInterface**.

After you create an object, it is not yet a part of the timeline. The method to add an object to the timeline depends on the object type. The following section describes how to add groups, compositions, and tracks to the timeline.

## Related topics

<dl> <dt>

[Constructing a Timeline](constructing-a-timeline.md)
</dt> </dl>

 

 
