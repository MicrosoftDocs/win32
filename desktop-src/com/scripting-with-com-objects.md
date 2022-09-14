---
title: Scripting with COM Objects
description: Scripting with COM Objects
ms.assetid: d99a561b-67dc-4fc9-adfa-cd7350eb16ba
ms.topic: article
ms.date: 05/31/2018
---

# Scripting with COM Objects

A *scripting language* is a programming language that is parsed at run time by a *scripting engine*, a component that translates scripts written in that language into machine code. Each scripting engine translates a specific scripting language. A *scripting host* is an application, such as a Web browser, that hosts a scripting engine to run scripts. If your scripting host supports COM, you can write scripts that use COM objects. The following topics describe scripting hosts that support COM objects, common scripting languages, and how to translate between scripting languages.

A scripting language differs from a compiled language in that it is translated into machine code at run time. This means that each time you run a script, the scripting engine first parses the code and then runs it. In contrast, compiled languages, such as C++, are translated to machine code once, during compilation. When you run a compiled application, the operating system simply runs the precompiled code.

Because a scripting engine must reparse a script each time it runs, scripting languages are typically slower and less efficient than their precompiled counterparts. The advantage of scripts, however, is they are easy to write and maintain. Scripting languages are usually simpler than precompiled languages, and when a script changes, it does not need to be recompiled. For lightweight and rapidly changing applications, such as webpages, scripting languages are ideal.

There are several host environments in which you can write scripts that use COM objects, as described following:

-   [Embedding COM Objects in Web Pages](embedding-com-objects-in-web-pages.md)
-   [Using COM Objects in Active Server Pages](using-com-objects-in-active-server-pages.md)
-   [Using COM Objects in Windows Script Host](using-com-objects-in-windows-script-host.md)
-   [Scripting COM Objects in Custom Applications](scripting-com-objects-in-custom-applications.md)

In each of the host environments mentioned preceding, a scripting engine parses and runs the script. Because the engine for each scripting language is a separate component, you can add a new scripting language to an environment by adding a new engine.

The most commonly used scripting languages are:

-   Microsoft Visual Basic Scripting Edition (VBScript), a subset of Visual Basic.
-   JavaScript, the Netscape scripting language, formerly known as LiveScript.
-   Microsoft JScript development software, the Microsoft implementation of the ECMA 262 language specification.

Microsoft provides scripting engines for JScript and VBScript. Other software companies provide ActiveX scripting engines for languages such as PerlScript, PScript, Python, and others.

For more information see the [ECMA 262 language specification](https://www.ecma-international.org/publications/standards/Ecma-262.htm).

Note that most scripting languages, such as VBScript and JScript, cannot access or modify files. This inability prevents the script from altering data on client computers. COM objects, however, have no such limitations. Once they are downloaded and installed on client computers, they can perform any standard application action. Thus, users should only download and run ActiveX controls from trusted sources.

For information on translating between scripting languages, see the following topics:

-   [Translating to VBScript](translating-to-vbscript.md)
-   [Translating to JScript](translating-to-jscript.md)
-   [Translating to JavaScript](translating-to-javascript.md)

 

 




