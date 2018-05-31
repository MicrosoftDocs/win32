---
title: Coding the PARAM Tag
description: Coding the PARAM Tag
ms.assetid: FA715EE3-95E9-4c59-891B-B074850E7579
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Coding the PARAM Tag

The &lt;PARAM&gt; tag is used to pass a sequence of [parameters](parameters.md) to the HTML Help ActiveX control to specify a feature and any additional information that the feature may require.

The &lt;PARAM&gt; tag is valid only within an &lt;OBJECT&gt; tag. The end tag is optional.



| Attribute | Description                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------|
| **NAME**  | Specifies a parameter. The first parameter in the sequence must be [Command](command-parameter.md). |
| **VALUE** | Specifies a valid value for the parameter specified in the **NAME** attribute.                       |



 

## Notes

-   Never omit the &lt;PARAM&gt; tag from an HTML Help ActiveX control &lt;OBJECT&gt; tag, as this may result in unexpected behavior.
-   For more information about other attributes supported by the &lt;OBJECT&gt; and &lt;PARAM&gt; tags, see a comprehensive HTML Reference, such as the HTML Elements reference on the MSDN Online Web Workshop.

## Related topics

<dl> <dt>

[About the HTML Help ActiveX Control](html-help-activex-control-overview.md)
</dt> </dl>

 

 




