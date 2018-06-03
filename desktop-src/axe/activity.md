---
title: Activity element
description: This element holds information about a category of related issues.
ms.assetid: FF717CB0-A544-488D-B6E6-FA2D8105ED4B
keywords:
- Activity element Access Execution Engine
topic_type:
- apiref
api_name:
- Activity
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Activity element

This element holds information about a category of related issues.

## Usage

``` syntax
<Activity
  ID = "ID"
  parentID = "IDREF">
  child elements
</Activity>
```

## Attributes



| Attribute               | Type             | Required      | Description                                                                                                              |
|-------------------------|------------------|---------------|--------------------------------------------------------------------------------------------------------------------------|
| **ID**<br/>       | ID<br/>    | No<br/> | Enables activity to be reference from the [**ActivityReference**](activityreference.md) element.<br/> <br/> |
| **parentID**<br/> | IDREF<br/> | No<br/> | Points to the parent of this activity. Source for this element is the assessment. <br/> <br/>                |



## Child elements



| Element                                                                       | Description                                                                                                                                                                        |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivityClass**](activityclass.md)<br/>                             | The class of this activity. <br/> <br/>                                                                                                                                |
| [**ActivityClassDisplayName**](activityclassdisplayname.md)<br/>       | Display name for the activity class.<br/> <br/>                                                                                                                        |
| [**ActivityDescription**](activitydescription.md)<br/>                 | Description of steps to resolve the issue.<br/> <br/>                                                                                                                  |
| [**ActivityEndThread**](activityendthread.md)<br/>                     | The thread id when the activity ended. Source for this element is the assessment.<br/> <br/>                                                                           |
| [**ActivityEndTime**](https://msdn.microsoft.com/library/windows/desktop/hh449252)<br/>                             | End time for this activity in nanoseconds.<br/> <br/>                                                                                                                  |
| [**ActivityInstance**](activityinstance.md)<br/>                       | Identifier for the activity.<br/> <br/>                                                                                                                                |
| [**ActivityInstanceDisplayName**](activityinstancedisplayname.md)<br/> | Display name for the activity instance.<br/> <br/>                                                                                                                     |
| [**ActivityStartThread**](activitystartthread.md)<br/>                 | The thread id when the activity started. The source for this element is the assessment.<br/> <br/>                                                                     |
| [**ActivityStartTime**](https://msdn.microsoft.com/library/windows/desktop/hh449256)<br/>                         | Start time for this activity in nanoseconds.<br/> <br/>                                                                                                                |
| [**ActivityTitle**](activitytitle.md)<br/>                             | Description of steps to resolve the issue.<br/> <br/>                                                                                                                  |
| [**Importance**](importance.md)<br/>                                   | The importance of the activity.<br/> <br/>                                                                                                                             |
| [**References**](references.md)<br/>                                   | Holds the [**MetricReference**](metricreference.md), [**IssueReference**](issuereference.md) and [**ActivityReference**](activityreference.md) element. <br/> <br/> |



### Child element sequence

``` syntax
(
  ActivityClass, 
  ActivityClassDisplayName, 
  ActivityEndThread, 
  ActivityEndTime, 
  ActivityInstance, 
  ActivityInstanceDisplayName, 
  ActivityStartThread, 
  ActivityStartTime, 
  ActivityTitle, 
  ActivityDescription, 
  Importance, 
  References
)
```

## Parent elements



| Element                                     | Description                                                           |
|---------------------------------------------|-----------------------------------------------------------------------|
| [**Activities**](activities.md)<br/> | A container element for **Activity** elements.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





