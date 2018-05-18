---
title: ExitValueMeaning element
description: Indicates whether the exit value means success or is a HRESULT.
ms.assetid: '338AAC69-4B23-4E23-9627-443EE93412E2'
keywords: ["ExitValueMeaning element Access Execution Engine"]
topic_type:
- apiref
api_name:
- ExitValueMeaning
api_type:
- Schema
---

# ExitValueMeaning element

Indicates whether the exit value means success or is a **HRESULT**.

## Usage

``` syntax
<ExitValueMeaning>
  child elements
</ExitValueMeaning>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                     | Description                                                                                                           |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**ExitValueIsHresult**](exitvalueishresult.md)<br/> | AXE should interpret the process exit value as an **HRESULT** to determine success or failure.<br/> <br/> |
| [**ZeroIsSuccess**](zeroissuccess.md)<br/>           | AXE should interpret the process exit value of zero to mean the assessment was successful.<br/> <br/>     |



### Child element sequence

``` syntax
(
  ZeroIsSuccess, 
  ExitValueIsHresult
)
```

## Parent elements



| Element                                     | Description                                               |
|---------------------------------------------|-----------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This element describes properties.<br/> <br/> |



## Remarks

Although Windows treats process exit values as unsigned values, some executables may return an **HRESULT** as their exit code.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





