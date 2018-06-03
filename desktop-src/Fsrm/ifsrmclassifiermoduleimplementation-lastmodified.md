---
title: IFsrmClassifierModuleImplementation LastModified property
description: The last time the classifier's internal rules were modified as a 64-bit FILETIME value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: edda630a-947d-4c81-b4d5-c02b3ba02f10
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- LastModified property File Server Resource Manager
- LastModified property File Server Resource Manager , IFsrmClassifierModuleImplementation interface
- IFsrmClassifierModuleImplementation interface File Server Resource Manager , LastModified property
topic_type:
- apiref
api_name:
- IFsrmClassifierModuleImplementation.LastModified
- IFsrmClassifierModuleImplementation.get_LastModified
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IFsrmClassifierModuleImplementation::LastModified property

The last time the classifier's internal rules were modified as a 64-bit FILETIME value.

This property is read-only.

## Syntax


```C++
HRESULT get_LastModified(
  [out] VARIANT *pLastModified
);
```



## Property value

Pointer to a **VARIANT** that contains the date for the last time the internal policies of the classifier was modified. The variant is of type **VT\_DECIMAL**. To access a value that can be directly converted into a [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284) structure, query the Low64 member of the **decVal** member of the variant.

<dt>

<span id="FsrmNeverModified"></span><span id="fsrmnevermodified"></span><span id="FSRMNEVERMODIFIED"></span>

<span id="FsrmNeverModified"></span><span id="fsrmnevermodified"></span><span id="FSRMNEVERMODIFIED"></span>**FsrmNeverModified** (0x0000000000000000)


</dt> <dd>

The classifier has no internal policies that are ever updated.

</dd> <dt>

<span id="FsrmAlwaysModified"></span><span id="fsrmalwaysmodified"></span><span id="FSRMALWAYSMODIFIED"></span>

<span id="FsrmAlwaysModified"></span><span id="fsrmalwaysmodified"></span><span id="FSRMALWAYSMODIFIED"></span>**FsrmAlwaysModified** (0xFFFFFFFFFFFFFFFF)


</dt> <dd>

The classifier has internal policies affecting rules that always need to be re-evaluated on each classification run.

</dd> <dt>

Any valid time stamp.
</dt> <dd>

This is the case when neither of the two previous constants are returned.

</dd> </dl>

## Error codes

The method returns the following return values.

<dl> <dt>

S\_OK
</dt> <dd>

Success.

</dd> </dl>

## Remarks

The last modified time is used by FSRM to determine whether rules using this classifier need to be run. If any classifier returns a time that is more recent than the time a file was last modified, FSRM will re-evaluate any applicable rules for that file.

A value corresponding to **FsrmNeverModified** can be returned if the classifier has no internal policies that are ever updated. An example of such a classifier is one that bases its classification decision on the attributes (such as path or owner) or content of a file.

A value corresponding to **FsrmAlwaysModified** can be returned if the classifier has internal policies that affect rules that always need to be reevaluated on each classification run. In this case, applicable rules for each file will always be evaluated. An example of such a classifier is one that bases its classification decision on a volatile set of policies that are outside the control of FSRM. A classifier that returns **FsrmAlwaysModified** will affect the performance of file classification because in such cases FSRM will skip optimizations that normally can avoid unnecessary rule reevaluations.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                      |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>                  |
| IID<br/>                      | IID\_IFsrmClassifierModuleImplementation is defined as 4c968fc6-6edb-4051-9c18-73b7291ae106<br/> |



## See also

<dl> <dt>

[**IFsrmClassifierModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduleimplementation)
</dt> </dl>

 

 





