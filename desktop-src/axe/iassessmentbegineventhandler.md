---
title: IAssessmentBeginEventHandler class
description: The IAssessmentBeginEventHandler interface enables a solution to receive notification from the AXE engine when an assessment begins.
ms.assetid: 'F7FE28E5-DF6B-4A24-A237-B0AF7C9AC7F2'
keywords: ["IAssessmentBeginEventHandler class Access Execution Engine", "IAssessmentBeginEventHandler class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- IAssessmentBeginEventHandler
api_location:
- AxeCore.dll
api_type:
- COM
---

# IAssessmentBeginEventHandler class

The **IAssessmentBeginEventHandler** interface enables a solution to receive notification from the AXE engine when an assessment begins.

## When to implement

An **IAssessmentBeginEventHandler** interface should be implemented by a solution that needs to display the status of the current job to the user. It is also needed if the solution allows the user to cancel the currently running assessment.

**IAssessmentBeginEventHandler** has these types of members:

-   [Methods](#methods)

### Methods

The **IAssessmentBeginEventHandler** class has these methods.



| Method                                                 | Description                                                                                      |
|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**OnAssessmentBegin**](ievents-onassessmentbegin.md) | The AXE Core raises this event to notify the solution that an assessment has started.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Execution Solution Interfaces**](execution-solution-interfaces.md)
</dt> </dl>

 

 





