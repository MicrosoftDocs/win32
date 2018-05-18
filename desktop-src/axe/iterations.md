---
title: Iterations element
description: A container element for one or more Iteration elements.
ms.assetid: '47DDC69B-3997-4DBA-A488-DA50CE8D52E9'
keywords: ["Iterations element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Iterations
api_type:
- Schema
---

# Iterations element

A container element for one or more [**Iteration**](iteration.md) elements.

## Usage

``` syntax
<Iterations>
  child elements
</Iterations>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------|
| [**Iteration**](iteration.md)<br/> | Receives metric values for a single assessment iteration.<br/> <br/> |



### Child element sequence

``` syntax
Iteration
```

## Parent elements



| Element                                                 | Description                                                               |
|---------------------------------------------------------|---------------------------------------------------------------------------|
| [**AssessmentResult**](assessmentresult.md)<br/> | Describes the result for an individual assessment.<br/> <br/> |



## Examples

The hierarchy looks like this with irrelevant elements omitted.

``` syntax
<AssessmentResults>
    <AssessmentResult>
        <Iterations>
            <Iteration>  ...  </Iteration>
                <Iteration>  ...  </Iteration>
                <Iteration>  ...  </Iteration>
        </Iterations>
        </AssessmentResult>
        <AssessmentResult>
            <Iteration>  ...  </Iteration
        </AssessmentResult>
    </AssessmentResults>
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





