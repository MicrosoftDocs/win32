---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 2c796d5c-1556-4348-83e2-23e93780ebc1
title: Referencing Parameters
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Referencing Parameters

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

A concrete example of an Option that includes a ParameterRef element is the custom media size Option. Note that it references two parameters: PageMediaSizeMediaSizeWidth and PageMediaSizeMediaSizeHeight. Each ParameterRef instance refers to a ParameterDef instance that is defined elsewhere in the PrintCapabilities document. For information about the ParameterDef element, see [ParameterDef](parameterdef.md). For conceptual information about defining parameters, see [ParameterDef and ParameterInit Elements](parameterdef-and-parameterinit-elements.md).

``` syntax
<!--Example of ParamterRef usage within a Feature-->
<psf:Option name="psk:CustomMediaSize" constrained="psk:None">
  <psf:ScoredProperty name="psk:MediaSizeWidth">
    <psf:ParameterRef name="psk:PageMediaSizeMediaSizeWidth" />
  </psf:ScoredProperty>
  <psf:ScoredProperty name="psk:MediaSizeHeight">
    <psf:ParameterRef name="psk:PageMediaSizeMediaSizeHeight" />
  </psf:ScoredProperty>
</psf:Option>
```

Merely creating a parameterized Option is not sufficient to ensure that the Option will be handled and processed correctly. The PrintCapabilities/PrintTicket provider and clients must provide additional support to properly implement parameterized Option instances. The required behaviors are described in the following sections.

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 



