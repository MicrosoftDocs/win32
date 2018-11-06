---
title: Scripting COM Objects in Custom Applications
description: Scripting COM Objects in Custom Applications
ms.assetid: 14e8cd53-e2b2-4393-8961-32efdf269f76
ms.topic: article
ms.date: 05/31/2018
---

# Scripting COM Objects in Custom Applications

Microsoft provides several environments for scripting COM objects: Active Server Pages, Windows Script Host, and so on. Independent software vendors (ISVs) can also license Microsoft scripting engines for use in their applications. For example, an ISV creating a word processor might want to add a macro language to the application so users could automate simple tasks. By licensing a scripting engine, the ISV can use a language such as VBScript or JScript as the application's macro language.

In addition to licensing VBScript and JScript scripting engines, ISVs can write their own ActiveX scripting engines. These scripting engines can then be plugged into any host environment that supports the ActiveX scripting engine standard. For example, an ISV might write a PerlScript scripting engine and install it on an ASP server, thus enabling the ASP server to process PerlScript scripts.

## Related topics

<dl> <dt>

[Scripting with COM Objects](scripting-with-com-objects.md)
</dt> </dl>

 

 




