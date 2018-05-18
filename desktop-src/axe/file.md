---
title: File element
description: Holds information that describes a file.
ms.assetid: 'e2146b74-9914-436b-a339-8778e162bedc'
keywords: ["File element Access Execution Engine"]
topic_type:
- apiref
api_name:
- File
api_type:
- Schema
---

# File element

Holds information that describes a file.

## Usage

``` syntax
<File>
  child elements
</File>
```

## Attributes

There are no attributes.

## Child elements



| Element                                       | Description                                                            |
|-----------------------------------------------|------------------------------------------------------------------------|
| [**Company**](https://msdn.microsoft.com/library/windows/desktop/hh449366)<br/>         | Describes the company that generates the file. <br/> <br/> |
| [**FilePath**](https://msdn.microsoft.com/library/windows/desktop/hh437546)<br/>       | Path to the file.<br/> <br/>                               |
| [**FileVersion**](https://msdn.microsoft.com/library/windows/desktop/hh437552)<br/> | The file version. <br/> <br/>                              |



### Child element sequence

``` syntax
(
  FilePath, 
  FileVersion, 
  Company
)
```

## Parent elements



| Element                           | Description                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------|
| [**Trace**](trace.md)<br/> | An optional trace file associated with this iteration.<br/> <br/> |



## Remarks

Source for this element is the assessment.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





