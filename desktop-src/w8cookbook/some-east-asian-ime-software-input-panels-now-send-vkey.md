---
title: Some East Asian IME software input panels now send vKey
description: Some East Asian IME software input panels now send vKey
ms.assetid: 5E3BE112-D962-4C11-B31E-229584191FAE
ms.topic: article
ms.date: 05/31/2018
---

# Some East Asian IME software input panels now send vKey

## Platforms

<dl> Clients - Windows 8.1  
Servers - Windows Server 2012 R2  
</dl>

## Description

In Windows 8, if one of the East Asian IMEs is selected, pressing a software input panel key did not send vKeys.

In Windows 8.1, vKeys are sent for the following configurations:



| Language            | IME                                 | Windows Store | Desktop |
|---------------------|-------------------------------------|---------------|---------|
| Simplified Chinese  | Microsoft Pinyin, Microsoft Wubi    | Yes           | Yes     |
| Traditional Chinese | Microsoft Changlie, Microsoft Quick | Yes           | Yes     |
| Traditional Chinese | Microsoft Bopomofo                  | No            | No      |
| Korean              | Microsoft IME                       | Yes           | No      |
| Japanese            | Microsoft IME                       | No            | No      |



 

## Manifestations

If the user chooses an IME that does not send vKeys, vKey-triggered functions do not work.

## Solution

Applications that do not use one of the above IME configurations must be designed so that users can complete the desired task without using functions that require vKeys.

If the user chooses an IME that does send vKeys, but the application was designed without that expectation, the application must be changed to recognize which version of Windows is running and respond accordingly.

 

 




