---
title: Using JavaScript and JScript
description: Using JavaScript and JScript
ms.assetid: c6927663-9432-4fa9-8de6-abb7237909b9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using JavaScript and JScript

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

If you use JavaScript or Microsoft JScript to access Microsoft Agent's programming interface, follow the conventions for this language for specifying methods or properties:

``` syntax
agent.object.Method (parameter)
agent.object.Property = value
```

JavaScript does not currently have event syntax for non-HTML objects. However, with Internet Explorer you can use the &lt;SCRIPT&gt; tag's **For...Event** syntax:

``` syntax
<SCRIPT LANGUAGE="JScript" FOR="object" EVENT="event()">
statements
</SCRIPT>
```

Because not all browsers currently support this event syntax, you may want to use JavaScript only for pages that support Microsoft Internet Explorer or for code that does not require event handling.

To access Agent's object collections, use the JScript [**Enumerator**](lwef-enumerator_function) function. However, versions of JScript included prior to Internet Explorer 4.0 do not support this function and do not support collections. To access methods and properties of the [**Character**](https://msdn.microsoft.com/library/windows/desktop/ms696372) object, use the [**Character**](character-method.md) method. Similarly, to access the properties of a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object, use the [**Command**](command-method.md) method.

 

 




