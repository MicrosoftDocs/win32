---
title: helpstringcontext(contextid)
description: Sets the string context in the Help file.
ms.assetid: 43b60fe6-bff0-45d8-81d6-075c1d4040a8
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Retrieved by the **GetDocumentation2** functions in the [**ITypeLib**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypelib) and [**ITypeInfo2**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypeinfo2) interfaces. The *contextid* is typically a 32-bit Help context identifier in the Help file.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




