---
title: SAMI File Example
description: SAMI File Example
ms.assetid: 52b566f1-0d87-4bf2-87b3-3821e69a5699
keywords:
- Windows Media Player,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player object model,Synchronized Accessible Media Interchange (SAMI)
- object model,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player Mobile,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player Mobile ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- Synchronized Accessible Media Interchange (SAMI),files
- SAMI (Synchronized Accessible Media Interchange),files
- Synchronized Accessible Media Interchange (SAMI),example code
- SAMI (Synchronized Accessible Media Interchange),example code
ms.topic: article
ms.date: 05/31/2018
---

# SAMI File Example

The following example code is a complete SAMI file with one set of closed caption text and several class declarations for text style and caption language.


```C++
<SAMI>
<HEAD>
   <STYLE TYPE = "text/css">
   <!--
   /* P defines the basic style selector for closed caption paragraph text */
   P {font-family:sans-serif; color:white;}
   /* Source, Small, and Big define additional ID selectors for closed caption text */
   #Source {color: orange; font-family: arial; font-size: 12pt;}
   #Small {Name: SmallTxt; font-size: 8pt; color: yellow;}
   #Big {Name: BigTxt; font-size: 12pt; color: magenta;}
   /* ENUSCC and FRFRCC define language class selectors for closed caption text */
   .ENUSCC {Name: 'English Captions'; lang: en-US; SAMIType: CC;}
   .FRFRCC {Name: 'French Captions'; lang: fr-FR; SAMIType: CC;}
   -->
   </STYLE>
</HEAD>
<BODY>
   <!<entity type="mdash"/>- The closed caption text displays at 1000 milliseconds. -->
   <SYNC Start = 1000>
      <!-- English closed captions -->
      <P Class = ENUSCC ID = Source>Narrator
      <P Class = ENUSCC>Great reason to visit Seattle, brought to you by two out-of-staters.
      <!-- French closed captions -->
      <P Class = FRFRCC ID = Source>Narrateur
      <P Class = FRFRCC>Deux personnes ne venant la r&eacute;gion vous donnent de bonnes raisons de visiter Seattle.
</BODY>
</SAMI>

```



Styles defined within a SAMI file conform to standard CSS selector syntax for elements, classes, and IDs. In the BODY element, all P elements have the style defined for the P element selector in the STYLE element. The class attribute of an element specifies the language of that element as defined by the class selectors in the STYLE element (the selectors beginning with periods). The language names specified by the class selectors can be any string. Elements with the ID attribute specified have additional styling applied as indicated by the ID selectors in the STYLE element (the selectors prefixed with \# characters).

When used in conjunction with the Windows Media Player object model, the class selectors correspond to the *ClosedCaption*.**SAMILang** property, which can be used to specify the language of the captions. The ID selectors correspond to the *ClosedCaption*.**SAMIStyle** property, which can be used to specify the style the captions will appear in.

For more information about creating SAMI files, see Understanding SAMI 1.0 at the [Microsoft website](/docs/).

## Related topics

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> </dl>

 

 
