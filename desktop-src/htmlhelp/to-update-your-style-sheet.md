---
title: To update your style sheet
description: You can make your expandable sections stand out by updating your style sheet with a new class.
ms.assetid: '7745624E-2053-4771-A9EF-E8FB3720D30F'
---

# To update your style sheet

You can make your expandable sections stand out by updating your [style sheet](use-cascading-style-sheets.md) with a new class. Style sheets let you define the style attributes for the section. For example, you can make the section have a colored border, or a repeating graphic for the background. You can also add style attributes to fine-tune the spacing, margins, and overall positioning of the section.

## Example

This is the style class that we have defined for the sidebars in the HTML Help documentation:


```
<STYLE>
DIV.sidebartext {
position: relative;
left: -22px;
height: 72px;
width: 300px;
margin-top: .6em;
margin-right: 3em;
margin-left: 0;
margin-bottom: .6em;
padding-top: .75em;
padding-right: 6px;
padding-left: .75em;
padding-bottom: .75em;
cursor: hand;
border-left: 4pt solid #339900;
background-color: #F0F0F0; }
</STYLE>
```



> [!Note]  
> Because there are usually many style attributes associated with this kind of Dynamic HTML (DHTML) link, it is easiest to maintain the information as a class in a cascading style sheet, rather than as attributes in each instance of the link tag.

 

## Related topics

<dl> <dt>

[Back to the Beginning](example--create-expandable-sections-with-dhtml.md)
</dt> </dl>

 

 




