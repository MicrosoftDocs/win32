---
title: TestCaseCollection class
description: This interface provides containers for TestCase objects.
ms.assetid: '025CEEEA-264F-475B-9737-4E1754F01D0E'
keywords: ["TestCaseCollection class Access Execution Engine", "TestCaseCollection class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- TestCaseCollection
api_location:
- AxeCore.dll
api_type:
- COM
---

# TestCaseCollection class

This interface provides containers for [**TestCase**](testcase-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**TestCaseCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **TestCaseCollection** class has these methods.



| Method                                                                | Description                                                                                                |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**~TestCaseCollection**](testcasecollection--testcasecollection.md) | Destructor method.<br/>                                                                              |
| [**AddItem**](testcasecollection-additem.md)                         | Creates and adds a new [**TestCase**](testcase-struct.md) to the **TestCaseCollection**.<br/>       |
| [**Clear**](testcasecollection-clear.md)                             | Deletes all [**TestCase**](testcase-struct.md) objects from the **TestCaseCollection**.<br/>        |
| [**DeleteItem**](testcasecollection-deleteitem.md)                   | Deletes a [**TestCase**](testcase-struct.md) from the **TestCaseCollection**.<br/>                  |
| [**GetCount**](testcasecollection-getcount.md)                       | Returns the count of [**TestCase**](testcase-struct.md) objects in the **TestCaseCollection**.<br/> |
| [**GetItem**](testcasecollection-getitem.md)                         | Returns a [**TestCase**](testcase-struct.md) from the **TestCaseCollection**.<br/>                  |



 

## Remarks

The **TestCase** objects hold information from the **Iteration/TestCases/TestCase** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





