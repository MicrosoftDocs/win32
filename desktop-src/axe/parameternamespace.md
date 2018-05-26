---
title: ParameterNamespace enumeration
description: Specifies which set of parameters to retrieve.
ms.assetid: 7BC209BC-0F9D-40A2-9649-CB0658325F58
keywords:
- ParameterNamespace enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- ParameterNamespace
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ParameterNamespace enumeration

Specifies which set of parameters to retrieve.

## Syntax


```C++
enum ParameterNamespace {
  ParameterNamespaceNone        = 0, 
  ParameterNamespaceAssessment, 
  ParameterNamespaceJob, 
  ParameterNamespaceSession, 
  ParameterNamespaceInvalid 

};
```



## Constants

<dl> <dt>

<span id="ParameterNamespaceNone"></span><span id="parameternamespacenone"></span><span id="PARAMETERNAMESPACENONE"></span>**ParameterNamespaceNone**
</dt> <dd>

No namespace was specified. This is an invalid value.

</dd> <dt>

<span id="ParameterNamespaceAssessment"></span><span id="parameternamespaceassessment"></span><span id="PARAMETERNAMESPACEASSESSMENT"></span>**ParameterNamespaceAssessment**
</dt> <dd>

Assessment parameters are specific to the running assessment and as they were defined by the author of the assessment in the assessment manifest.

</dd> <dt>

<span id="ParameterNamespaceJob"></span><span id="parameternamespacejob"></span><span id="PARAMETERNAMESPACEJOB"></span>**ParameterNamespaceJob**
</dt> <dd>

Job level parameters are set by the job author when the job is created.

</dd> <dt>

<span id="ParameterNamespaceSession"></span><span id="parameternamespacesession"></span><span id="PARAMETERNAMESPACESESSION"></span>**ParameterNamespaceSession**
</dt> <dd>

Session parameters provided by Axe.

</dd> <dt>

<span id="ParameterNamespaceInvalid"></span><span id="parameternamespaceinvalid"></span><span id="PARAMETERNAMESPACEINVALID"></span>**ParameterNamespaceInvalid**
</dt> <dd>

An invalid value. This value is primarily for controlling the exit from loops.

</dd> </dl>

## Remarks

Managed code uses the [**ParameterNamespace**](axe-parameternamespace_om) enum.

AXE supports three parameter namespaces.

Assessment Parameters:

<dl> The assessment defines parameters in the assessment manifest. When the job is created, the user specifies the values for each parameter. The parameter name and value pairs are stored in the job manifest. Specifying the ASSESSMENT namespace allows the assessment to ask the engine for the parameter object for a given assessment parameter.  
Assessment parameters can be anything defined by the Assessment author. Examples include iterations, specific workloads to run, or any other type of value an assessment needs operationally.  
</dl>

Job Parameters:

<dl> A person can provide values for the Job level parameter when the Job is created. An assessment can obtain job parameter values by using the JOB namespace.  
</dl>

Session Parameters:

<dl> These parameters are defined by AXE at run time.  
</dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





