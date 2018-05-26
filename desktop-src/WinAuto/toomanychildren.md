---
title: TooManyChildren
description: TooManyChildren
ms.assetid: BF667CDC-C1F9-44B2-B64C-CD7F085CA364
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TooManyChildren

## Text

Stopped looking for additional siblings after finding {0} siblings. Possible incorrect tree

## Type

Warning

## Description

The element tree might be cyclic and the tree depth infinite.

This issue can cause navigation problems for automated tools because they will enter what appears to be a circular reference or infinite loop.

## Possible causes

-   Application or control design may be too complex. This warning might be reported for list-view controls that have a large number of items. In these cases, you can typically ignore this warning.
-   An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[**IAccessible::accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
</dt> </dl>

 

 




