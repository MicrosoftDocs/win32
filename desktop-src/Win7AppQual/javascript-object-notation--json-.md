---
description: JavaScript Object Notation (JSON)
ms.assetid: 2F6FDE88-C852-46BC-B6B1-630C266AF0AA
title: JavaScript Object Notation (JSON)
ms.topic: article
ms.date: 05/31/2018
---

# JavaScript Object Notation (JSON)

[JavaScript Object Notation (JSON)](https://www.json.org/) is a simple and lightweight data-interchange format that is based on a subset of the object literal notation of the JavaScript language. The JavaScript engine in Windows Internet Explorer 8 implements the [ECMAScript 3.1 JSON proposal](https://www.ecma-international.org/) for native JSON-handling functions (which uses [Douglas Crockford's json2.js API](https://github.com/douglascrockford/JSON-js/blob/master/json2.js)).

Internet Explorer 8 includes a native JSON object that complies with the JSON support that is described in the [ES3.1 Proposal Working Draft](https://www.ecma-international.org/). Some webpages detect the native JSON object, and then use it in a non-standard way. This usage typically causes a script error and breaks the handling of AJAX requests. The following code example shows the wrong way to use the JSON object.


```JScript
    if(!window.JSON) JSON = myJSON; 
    JSON.encode(obj); // Not part of the standard
```



Instead, the following code example shows a good way to use the JSON object.


```JScript
    JSON = myJSON; 
    JSON.encode(obj);
```



Windows Internet Explorer includes native supports for JSON by introducing a global JSON object that has two built-in methods: **stringify** and **parse**. The global JSON object is defined in the JavaScript engine and is created during the engine initialization phase. To maintain backward compatibility, this feature is available only when a website uses the latest version of JavaScript features by using the "Internet Explorer 8 Standards" layout (document) mode. This feature also might affect the behavior of webpages that depend on a global variable JSON or use [json2.js](https://github.com/douglascrockford/JSON-js/blob/master/json2.js).

You can override the global JSON object. But when a webpage uses the “Internet Explorer 8 Standards” layout (document) mode, it is not an undefined object anymore. Because JSON is instantiated as a global name by the JavaScript engine, checks like "if(!this.JSON)" evaluate to False and must be changed in the user code.

Webpages that use [json2.js](https://github.com/douglascrockford/JSON-js/blob/master/json2.js) are likely not affected. With few exceptions, these pages should work faster. The exceptions are because of the differences between the Internet Explorer native JSON implementation and json2.js. For example, during serialization, the native JSON implementation detects cycles and does not go in infinite recursion like json.js. For more information about these exceptions, see the [JavaScript Blogs](/archive/blogs/jscript/).

For more information, see [JSON Documentation](https://msdn.microsoft.com/library/cc836458(VS.85).aspx) and [Versioning and JavaScript Engine’s Version Support](https://www.microsoft.com/windows/internet-explorer/readiness/developers-new.aspx).

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 
