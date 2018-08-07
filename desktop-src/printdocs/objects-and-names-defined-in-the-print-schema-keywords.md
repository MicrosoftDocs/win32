---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 5a07ec21-dc7c-46d5-b1c2-de06f53fe6bf
title: Objects and Names Defined in the Print Schema Keywords
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Objects and Names Defined in the Print Schema Keywords

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

The Print Schema Framework defines a namespace that includes the elements and XML attributes defined in the Print Schema Keywords. This includes elements such as Feature, Option, and ScoredProperty; attribute names such as name and propagate; and values for XML attributes such as constrained. In other words, every use of a name that is defined in the Print Schema Keywords should be explicitly qualified with this namespace, or should be implicitly associated with this namespace by the use of a default xmlns attribute. The Print Schema Keywords document defines the public element instances that may appear in any given context or location. Element instances must appear only within the context or location designated in the Print Schema Framework. For example, the <psf:Option name= "psk:Letter"&gt; instance that is defined in the Print Schema Keywords must appear within the <psf:Feature name = "psk:PageMediaSize"&gt; instance (also defined in the Print Schema Keywords). You do not have the freedom to use a given Option instance outside of its specified context.

Privately-defined element instances may appear anywhere as long as the element type appears in a context allowed by the Print Schema Framework.

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 



