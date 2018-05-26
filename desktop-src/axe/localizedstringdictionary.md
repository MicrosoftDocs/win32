---
title: LocalizedStringDictionary element
description: The localized strings that should be displayed in a UI for localized nodes in the manifest.
ms.assetid: 6BF79DD4-B04B-441F-9EAF-B657AF9BDFC6
keywords:
- LocalizedStringDictionary element Access Execution Engine
topic_type:
- apiref
api_name:
- LocalizedStringDictionary
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LocalizedStringDictionary element

The localized strings that should be displayed in a UI for localized nodes in the manifest.

## Usage

``` syntax
<LocalizedStringDictionary>
  text
</LocalizedStringDictionary>
```

## Attributes

There are no attributes.

## Text value

This node holds the localized strings that should be displayed in a UI for localized nodes in the manifest. This node should not be populated in an assessment manifest by an assessment author. It is created by the AXE object model and populated when a job manifest is being written.

To localize an assessment manifest, the nodes being localized use a **\_locId** attribute, where the value is a unique identifier. A version of the assessment manifest is created for each language, and each is installed into a subdirectory of the assessment directory named for the language. An application such as "Windows Assessment Console" that creates job manifests loads each localized assessment manifest and stores the localized strings into the localized string dictionary. When the object model writes out the job manifest, this node will be populated.

## Child elements

There are no child elements.

## Parent elements



| Element                                                           | Description                                                             |
|-------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**AxeAssessmentManifest**](axeassessmentmanifest.md)<br/> | This is the root node of an assessment manifest.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



 

 





