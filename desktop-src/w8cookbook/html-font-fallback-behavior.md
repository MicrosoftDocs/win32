---
title: HTML font fallback behavior
description: HTML font fallback behavior
ms.assetid: 5BDFBD58-0B34-4A58-BFAF-B8BB1DD569DB
ms.topic: article
ms.date: 05/31/2018
---

# HTML font fallback behavior

## Platform

Clients -** Windows 8.1  
**Servers -** Windows Server 2012 R2  


## Description

Microsoft is updating the logic for UI fonts for several languages in Windows Store apps using HTML. Rather than using a single font for all languages, the UI font will now be determined on a per language basis. For example, UI fonts for Japanese will now be Meiryo UI in apps that use HTML.

## Manifestation

Apps that depended on an old font may look different; while your app appearance will be improved overall thanks to more readable fonts, there could be an issue with layouts that depend on pixel-perfect content sizes. For example, some lines of content may be bigger than they were previously, causing unexpected line breaks and/or resizing of container elements. However, in practice we haven’t noticed any issues with any existing apps.

## Solution

Affected apps can mitigate this behavior by specifying a given font via CSS (for example, “font-family: Meiryo UI”) instead of relying on the old default fonts. The following table provides the UI font for each of the script names.



| Script Name        | UI Font               |
|--------------------|-----------------------|
| Arabic             | Segoe UI              |
| Armenian           | Segoe UI              |
| Bengali            | Nirmala UI            |
| Bopomofo           | Microsoft JhengHei UI |
| Braille            | Segoe UI Symbol       |
| Buginese           | Leelawadee UI         |
| Canadian Syllabics | Gadugi                |
| Cherokee           | Gadugi                |
| Coptic             | Segoe UI Symbol       |
| Han (Simplified)   | Microsoft YaHei UI    |
| Han (Traditional)  | Microsoft JhengHei UI |
| Cyrillic           | Segoe UI              |
| Devanagari         | Nirmala UI            |
| Deseret            | Segoe UI Symbol       |
| Ethiopic           | Ebrima                |
| Georgian           | Segoe UI              |
| Glagolitic         | Segoe UI Symbol       |
| Gothic             | Segoe UI Symbol       |
| Greek              | Segoe UI              |
| Gujarati           | Nirmala UI            |
| Gurmukhi           | Nirmala UI            |
| Hebrew             | Segoe UI              |
| Old Italic         | Segoe UI Symbol       |
| Javanese           | Javanese Text         |
| Japanese           | Meiryo UI             |
| Kannada            | Mirmala UI            |
| Khmer              | Leelawadee UI         |
| Korean             | Malgun Gothic         |
| Lao                | Leelawadee            |
| Latin              | Segoe UI              |
| Malayalam          | Nirmala UI            |
| Mongolian          | Mongolian Baiti       |
| Myanmar            | Myanmar Text          |
| N'Ko               | Ebrima                |
| Ogham              | Segoe UI Symbol       |
| Ol Chiki           | Nirmala UI            |
| Old Turkic         | Segoe UI Symbol       |
| Oriya              | Nirmala UI            |
| Osmanya            | Ebrima                |
| Phags-pa           | Microsoft PhagsPa     |
| Runic              | Segoe UI Symbol       |
| Sora Sompeng       | Nirmala UI            |
| Sinhala            | Nirmala UI            |
| Syriac             | Estrangelo Edessa     |
| Tai Le             | Microsoft Tai Le      |
| New Tai Lue        | Microsoft New Tai Lue |
| Tamil              | Nirmala UI            |
| Telugu             | Nirmala UI            |
| Tifinagh           | Ebrima                |
| Thaana             | MV Boli               |
| Thai               | Leelawadee UI         |
| Tibetan            | Microsoft Himalaya    |
| Vai                | Ebrima                |
| Yi                 | Microsoft Yi Baiti    |



 

 

 




