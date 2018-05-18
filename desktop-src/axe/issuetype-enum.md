---
title: IssueType enumeration
description: Specifies the types of issues that can occur in Axe.
ms.assetid: 'A7B92F3B-7949-42B5-B04C-CE7ABB4A10C6'
keywords: ["IssueType enumeration Access Execution Engine"]
topic_type:
- apiref
api_name:
- IssueType
api_location:
- AxeCore.h
api_type:
- HeaderDef
---

# IssueType enumeration

Specifies the types of issues that can occur in Axe.

## Syntax


```C++
enum IssueType {
  IssueTypeNone     = 0, 
  IssueTypeInfo     = 1, 
  IssueTypeWarning  = 2, 
  IssueTypeError    = 3, 
  IssueTypeInvalid  = 4 

};
```



## Constants

<dl> <dt>

<span id="IssueTypeNone"></span><span id="issuetypenone"></span><span id="ISSUETYPENONE"></span>**IssueTypeNone**
</dt> <dd>

No error type was specified. This is an invalid value.

</dd> <dt>

<span id="IssueTypeInfo"></span><span id="issuetypeinfo"></span><span id="ISSUETYPEINFO"></span>**IssueTypeInfo**
</dt> <dd>

This issue is only informational.

</dd> <dt>

<span id="IssueTypeWarning"></span><span id="issuetypewarning"></span><span id="ISSUETYPEWARNING"></span>**IssueTypeWarning**
</dt> <dd>

This issue is a warning that should not block execution or cause it to fail prematurely.

</dd> <dt>

<span id="IssueTypeError"></span><span id="issuetypeerror"></span><span id="ISSUETYPEERROR"></span>**IssueTypeError**
</dt> <dd>

This issue is an error that has blocked execution or caused it to fail prematurely.

</dd> <dt>

<span id="IssueTypeInvalid"></span><span id="issuetypeinvalid"></span><span id="ISSUETYPEINVALID"></span>**IssueTypeInvalid**
</dt> <dd>

This is an invalid issue type. This enumerator is most often used for range checking the enumerator values. It should not be used to report any real issues.

</dd> </dl>

## Remarks

Managed code uses the [**IssueType**](axe-issuetype_om) enum.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl> |



 

 





