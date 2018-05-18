---
title: IAssessmentEndEventHandler class
description: The IAssessmentEndEventHandler interface enables a solution to receive notification from the AXE engine when an assessment has finished.
ms.assetid: '9327B389-2B20-418D-98C3-ED7AF923F003'
keywords: ["IAssessmentEndEventHandler class Access Execution Engine", "IAssessmentEndEventHandler class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- IAssessmentEndEventHandler
api_location:
- AxeCore.dll
api_type:
- COM
---

# IAssessmentEndEventHandler class

The **IAssessmentEndEventHandler** interface enables a solution to receive notification from the AXE engine when an assessment has finished.

## When to implement

An **IAssessmentEndEventHandler** interface should be implemented by a solution that needs to display the status and assessment errors of the job to the user.

**IAssessmentEndEventHandler** has these types of members:

-   [Methods](#methods)

### Methods

The **IAssessmentEndEventHandler** class has these methods.



| Method                                             | Description                                                                                    |
|:---------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**OnAssessmentEnd**](ievents-onassessmentend.md) | The AXE Core raises this event to notify the solution that an assessment has ended.<br/> |



 

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

 

 





