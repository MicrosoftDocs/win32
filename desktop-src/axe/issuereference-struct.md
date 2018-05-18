---
title: IssueReference class
description: This interface provides access to IssueReference objects.
ms.assetid: '351CA6AC-2045-47AB-A0C7-B841028CA5A2'
keywords: ["IssueReference class Access Execution Engine", "IssueReference class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- IssueReference
api_location:
- AxeCore.dll
api_type:
- COM
---

# IssueReference class

This interface provides access to **IssueReference** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**IssueReference** has these types of members:

-   [Methods](#methods)

### Methods

The **IssueReference** class has these methods.



| Method                                                            | Description                                                |
|:------------------------------------------------------------------|:-----------------------------------------------------------|
| [**~IssueReference**](issuereference--issuereference.md)         | Destructor method.<br/>                              |
| [**GetAttributeIssueID**](issuereference-getattributeissueid.md) | Returns the issue ID of the **IssueReference**.<br/> |
| [**SetAttributeIssueID**](issuereference-setattributeissueid.md) | Sets the issue ID of the **IssueReference**.<br/>    |



 

## Remarks

An **IssueReference** holds data from an **Activity/References/IssueReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





