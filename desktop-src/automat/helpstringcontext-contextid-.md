---
title: helpstringcontext(contextid)
description: Sets the string context in the Help file.
ms.assetid: 43b60fe6-bff0-45d8-81d6-075c1d4040a8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# helpstringcontext(contextid)

Sets the string context in the Help file.

## Parameters

<dl> <dt>

<span id="contextid"></span><span id="CONTEXTID"></span>*contextid*
</dt> <dd>

The ID for the context string.

</dd> </dl>

## Allowed on

Type library, type information (TypeInfo), function, and variable level.

## Remarks

Retrieved by the **GetDocumentation2** functions in the [**ITypeLib**](/windows/previous-versions/oaidl/nn-oaidl-itypelib?branch=master) and [**ITypeInfo2**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo2?branch=master) interfaces. The *contextid* is typically a 32-bit Help context identifier in the Help file.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




