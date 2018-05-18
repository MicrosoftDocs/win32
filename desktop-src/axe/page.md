---
title: Page element
description: A description of a page.
ms.assetid: '7C501030-61B9-416B-AF21-0A61DF8F4355'
keywords: ["Page element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Page
api_type:
- Schema
---

# Page element

A description of a page.

## Usage

``` syntax
<Page>
  child elements
</Page>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                                                                                               |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**Description**](description.md)<br/>     | This node contains the description of the page. The programmatic name is used to link to the page and is required.<br/> <br/> |
| [**Groups**](groups.md)<br/>               | This node is a container for one or more groups.<br/> <br/>                                                                   |
| [**TestCaseTable**](testcasetable.md)<br/> | The test case table node defines a table of test cases on a page.<br/> <br/>                                                  |



### Child element sequence

``` syntax
DescriptionGroupsTestCaseTable
```

## Parent elements



| Element                           | Description                                                                           |
|-----------------------------------|---------------------------------------------------------------------------------------|
| [**Pages**](pages.md)<br/> | A collection of Page nodes describing all pages in the report.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





