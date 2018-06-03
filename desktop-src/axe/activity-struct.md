---
title: Activity class
description: This interfaces provides access to Activity objects.
ms.assetid: 1584482D-C7A5-4062-9984-CB3416CB6C93
keywords:
- Activity class Access Execution Engine
- Activity class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Activity
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Activity class

This interfaces provides access to **Activity** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**Activity** has these types of members:

-   [Methods](#methods)

### Methods

The **Activity** class has these methods.



| Method                                                                            | Description                                                                                            |
|:----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**~Activity**](activity--activity.md)                                           | Destructor method.<br/>                                                                          |
| [**AddReference**](activity-addreference.md)                                     | Creates an [**IssueReference**](issuereference-struct.md) and adds it to the **Activity**.<br/> |
| [**ClearTrace**](activity-cleartrace.md)                                         | Clears the [**Trace**](trace-struct.md) settings of the **Activity**.<br/>                      |
| [**GetActivityClass**](activity-getactivityclass.md)                             | Returns the activity class of the **Activity**.<br/>                                             |
| [**GetActivityClassDisplayName**](activity-getactivityclassdisplayname.md)       | Returns the activity class display name of the **Activity**.<br/>                                |
| [**GetActivityDescription**](activity-getactivitydescription.md)                 | Returns the activity description of the **Activity**.<br/>                                       |
| [**GetActivityEndThread**](activity-getactivityendthread.md)                     | Returns the activity end thread of the **Activity**.<br/>                                        |
| [**GetActivityEndTime**](activity-getactivityendtime.md)                         | Returns the activity end time of the **Activity**.<br/>                                          |
| [**GetActivityInstance**](activity-getactivityinstance.md)                       | Returns the activity instance of the **Activity**.<br/>                                          |
| [**GetActivityInstanceDisplayName**](activity-getactivityinstancedisplayname.md) | Returns the activity instance display name of the **Activity**.<br/>                             |
| [**GetActivityStartThread**](activity-getactivitystartthread.md)                 | Returns the activity start thread of the **Activity**.<br/>                                      |
| [**GetActivityStartTime**](activity-getactivitystarttime.md)                     | Returns the activity start time of the **Activity**.<br/>                                        |
| [**GetActivityTitle**](activity-getactivitytitle.md)                             | Returns the activity title of the **Activity**.<br/>                                             |
| [**GetAttributeID**](activity-getattributeid.md)                                 | Returns the **ID** of the **Activity**.<br/>                                                     |
| [**GetAttributeParentID**](activity-getattributeparentid.md)                     | Returns the parent ID of the **Activity**.<br/>                                                  |
| [**GetImportance**](activity-getimportance.md)                                   | Returns the importance of the **Activity**.<br/>                                                 |
| [**GetReferences**](activity-getreferences.md)                                   | Returns the [**ReferenceCollection**](referencecollection.md) of the **Activity**.<br/>         |
| [**GetTrace**](activity-gettrace.md)                                             | Returns the [**Trace**](trace-struct.md) of the **Activity**.<br/>                              |
| [**GetTraceFile**](activity-gettracefile.md)                                     | Returns the trace file name of the **Activity**.<br/>                                            |
| [**GetTraceLink**](activity-gettracelink.md)                                     | Returns the trace link of the **Activity**.<br/>                                                 |
| [**GetTraceName**](activity-gettracename.md)                                     | Returns the trace name of the **Activity**.<br/>                                                 |
| [**GetTraceToolTip**](activity-gettracetooltip.md)                               | Returns the trace tooltip of the **Activity**.<br/>                                              |
| [**SetActivityClass**](activity-setactivityclass.md)                             | Sets the activity class of the **Activity**.<br/>                                                |
| [**SetActivityClassDisplayName**](activity-setactivityclassdisplayname.md)       | Sets the activity class display name of the **Activity**.<br/>                                   |
| [**SetActivityDescription**](activity-setactivitydescription.md)                 | Sets the activity description of the **Activity**.<br/>                                          |
| [**SetActivityEndThread**](activity-setactivityendthread.md)                     | Sets the activity end thread of the **Activity**.<br/>                                           |
| [**SetActivityEndTime**](activity-setactivityendtime.md)                         | Sets the activity end time of the **Activity**.<br/>                                             |
| [**SetActivityInstance**](activity-setactivityinstance.md)                       | Sets the activity instance of the **Activity**.<br/>                                             |
| [**SetActivityInstanceDisplayName**](activity-setactivityinstancedisplayname.md) | Sets the activity instance display name of the **Activity**.<br/>                                |
| [**SetActivityStartThread**](activity-setactivitystartthread.md)                 | Sets the activity start thread of the **Activity**.<br/>                                         |
| [**SetActivityStartTime**](activity-setactivitystarttime.md)                     | Sets the activity start time of the **Activity**.<br/>                                           |
| [**SetActivityTitle**](activity-setactivitytitle.md)                             | Sets the activity title of the **Activity**.<br/>                                                |
| [**SetAttributeID**](activity-setattributeid.md)                                 | Sets the ID of the **Activity**.<br/>                                                            |
| [**SetAttributeParentID**](activity-setattributeparentid.md)                     | Sets the parent ID of the **Activity**.<br/>                                                     |
| [**SetImportance**](activity-setimportance.md)                                   | Sets the importance of the **Activity**.<br/>                                                    |
| [**SetTrace**](activity-settrace.md)                                             | Overloaded. Sets [**Trace**](trace-struct.md) settings of the **Activity**.<br/>                |
| [**SetTraceFile**](activity-settracefile.md)                                     | Sets the trace file name of the **Activity**.<br/>                                               |
| [**SetTraceLink**](activity-settracelink.md)                                     | Sets the trace link of the **Activity**.<br/>                                                    |
| [**SetTraceName**](activity-settracename.md)                                     | Sets the trace name of the **Activity**.<br/>                                                    |
| [**SetTraceToolTip**](activity-settracetooltip.md)                               | Sets the trace tooltip of the **Activity**.<br/>                                                 |



 

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





