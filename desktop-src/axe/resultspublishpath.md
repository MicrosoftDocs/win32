---
title: ResultsPublishPath element
description: Specifies a UNC path to a file containing results.
ms.assetid: 'BAA8E7D4-5DA3-4669-B737-1FF3A637B926'
keywords: ["ResultsPublishPath element Access Execution Engine"]
topic_type:
- apiref
api_name:
- ResultsPublishPath
api_type:
- Schema
---

# ResultsPublishPath element

Specifies a UNC path to a file containing results. At the end of a job, AXE aggregates all the XML results from each assessment, ETL files, and any other specified files (as cabinet files) and copies these results to this path.

## Usage

``` syntax
<ResultsPublishPath>
  text
</ResultsPublishPath>
```

## Attributes

There are no attributes.

## Text value

A UNC path to a file containing results. This path is processed using **ExpandEnvironmentStringsW**.

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                                                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**JobParameters**](jobparameters.md)<br/> | Describes the parameters for a job. These parameters control how a job runs, and can be read by an assessment.<br/> <br/> |



## Remarks

This path is processed using. AXE will process this path with the Win32 API ExpandEnvironmentStringsW() until no more expansions occur.

For single machine scenarios this should be a local path that is not in one of the Window's temporary directories. The solution determines this path.

Object Model Warnings Supported: If the path is not a valid UNC path.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





