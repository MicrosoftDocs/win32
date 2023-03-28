---
title: Translating to JScript from JavaScript
description: Translating to JScript from JavaScript
ms.assetid: 86067a69-a6a1-474f-b8d8-85caf384a311
ms.topic: article
ms.date: 03/28/2023
---

# Translating to JScript from JavaScript

JScript is largely compatible with JavaScript. However, JScript version 5.0 includes some objects that aren't currently supported by JavaScript; such as ActiveXObject, Enumerator, Error, Global, and VBArray.

JScript 5.0 supports exception handling through **try**...**catch** statements; just as JavaScript does.

When working with either JScript or JavaScript, there are some subtle differences between the object model implementations supported by various Web browsers. To write script that runs on both Internet Explorer and Netscape Navigator, limit the features used by your scripts to those specified in the World Wide Web Consortium (W3C) standard for HTML version 3.2. For more information about this standard, see [HTML 3.2 Reference Specification](https://www.w3.org/TR/REC-html32.html).

## Related topics

* [Translating to JScript](translating-to-jscript.md)
