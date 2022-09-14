---
title: Skin Definition File
description: Skin Definition File
ms.assetid: 'ed5f7c61-c830-4075-a79f-d5539454bd3b'
keywords:
- Windows Media Player skins,skin definition files
- skins,skin definition files
- files for skins,skin definition
- skin definition files,about
ms.topic: article
ms.date: 05/31/2018
---

# Skin Definition File

Skin definition files contain the basic instructions for what the skin does and where other files used by the skin can be found. There can only be one skin definition file for a skin, and it has a .wms file name extension.

The instructions in the skin definition file are written in Extensible Markup Language (XML), which is similar to HTML. If you have used HTML to create webpages, you will find that XML looks familiar.

The XML in the skin definition file uses a set of special element tags to define parts of the skin user interface. For example, the [BUTTON](button-element.md) element defines how a button will behave, where it will go, and what it will look like.

Each element tag has specific attributes. For example, the [BUTTON](button-element.md) element has an **image** attribute that defines where the picture for the button can be found. This is similar to HTML, where the BODY element will have a **bgcolor** attribute that defines the background color of the HTML page. Detailed information about all skin elements and their attributes is included in the [Skin Programming Reference](skin-programming-reference.md) section.

XML has a few simple rules that you need to know to create skins. Unlike HTML, XML requires you to follow the rules exactly.

## Enclose Elements with Angle Brackets

All elements are enclosed by angle brackets; for example, the **BUTTON** element is typed like this:


```C++
<BUTTON>

```



You do not need to type the word "BUTTON" in all uppercase letters, but the convention of typing element names in all uppercase is used in the example code of this SDK.

## Put Attributes Before the Closing Bracket

All attributes for a particular element must be included before the closing angle bracket. An attribute consists of the attribute name followed by an equal sign (=) and the value of the attribute in quotes.


```C++
<BUTTON image="mypic.jpg">

```



You do not need to type the word "image" in lowercase, but the convention of typing attribute names in lowercase is used in the example code of this SDK. Also note that the value of the attribute is enclosed in quotation marks.

## Opening and Closing Elements

Some elements are grouped together inside another element. For example, the **BUTTONGROUP** element does not make a lot of sense unless you use one or more **BUTTONELEMENT** elements with it. To make the grouping clear, you need to have an opening and closing tag for each element. The opening tag is just the element name and any related attributes, surrounded by angle brackets. The closing tag is the element name, preceded by a forward slash (/), and then enclosed by angle brackets. For example, the **BUTTONGROUP** element opening tag looks like this:


```C++
<BUTTONGROUP>

```



The closing **BUTTONGROUP** tag looks like this:


```C++
</BUTTONGROUP>

```



You would put the **BUTTONELEMENT** tags between the opening and closing **BUTTONGROUP** element tags. For example:


```C++
<BUTTONGROUP>
    <BUTTONELEMENT/>
    <BUTTONELEMENT/>
    <BUTTONELEMENT/>
</BUTTONGROUP>

```



## Closing Off Elements

If an element has no other elements inside it, you must put a forward slash at the end of the element name just before the closing angle bracket. For example, in the code above, each **BUTTONELEMENT** element has a forward slash to indicate that there are no other elements nested within it.

In other words, you must either have a closing element tag or close off your element with a forward slash.

This is correct:


```C++
<BUTTONGROUP>
    <BUTTONELEMENT/>
    <BUTTONELEMENT/>
</BUTTONGROUP>

```



This is not correct:


```C++
<BUTTONGROUP/>
    <BUTTONELEMENT/>
    <BUTTONELEMENT/>
</BUTTONGROUP>

```



This is also not correct:


```C++
<BUTTONGROUP>
    <BUTTONELEMENT>
    <BUTTONELEMENT>
</BUTTONGROUP>

```



The following section provides more information about skin definition files:

-   [Skin Definition File Structure](skin-definition-file-structure.md)

## Related topics

<dl> <dt>

[**Skin Files**](skin-files.md)
</dt> </dl>

 

 




